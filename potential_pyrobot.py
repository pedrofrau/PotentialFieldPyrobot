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
   
   def step(self):
      #Robot goal declaration
      '''World1_P1'''
      goal_x = 9.0
      goal_y = 1.0
      '''World2_P1'''
      #goal_x = 9.0
      #goal_y = 7.0
      '''prac2010a'''
      #goal_x = 8.0
      #goal_y = 4.0
      '''prac2010b'''
      #goal_x = 4.5
      #goal_y = 4.5
      
      #Set up for variables and constants
      speed = .05
      maxSpeed = .1
      maxAcc = .5
      maxTurn = 1
      k = 8 #charge decay constant
      positive_charge = 30000
      negative_charge = 30000
      minPositive = 0.5
      
      #Reading the sonar sensors
      front = min([s.distance() for s in self.robot.range["front"]])#Two frontal (3, 4)
      left_f = min([s.distance() for s in self.robot.range["front-left"]])#Left frontal (1, 2, 3)
      right_f = min([s.distance() for s in self.robot.range["front-right"]])#Right frontal (4, 5, 6)
      left = min([s.distance() for s in self.robot.range["left-front"]])#Left (0)
      right = min([s.distance() for s in self.robot.range["right-front"]])#Right (7)
	  back_right = min([s.distance() for s in self.robot.range["back-right"]])#Left back (12, 13, 14)
      back_left = min([s.distance() for s in self.robot.range["back-left"]])#Righ back (9, 10, 11)
      back = min([s.distance() for s in self.robot.range["back"]])#Two back (11, 12)
      
      #Getting the robot simulated position (x, y) and orientation angle (th)     
      x = self.robot.simulation[0].getPose(0)[0]
      y = self.robot.simulation[0].getPose(0)[1]
      th = self.robot.simulation[0].getPose(0)[2]
      
      #Getting the orientation to the goal      
      phi = math.atan2(goal_y-y, goal_x-x) - math.pi/2
      cmd = adjust(phi) - adjust(th)
      
      #Getting the distance to the goal
      distanceGoal = math.sqrt((x - goal_x)**2 + (y - goal_y)**2)
      
      #Calculating the potentials
      	#Repulsive
      '''We need to calculate the distance from the obstacles for each direction (i.e. front, diagonals and sides)
      and calculate the charge applied to the robot from each one of those directions'''
      repulsivePotential_x = ((1.0/front)**k) * math.sin(cmd) + ((1.0/left)**k) * \
      math.sin(cmd + math.pi/2) + ((1.0/right)**k) * math.sin(cmd - math.pi/2) + \
      ((1.0/left_f)**k) * math.sin(cmd + math.pi/4) + ((1.0/right_f)**k) * \
      math.sin(cmd - math.pi/4) + ((1.0/back_left)**k) * math.sin(cmd + 3*math.pi/4) + \
      ((1.0/back_right)**k) * math.sin(cmd - 3*math.pi/4) + ((1.0/back)**k) * math.sin(cmd + math.pi)
      repulsivePotential_y = ((1.0/front)**k) * math.cos(cmd) + ((1.0/left)**k) * \
      math.cos(cmd + math.pi/2) + ((1.0/right)**k) * math.cos(cmd - math.pi/2) + \
      ((1.0/left_f)**k) * math.cos(cmd + math.pi/4) + ((1.0/right_f)**k) * \
      math.cos(cmd - math.pi/4) + ((1.0/back_left)**k) * math.cos(cmd + 3*math.pi/4) + \
      ((1.0/back_right)**k) * math.cos(cmd - 3*math.pi/4) + ((1.0/back)**k) * math.cos(cmd + math.pi)
	  
      	#Attractive
      attractivePotential_x = max(((1.0/distanceGoal)**k) * positive_charge, minPositive) * \
      math.sin(phi)
      attractivePotential_y = max(((1.0/distanceGoal)**k) * positive_charge, minPositive) * \
      math.cos(phi)
      	#Total
      totalPotential_x = attractivePotential_x - repulsivePotential_x * negative_charge
      totalPotential_y = attractivePotential_y - repulsivePotential_y * negative_charge


      #Steering of the robot depeding on the potential value
      turn = math.atan2(speed * math.sin(cmd) + totalPotential_x, speed * math.cos(cmd) + \
      totalPotential_y) - cmd
      while turn > math.pi:
         turn = turn - math.pi
      while turn < -math.pi:
         turn = turn + math.pi
         
      turn = min(maxTurn, turn)
      turn = max(-maxTurn, turn)
      cmd = cmd + turn
      
      new_speed = math.sqrt(speed * (math.sin(cmd) + totalPotential_x)**2 + \
      speed*(math.cos(cmd) + totalPotential_y)**2)
      new_speed = min(speed + maxAcc, new_speed)
      speed = max(speed - maxAcc, new_speed)
      speed = min(speed, maxSpeed)
      speed = max(speed, 0)
      
      #Moving conditions
      if math.fabs(x-goal_x) < .5 and math.fabs(y-goal_y) < .5:#Stop if near goal
         self.robot.move(0, 0)
      else:
         self.robot.move(speed, cmd)#Move depending on obtained speed and direction
         
def INIT(engine):  
   return Practica('Practica', engine)
      
		


  
