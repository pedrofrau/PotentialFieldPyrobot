from pyrobot.simulators.pysim import *
 
def INIT():
    # (width, height), (offset x, offset y), scale:
    sim = TkSimulator((852,491),(21,451),80.517190)
    sim.addLight(8, 4, 0.1, "yellow")
    # x1, y1, x2, y2 in meters:
    sim.addBox(0, 0, 10, 5)
    sim.addBox(2, 0,  2, 1)
    sim.addBox(2, 2,  2, 4)
    sim.addBox(3, 1,  3, 5)
    sim.addBox(6, 1,  6, 2)
    sim.addBox(6, 3,  6, 5)
    sim.addBox(7, 1,  7, 3)
    sim.addBox(7, 4,  7, 5)
    sim.addBox(9, 2,  9, 5)
 
    sim.addBox(0, 2,  2, 2)
    sim.addBox(3, 1,  6, 1)
    sim.addBox(7, 1,  9, 1)
 
    sim.addBox(0.8, 2.8, 1.2, 4.2)
    sim.addBox(4.5, 1.5, 5.0, 2)
    sim.addBox(3.8, 3.5, 5.8, 4)
    sim.addBox(7.5, 1.5, 8.0, 2)
    sim.addBox(8.5, 2.5, 9.0, 4.5)
 
    # port, name, x, y, th, bounding Xs, bounding Ys, color
    # (optional TK color name):
    sim.addRobot(60000, TkPioneer("RedPioneer",
                                  .5, .5, 0.00,
                                  ((.225, .225, -.225, -.225),
                                   (.175, -.175, -.175, .175))))
    # add some sensors:
    sim.robots[0].addDevice(PioneerFrontSonars()) # for 8 front sonar
    return sim
