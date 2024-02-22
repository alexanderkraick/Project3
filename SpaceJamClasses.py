from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from direct.task import Task

class Planet(ShowBase):
    
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
        
        self.Planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet1.reparentTo(self.render)
        self.Planet1.setPos(2000, 2000, 500)
        self.Planet1.setScale(10)
        self.tex = self.loader.loadTexture("./Assets/Planets/Earth.jpg")
        self.Planet1.setTexture(self.tex, 1)
        
        self.Planet2 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet2.reparentTo(self.render)
        self.Planet2.setPos(2000, 2000, 500)
        self.Planet2.setScale(10)
        self.tex = self.loader.loadTexture("./Assets/Planets/Jupiter.jpg")
        self.Planet2.setTexture(self.tex, 1)
        
        self.Planet3 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet3.reparentTo(self.render)
        self.Planet3.setPos(2000, 2000, 500)
        self.Planet3.setScale(10)
        self.tex = self.loader.loadTexture("./Assets/Planets/Mars.jpg")
        self.Planet3.setTexture(self.tex, 1)
        
        self.Planet4 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet4.reparentTo(self.render)
        self.Planet4.setPos(2000, 2000, 500)
        self.Planet4.setScale(10)
        self.tex = self.loader.loadTexture("./Assets/Planets/Moon.jpg")
        self.Planet4.setTexture(self.tex, 1)
        
        self.Planet5 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet5.reparentTo(self.render)
        self.Planet5.setPos(2000, 2000, 500)
        self.Planet5.setScale(10)
        self.tex = self.loader.loadTexture("./Assets/Planets/Pluto.jpg")
        self.Planet5.setTexture(self.tex, 1)
        
        self.Planet6 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet6.reparentTo(self.render)
        self.Planet6.setPos(2000, 2000, 500)
        self.Planet6.setScale(10)
        self.tex = self.loader.loadTexture("./Assets/Planets/Venus.jpg")
        self.Planet6.setTexture(self.tex, 1)
        
class Player(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
        
        self.Spaceship = self.loader.loadModel("./Assets/Spaceship/theBorg.x")
        self.Spaceship.reparentTo(self.render)
        self.Spaceship.setPos(2000, 2000, 500)
        self.Spaceship.setScale(10)
        self.tex = self.loader.loadTexture("./Assets/Spaceship/theBorg.jpg")
        self.Spaceship.setTexture(self.tex, 1)
        
    def Thrust(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyThrust, 'forward-thrust')
        else:
            self.taskManager.remove('forward-thrust')
            
    def ApplyThrust(self, task):
        rate = 5
        trajectory = self.render.getRelativeVector(self.modelNode, Vec3.forward())
        trajectory.normalize()
        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)
        return Task.cont
    
    def SetKeyBindings(self):
        self.accept('space', self.Thrust, [1])
        self.accept('space-up', self.Thrust, [0])
        
    def LeftTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyLeftTurn, 'left-turn')
        else:
            self.taskManager.remove('left-turn')
            
    def ApplyLeftTurn(self, task):
        rate = .5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont
    
    def SetKeyBindings(self):
        self.accept('a', self.LeftTurn, [1])
        self.accept('a-up', self.LeftTurn, [0])
        
    def RightTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyRightTurn, 'right-turn')
        else:
            self.taskManager.remove('right-turn')
            
    def ApplyRightTurn(self, task):
        rate = .5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont
    
    def SetKeyBindings(self):
        self.accept('a', self.RightTurn, [1])
        self.accept('a-up', self.RightTurn, [0])
        
    def LookUp(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyLookUp, 'up-turn')
        else:
            self.taskManager.remove('up-turn')
            
    def ApplyLookUp(self, task):
        rate = .5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont
    
    def SetKeyBindings(self):
        self.accept('w', self.LookUp, [1])
        self.accept('w-up', self.LookUp, [0])
        
    def LookDown(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyLookDown, 'down-turn')
        else:
            self.taskManager.remove('down-turn')
            
    def ApplyLookDown(self, task):
        rate = .5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont
    
    def SetKeyBindings(self):
        self.accept('s', self.LookDown, [1])
        self.accept('s-up', self.LookDown, [0])
        
    def LeftRoll(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyLeftRoll, 'left-roll')
        else:
            self.taskManager.remove('left-roll')
            
    def ApplyLeftRoll(self, task):
        rate = .5
        self.modelNode.setR(self.modelNode.getR() + rate)
        return Task.cont
    
    def SetKeyBindings(self):
        self.accept('q', self.LeftRoll, [1])
        self.accept('q-up', self.LeftRoll, [0])
        
    def RightRoll(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyRightRoll, 'right-roll')
        else:
            self.taskManager.remove('right-roll')
            
    def ApplyRightRoll(self, task):
        rate = .5
        self.modelNode.setR(self.modelNode.getR() + rate)
        return Task.cont
    
    def SetKeyBindings(self):
        self.accept('e', self.RightRoll, [1])
        self.accept('e-up', self.RightRoll, [0])
        
class Universe(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
        
        self.Universe = self.loader.loadModel("./Assets/Universe/Universe.x")
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)
        self.tex = self.loader.loadTexture("./Assets/Universe/space-galaxy.jpg")
        self.Universe.setTexture(self.tex, 1)
        
class Drone(ShowBase):
    droneCount = 0
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
        
        self.DroneDefender = self.loader.loadModel("./Assets/DroneDefender/DroneDefender.x")
        self.DroneDefender.reparentTo(self.render)
        self.DroneDefender.setScale(15000)
        self.tex = self.loader.loadTexture("./Assets/DroneDefender/DroneDefender.obj")
        self.DroneDefender.setTexture(self.tex, 1)