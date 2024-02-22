import math, random
from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
import SpaceJamClasses as SpaceJamClasses

def Cloud(radius = 1):
    x = 2 * random.random() - 1
    y = 2 * random.random() - 1
    z = 2 * random.random() - 1
    unitVec = Vec3(x, y, z)
    unitVec.normalize()
    return unitVec * radius

def BaseballSeams(step, numSeams, B, F = 1):
    time = step / float(numSeams) * 2 * math.pi
    
    F4 = 0
    
    R = 1
    
    xxx = math.cos(time) - B * math.cos(3 * time)
    yyy = math.sin(time) + B * math.sin(3 * time)
    zzz = F * math.cos(2 * time) + F4 * math.cos(4 * time)
    
    rrr = math.sqrt(xxx ** 2 + yyy ** 2 + zzz ** 2)
    
    x = R * xxx / rrr
    y = R * yyy / rrr
    z = R * zzz / rrr
    
    return Vec3(x, y, z)

def DrawCircleXYDefense(self):
        self.parent = self.loader.loadModel('./Assets/DroneDefender/DroneDefender.obj')
        self.parent.setScale(0.25)
        a = 0.0
        aInc = 0.2
        R = 50.0

        for i in range(30):
            posVec = (R * math.cos(a), R * math.sin(a), 0)
            self.placeholder = self.render.attachNewNode("Placeholder")
            self.placeholder.setPos(posVec)
            self.placeholder.setColor(255, 0, 0, 1)
            self.parent.instanceTo(self.placeholder)
            a += aInc

def DrawCircleXZDefense(self):
    self.parent = self.loader.loadModel('./Assets/DroneDefender/DroneDefender.obj')
    self.parent.setScale(0.25)
    a = 0.0
    aInc = 0.2
    R = 50.0

    for i in range(30):
        posVec = (R * math.cos(a), 0, R * math.sin(a))
        self.placeholder = self.render.attachNewNode("Placeholder")
        self.placeholder.setPos(posVec)
        self.placeholder.setColor(0, 255, 0, 1)
        self.parent.instanceTo(self.placeholder)
        a += aInc

def DrawCircleYZDefense(self):
    self.parent = self.loader.loadModel('./Assets/DroneDefender/DroneDefender.obj')
    self.parent.setScale(0.25)
    a = 0.0
    aInc = 0.2
    R = 50.0

    for i in range(30):
        posVec = (0, R * math.cos(a), R * math.sin(a))
        self.placeholder = self.render.attachNewNode("Placeholder")
        self.placeholder.setPos(posVec)
        self.placeholder.setColor(0, 0, 255, 1)
        self.parent.instanceTo(self.placeholder)
        a += aInc