from pyrobot.simulators.pysim import *
 
def INIT():
    # (width, height), (offset x, offset y), scale:
    sim = TkSimulator((446,491),(21,451),80.517190)
    # x1, y1, x2, y2 in meters:
    sim.addBox(0, 0, 5, 5)
    sim.addLight(4.5, 4.5, 0.1, "yellow")
    sim.addBox(1, 0, 1, 2)
    sim.addBox(2, 0, 2, 1)
    sim.addBox(2, 2, 2, 3)
    sim.addBox(3, 2, 3, 4)
    sim.addBox(4, 1, 4, 2)
    sim.addBox(4, 3, 4, 5)
 
    sim.addBox(3, 1, 4, 1)
    sim.addBox(4, 2, 5, 2)
    sim.addBox(0, 3, 2, 3)
    sim.addBox(3, 3, 4, 3)
    sim.addBox(1, 4, 3, 4)
    # port, name, x, y, th, bounding Xs, bounding Ys, color
    # (optional TK color name):
    sim.addRobot(60000, TkPioneer("RedPioneer",
                                  .5, 2.2, 0.00,
                                  ((.225, .225, -.225, -.225),
                                   (.175, -.175, -.175, .175))))
    # add some sensors:
    sim.robots[0].addDevice(PioneerFrontSonars()) # for 8 front sonar
    return sim
