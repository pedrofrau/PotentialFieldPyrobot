# robot goes forward and then slows to a stop when it detects something  
   
from pyrobot.brain import Brain
from random import randint
import math

		
def adjust(theta):
   while theta > math.pi:
      theta -= 2 * math.pi
   while theta < - math.pi:
      theta += 2 * math.pi
   return theta

   
class Practica(Brain):  
   global i
   i = 0
   global goal
   
   #Waypoints declaration
   goal = [[1, 4], [4, 4], [4, 1], [8, 1], [8, 5], [7, 7], [9, 7]]
            
   def step(self):  
      global i
      goalReached = False
      
      #New goal declaration      
      goal_x = goal[i][0]
      goal_y = goal[i][1] 
      print i
      
      #Simulated robot position
      x = self.robot.simulation[0].getPose(0)[0]
      y = self.robot.simulation[0].getPose(0)[1]
      th = self.robot.simulation[0].getPose(0)[2]
      
      #Robot direction depending on the goal
      phi = math.atan2(goal_y-y, goal_x-x) - math.pi/2
      cmd = adjust(phi) - adjust(th)

      #Connditions to move and/or change goal
      if math.fabs(x-goal_x) < .5 and math.fabs(y-goal_y) < .5:
         goalReached = True
      else:
         self.robot.move(0.2, cmd)
      
      if goalReached:
         i = i+1
      
      #If final goal reached, stop robot  
      if i == 7:
         self.robot.move(0, 0)

def INIT(engine):  
   return Practica('Practica', engine)  

  
