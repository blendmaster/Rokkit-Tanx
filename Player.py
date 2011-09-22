from PhysicsObject import *
from Platform import *
import random

#FIREDOWN  = pygame.image.load("C:\\Documents and Settings\\catapult\\workspace\\Rocket Tanks\\src\\firedown.png")
#FIREUP    = pygame.image.load("C:\\Documents and Settings\\catapult\\workspace\\Rocket Tanks\\src\\fireup.png")
#FIRELEFT  = pygame.image.load("C:\\Documents and Settings\\catapult\\workspace\\Rocket Tanks\\src\\fireleft.png")
#FIRERIGHT = pygame.image.load("C:\\Documents and Settings\\catapult\\workspace\\Rocket Tanks\\src\\fireright.png")

WIDTH = 50
HEIGHT = 50
MASS = 10


UP = Vector(0,1.5)
LEFT = Vector(-2,0)
RIGHT = Vector(2,0)
DOWN = Vector(0,-1)

MAXFUEL = 150
UPFUEL = 2
OTHERFUEL = .75

class Player(PhysicsCircle):
    
    def __init__(self,x,y,image,flyimage,flyimage2,velocity=Vector(0,0)):
        PhysicsCircle.__init__(self, x, y, WIDTH, HEIGHT, MASS, velocity, pygame.Color('red'))
        self.score = 0
        self.image = image
        self.flyimage = flyimage
        self.flyimage2 = flyimage2
        self.fuel = MAXFUEL
        
        self.multiplier = 1
        
        self.altitude = 0
        
        #LOLOLOLOLOLOLOLOL
        self.isDead = False
        
        self.isDying = False
        self.deathCounter = 0.0
        
        #self.image_rect = self.image.get_rect()
        #self.image_rect.center = self.center
        
        #self.flyimage_rect = self.flyimage.get_rect()
        #self.flyimage_rect.topleft = self.image_rect.topleft
        
        #sigh moar sprites foar left and right (foar... goddammit)
                
        self.upPressed = False
        self.downPressed = False
        self.leftPressed = False
        self.rightPressed = False
        
        self.stupidAnimation = False
        
        
    def draw(self,win):
        #PhysicsCircle.draw(self,win)
        
        
        
        radians = self.velocity.getDirection()
        #STUPID STUPID COUNTERCLOCKWISE DEGREES
        
        #BUT IT LOOKS SILLY SO I DON"T CARE
        
        angle = degrees(radians)-90
        
        #nvm
        #if they're not moving up and down, they're probably moving flat, so keep em upright
        #if abs(self.velocity.y) < 1: angle = 0
        
        #nvm
        #if self.velocity.getMagnitude() < 1: #let's make em upright if they're not moving a lot
        #    angle = 0
        
        if self.upPressed and self.fuel > 0:
            
            if self.stupidAnimation:
                rotated = pygame.transform.rotate(self.flyimage,angle)
            else:
                rotated = pygame.transform.rotate(self.flyimage2,angle)
            rotatedrect = rotated.get_rect()
            rotatedrect.center = self.center
            
#            win.blit(FIREDOWN,self.hull)
#        if self.downPressed:
#            win.blit(FIREUP,self.hull)
#        if self.leftPressed:
#            win.blit(FIRELEFT,self.hull)
#        if self.rightPressed:
#            win.blit(FIRERIGHT,self.hull)
        else:
            rotated = pygame.transform.rotate(self.image,angle)
            rotatedrect = rotated.get_rect()
            rotatedrect.center = self.center
        win.blit(rotated,rotatedrect)
        
        self.stupidAnimation = not self.stupidAnimation
        
        #debug
        #pygame.draw.ellipse(win, self.color, pygame.Rect(self.prevCenterX-self.width/2,self.prevCenterY-self.height/2,self.width,self.height), 1 )
    
    def setX(self,x):
        PhysicsCircle.setX(self,x)
        #self.image_rect.centerx = self.centerx
        #self.flyimage_rect.topleft = self.image_rect.topleft
        
    def setY(self,y):
        PhysicsCircle.setY(self,y)
        #self.image_rect.centery = self.centery
        #self.flyimage_rect.topleft = self.image_rect.topleft
    
#bleh, this is a bad method
#    def setY(self,y):
#        #this moves everything else to keep this at it's original position
#        deltay = self.y - float(y)
#        self.centery = self.y + self.width/2
#        
#        self.center = (self.centerx,self.centery)
#        
#        self.topleft = (self.x,self.y)
#        self.topright = (self.x+self.width,self.y)
#        self.bottomleft = (self.x,self.y+self.height)
#        self.bottomright = (self.x+self.width,self.y+self.height)
#        
#        self.top = self.y
#        self.bottom = self.y + self.height
#        
#        self.hull.y = self.y
#        self.image_rect.centery = self.centery
#        
#        #moar accurate y position for prevCenterY
#        self.prevCenterY = self.prevCenterY + deltay
#        
#        for o in self.others:
#            o.setY(o.y + deltay)
    
    def applyVelocity(self):    
        "simple: applies the velocity , and updates prevX and Y"
        #this also updates altitude
        self.prevCenterX = self.centerx
        self.prevCenterY = self.centery
        self.setX( self.x + self.velocity.x)
        self.setY( self.y - self.velocity.y)
        self.altitude += self.velocity.y
        #print self.altitude
        
    def move(self, deltaV, others):
        """
        mods velocity and collides against PhysicsObjects in the others list
        """
        if self.fuel > 0:
            if self.leftPressed: 
                self.addVelocity(LEFT)
                self.fuel -= OTHERFUEL
            if self.downPressed: 
                self.addVelocity(DOWN)
                self.fuel -= OTHERFUEL
            if self.rightPressed: 
                self.addVelocity(RIGHT)
                self.fuel -= OTHERFUEL
            if self.upPressed:
                self.addVelocity(UP)
                self.fuel -= UPFUEL
        
        self.fuel += .5
        if self.fuel > MAXFUEL:
            self.fuel = MAXFUEL
        #print self.fuel
        self.addVelocity(deltaV)
        if GRAVITY_ENABLED:
            self.addGravity()
                
        self.applyVelocity()
        
        collidedWith = []
        
        for o in others:
            if o == self: continue
            if self.intersects(o):
                self.uncollide(o)
                if o.isCircle():
                    self.elasticCollision(o)
                else:
                    posRel = self.posRelTo(o)
                    #fuel
                    if posRel ==1:
                        self.fuel += o.bouncemod
                        collidedWith.append(o)
                        self.multiplier += 1
                    elif posRel == 4:
                        self.multiplier = 1
                    o.rectCollision(self)
        #add altitude to score once
        self.score += int(self.altitude/1000)
               
            
        return collidedWith

    