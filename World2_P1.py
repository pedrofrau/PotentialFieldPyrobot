''''World 1'''
from pyrobot.simulators.pysim import *

def INIT():
    # (width, height), (offset x, offset y), scale:
    sim = TkSimulator((1020,820),(10,810),100)
    '''Here starts all the obstacle declaration'''
    # x1, y1, x2, y2 in meters:
    #Outside limits
    sim.addBox(0, 0, 10, 8)
    
    #Goal
    sim.addLight(9, 7, 0.1, "yellow")
    
    #Walls
    sim.addBox(2.5, 0, 2.6, 3, "black", wallcolor="black")
    sim.addBox(0, 5, 6, 5.1, "black", wallcolor="black")
    sim.addBox(5.9, 3, 6, 5, "black", wallcolor="black")
    sim.addBox(6, 3, 7, 4, "red", wallcolor="red")
    sim.addBox(8, 6, 10, 6.1, "black", wallcolor="black")

	
    # port, name, x, y, th, bounding Xs, bounding Ys, color
    # (optional TK color name):
    sim.addRobot(60000, TkPioneer("RedPioneer",
                                  1, 1, 0.00,
                                  ((.225, .225, -.225, -.225),
                                   (.175, -.175, -.175, .175))))
    #Sensors
    sim.robots[0].addDevice(PioneerFrontSonars()) # for full 360 sonar
    
    return sim
