from math import *
from Vector import *

import pygame
from pygame.locals import *

DEBUG_DRAW_HULLS = True
DEBUG_DRAW_VELOCITY = False

GRAVITY_ENABLED = True
GRAVITY = Vector(0.0, -1.0)

ELASTIC_COLLISION_DAMPENING = .95

class PhysicsObject:
    """
    An circle exibiting rigid body non angular velocity physics ( no force ). This is supposed to be an abstract class
    so, you know, don't make any or whatever. kthxbai
    """
    
    def __init__(self,x,y,width,height,mass,velocity=Vector(0,0),color=pygame.Color('blue')):
        self.velocity = velocity # velocity in other words, dx and dy
        self.mass = mass
        
        
        
        #damn rect object doesn't store float values
        self.x = float(x)
        self.y = float(y)
        self.prevCenterX = self.x
        self.prevCenterY = self.y
        self.width = float(width)
        self.height = float(height)
        self.centerx = self.x + self.width/2
        self.centery = self.y + self.height/2
        self.center = (self.centerx,self.centery)
        #moar rect variables made floaty
        self.topleft = (self.x,self.y)
        self.topright = (self.x+self.width,self.y)
        self.bottomleft = (self.x,self.y+self.height)
        self.bottomright = (self.x+self.width,self.y+self.height)
        
        self.top = self.y
        self.bottom = self.y + self.height
        self.left = self.x
        self.right = self.x + self.width
        
        self.hull = pygame.Rect(x,y,width,height) # the collision hull, even though the image
                                                  # overlayed might be different
        self.color = color                                          
    
    def setX(self,x):
        self.x = float(x)
        self.centerx = self.x + self.width/2

        self.center = (self.centerx,self.centery)
        
        self.topleft = (self.x,self.y)
        self.topright = (self.x+self.width,self.y)
        self.bottomleft = (self.x,self.y+self.height)
        self.bottomright = (self.x+self.width,self.y+self.height)
        
        self.left = self.x
        self.right = self.x + self.width
        
        self.hull.x = x
        
        
        
    def setY(self,y):
        self.y = float(y)
        self.centery = self.y + self.width/2
        
        
        self.center = (self.centerx,self.centery)
        
        self.topleft = (self.x,self.y)
        self.topright = (self.x+self.width,self.y)
        self.bottomleft = (self.x,self.y+self.height)
        self.bottomright = (self.x+self.width,self.y+self.height)
        
        self.top = self.y
        self.bottom = self.y + self.height
        
        self.hull.y = y
        
    def intersects(self,o):
        """
        This returns true if the other physics object is too far away from this one
        """
        
        if abs( self.centerx - o.centerx ) > 500 and abs( self.centery - o.centery ) > 500:
            return False
        return True
           
    def posRelTo(self,o): #abstract
        """
        This one is annoying but I also don't know a better way to do this
        It returns an int based on where this object is to the other one. a-like so:
        // above returns 1;
        // left returns 2;
        // right returns 3;
        // bottom returns 4;
        // middle returns 0;
        // weird error returns -1;
        excuse the java comment markers pl0xorz
        """
        return 0 
        
    def uncollide(self,o): pass #abstract
    
    def addVelocity(self,v):
        self.velocity = self.velocity.add(v)
        
    def applyVelocity(self): pass #abstract
        
    def addGravity(self):
        self.velocity = self.velocity.add(GRAVITY)
    
    def counteractGravity(self):
        #this removes the effect of gravity, in case you are on the ground and don't want to keep
        #goin down
        self.velocity = velocity.add(Vector(GRAVITY.x*-1,GRAVITY.y*-1))
    
    def move(self, deltaV, others): return [] # abstract, kind of
    
    def draw(self,win):
        """
        Draws the velocity if needed, which is the thing that all Physics Objects have
        """
        if DEBUG_DRAW_VELOCITY:
            pygame.draw.line(win, pygame.Color('red'), self.center, (int(self.centerx + self.velocity.x*10.0), int(self.centery - self.velocity.y*10.0) ) )
          
    def __str__(self):
        return "PhysicsObject("+str(self.x)+","+str(self.y)+"), velocity("+str(self.velocity)

class PhysicsCircle(PhysicsObject):
    """These move and behave well, like good little 2d circles"""
    
    def __init__(self,x,y,width,height,mass,velocity=Vector(0,0),color=pygame.Color('blue')):
        PhysicsObject.__init__(self,x,y,width,height,mass,velocity,color)
        
    def applyVelocity(self):    
        "simple: applies the velocity , and updates prevX and Y"
        self.prevCenterX = self.centerx
        self.prevCenterY = self.centery
        self.setX( self.x + self.velocity.x)
        self.setY( self.y - self.velocity.y)
        
    def __str__(self):
        return "Circle"+PhysicsObject.__str__(self)
    
    def draw(self,win):
        """
        Draw that. this will probably be overridden to draw an image, but for debugging it draws
        the hull
        """
        
        PhysicsObject.draw(self,win)
        
        if DEBUG_DRAW_HULLS:
            pygame.draw.ellipse(win, self.color, self.hull, 1 )
            
    def elasticCollision(self,o):
        """
        Elastic collision with another object
        This changes the velocity of both objects
        """
        normal = Vector( o.x - self.x, self.y - o.y )
        normal.setVector( normal.getUnitVector() )
        tangent = Vector( -normal.y, normal.x )
        
        m1 = self.mass
        m2 = o.mass
        
        v1n = normal.dotProduct( self.velocity )
        v1t = tangent.dotProduct( self.velocity )
        v2n = normal.dotProduct( o.velocity )
        v2t = tangent.dotProduct( o.velocity )        
        
        v1tPrime = v1t
        v2tPrime = v2t
        
        v1nPrime = (v1n*(m1-m2)+v2n*m2*2)/(m1+m2)
        v2nPrime = (v2n*(m2-m1)+v1n*m1*2)/(m1+m2)
        
        vectorV1nPrime = normal.multiply(v1nPrime)
        vectorV1tPrime = tangent.multiply(v1tPrime)
        vectorV2nPrime = normal.multiply(v2nPrime)
        vectorV2tPrime = tangent.multiply(v2tPrime)
        
        self.velocity = vectorV1nPrime.add(vectorV1tPrime).multiply(ELASTIC_COLLISION_DAMPENING)
        o.velocity = vectorV2nPrime.add(vectorV2tPrime).multiply(ELASTIC_COLLISION_DAMPENING)
    
    def uncollide(self,o):
        """
        moves this object out of the other object
        which prevents collision detection from changing velocity moar than once
        DOESN'T CHANGE VELOCITY
        """
    
        if o.isCircle():
            normal = Vector( o.centerx - self.centerx, self.centery - o.centery )
            distanceToMove = self.width/2.0 + o.width/2.0 - normal.getMagnitude()
            
            normal.setVector( Vector (-normal.x, -normal.y ) )
            normal.setVector( normal.getUnitVector() ) # set's to 1 so we can multiply better
            normal = normal.multiply( distanceToMove ); #gets short vector
            
            self.setX( self.x + normal.x)
            self.setY( self.y - normal.y)
        else:
            posRel = self.posRelTo(o)
            if posRel == 1: self.setY( self.y - ( self.y + self.height - o.y ) )
            elif posRel == 2: self.setX( self.x - ( self.x + self.width - o.x ) )
            elif posRel == 3: self.setX( self.x + ( o.x + o.width - self.x ) )
            elif posRel == 4: self.setY( self.y + ( o.y + o.height - self.y ) )
            else: self.setY( self.y - ( self.y + self.height - o.y ) ) #just move it up
            
    def posRelTo(self,o):
        """
        This one is annoying but I also don't know a better way to do this
        It returns an int based on where this object is to the other one. a-like so:
        // above returns 1;
        // left returns 2;
        // right returns 3;
        // bottom returns 4;
        // middle returns 0;
        // weird error returns -1;
        excuse the java comment markers pl0xorz
        """
        
        #this tests where the PREVIOUS center of self was in relation to
        # object
        
        # a like so
        #  0 1 2
        #  3 x 5
        #  6 7 8
        # it shouldn't ever be 4
        
        # and THEN it checks for sure in spaces 0 2 6 8 for which direction
        # the object was going
        
        
        if o.isCircle():
            centerAngle =  atan2( o.centery - self.centery, self.centerx - o.centerx )/pi
                                               
            if (1.0/4.0) < centerAngle and centerAngle < (3.0/4.0):
                return 1
            if (-1.0/4.0) < centerAngle and centerAngle < (1.0/4.0) :
                return 3;
            if (-3.0/4.0) < centerAngle and centerAngle < (-1.0/4.0) : 
                return 4;
            if (-3.0/4.0) < centerAngle or centerAngle > (3.0/4.0) :
                return 2 
            
        else:
            switchX = 0
            switchY = 0
            
            if o.left > self.prevCenterX:
                #print "left"
                switchX = 0
            elif o.left <= self.prevCenterX and self.prevCenterX <= o.right:
                #print "middle"
                switchX = 1
            else:
                #print "right"
                switchX = 2
        
            if o.top > self.prevCenterY:
                #print "top"
                switchY = 0
            elif o.top <= self.prevCenterY and self.prevCenterY <= o.bottom:
                #print "middle"
                switchY = 1
            else:
                #print "bottom"
                switchY = 2
            
            switch = switchY*3 + switchX
        
            #print str(self) + " is in octant " + str(switch) + " of " + str(o)
        
            if switch == 1: return 1
            elif switch == 3: return 2
            elif switch == 5: return 3
            elif switch == 7: return 4
            elif switch == 0:
                angle = atan2( o.top - self.prevCenterY, self.prevCenterX - o.left )
                if self.velocity.getDirection() <= angle:
                    return 1
                else: return 2
            elif switch == 2:
                angle = atan2( o.top - self.prevCenterY, self.prevCenterX - o.right )
                if self.velocity.getDirection() >= angle:
                    return 1
                else: return 3
            elif switch == 6:
                angle = atan2( o.bottom - self.prevCenterY, self.prevCenterX - o.left )
                if self.velocity.getDirection() >= angle:
                    return 4
                else: return 2
            elif switch == 8:
                angle = atan2( o.bottom - self.prevCenterY, self.prevCenterX - o.right )
                if self.velocity.getDirection() <= angle:
                    return 4
                else: return 3 
            elif switch == 4:
                #let's just assume it came from above
                return 1
            
        
        return -1
        
    def intersects(self,o):
        if PhysicsObject.intersects(self,o):
            if o.isCircle():
                #distance between centers is less than their two radiuses, moveable objects are always circles, hopefully
                return (self.centerx - o.centerx)**2 + (self.centery - o.centery)**2 <= (self.width/2.0+o.width/2.0)**2
            else:
                #sigh, no circle to rect collision, so they'll be some weirdness at the edges of boxen
                return self.hull.colliderect(o.hull) 
        return False
    
    def isCircle(self):
        return True

    
    def move(self, deltaV, others):
        """
        mods velocity and collides against PhysicsObjects in the others list
        """
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
                    o.rectCollision(self)
                collidedWith.append(o)
            
        return collidedWith
        
class PhysicsRect(PhysicsObject):
    """These don't move because since there's no angular velocity, it looks weird"""

    def __init__(self,x,y,width,height,bouncemod,friction,color=pygame.Color('green')):
            PhysicsObject.__init__(self,x,y,width,height,100,Vector(0,0),color)
            self.bouncemod = bouncemod
            self.friction = friction
    
    def isCircle(self):
        return False

    def rectCollision(self,o):
        """
        changes other object's velocity accordingly when
        it collides with this platform
        """
        posRel = o.posRelTo(self)
        
        if posRel == 1: 
            o.velocity.y = -o.velocity.y*self.bouncemod
            o.velocity.x = o.velocity.x*self.friction
        elif posRel == 2: 
            o.velocity.x = -o.velocity.x*self.bouncemod
            o.velocity.y = o.velocity.y*self.friction
        elif posRel == 3: 
            o.velocity.x = -o.velocity.x*self.bouncemod
            o.velocity.y = o.velocity.y*self.friction
        elif posRel == 4: 
            o.velocity.y = -o.velocity.y*self.bouncemod
            o.velocity.x = o.velocity.x*self.friction
        else: 
            o.velocity.y = -o.velocity.y*self.bouncemod #just bounce it up
            o.velocity.x = o.velocity.x*self.friction
    
            
    def __str__(self):
        return "Rect"+PhysicsObject.__str__(self)
    
    def intersects(self,o):
        if PhysicsObject.intersects(self,o):
            return self.hull.colliderect(o.hull)
        return False
    
    def applyVelocity(self):
        "since these shouldn't move, let's apply no velocity"
        pass
    
    def draw(self,win):
        """
        Draw that. this will probably be overridden to draw an image, but for debugging it draws
        the hull
        """
        
        PhysicsObject.draw(self,win)
        
        if DEBUG_DRAW_HULLS:
            pygame.draw.rect(win, self.color, self.hull, 1 )       
    
# testing
def main():
    
    import random
    pygame.init()
    
    window = pygame.display.set_mode((1024,768),0,32)
    pygame.display.set_caption("Physics Test")
    player = PhysicsCircle( 250, 250, 50,50,15 )
    
    things = [player]
    leftPressed = False
    rightPressed = False
    downPressed = False
    upPressed = False
    fuel = 1024.0
    font = pygame.font.Font(None, 15)
    text = font.render('Fuel', True, (255,255, 255))
    textRect = text.get_rect()
    textRect.x = 20
    textRect.y = 0
    
    
    #something clevar to draw new platforms
    firstclick = None
    secondclick = None
    tempsecondclick = None
    
    pewpewpew = pygame.mixer.Sound("lazor.wav")
    
    
    platforms = [PhysicsRect(0,80,80,768-160,.5,.90),
                 PhysicsRect(0,0,1024,80,.5,.90),
                 PhysicsRect(1024-80,80,80,768-160,.5,.90),
                 PhysicsRect(0,768-80,1024,80,.5,.90)
                 #PhysicsRect(1024/2-200,768/2,400,50,.20,.90)
                 ]
    isRunning = True
    while isRunning:
        window.fill(pygame.Color('black'))
        events = pygame.event.get()
        for event in events:
            #if event.type == QUIT:
            #    exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    newDiam = random.randint(10,30)
                    newVector = Vector((event.pos[0] - player.x)/10.0, (player.y - event.pos[1])/10.0)
                    newNormal = newVector.getUnitVector()
                    newCenterx = player.centerx + newNormal.multiply(player.width/2.0 + newDiam/2.0).x
                    newCentery = player.centery - newNormal.multiply(player.width/2.0 + newDiam/2.0).y
                    newX = newCenterx - newDiam/2.0
                    newY = newCentery - newDiam/2.0
                    newThing = PhysicsCircle(newX,newY,newDiam ,newDiam , newDiam/10.0, newVector,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))    
                    things.append(newThing)
                    pewpewpew.play()
                elif event.button == 3:
                    if firstclick == None:
                        firstclick = event.pos
                    else:
                        #clicked two times
                        secondclick = event.pos
                        #no negative rectangles
                        second = False
                        if firstclick[0]>secondclick[0]: 
                            
                            secondclick = None
                            firstclick = None
                            tempsecondclick = None
                            break
                        else: 
                            width = secondclick[0]-firstclick[0]
                        
                        if firstclick[1]>secondclick[1]:
                            secondclick = None
                            firstclick = None
                            tempsecondclick = None
                            break
                        else: 
                            height = secondclick[1]-firstclick[1]
                            
                            platforms.append(PhysicsRect(firstclick[0],firstclick[1],width,height,0,.90))
                        secondclick = None
                        firstclick = None
                        tempsecondclick = None
            
            elif event.type == MOUSEMOTION and firstclick != None:
                #draw temprect where the platform would be named
                tempsecondclick = event.pos
                
                   
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    upPressed = True
                if event.key == K_LEFT:
                    leftPressed = True
                if event.key == K_RIGHT:
                    rightPressed = True
                if event.key == K_DOWN:
                    downPressed = True
                if event.key == K_ESCAPE:
                    isRunning = False
        
            elif event.type == KEYUP:
                if event.key == K_UP:
                    upPressed = False
                if event.key == K_LEFT:
                    leftPressed = False
                if event.key == K_RIGHT:
                    rightPressed = False
                if event.key == K_DOWN:
                    downPressed = False
            
        #move "player"
        if fuel > 0:
            if leftPressed: 
                player.addVelocity(Vector(-1.0,0))
                fuel = fuel - 2 
            if downPressed: 
                player.addVelocity(Vector(0.0,-1.0))
                fuel = fuel - 2 
            if rightPressed: 
                player.addVelocity(Vector(1.0,0.0))
                fuel = fuel - 2 
            if upPressed: 
                player.addVelocity(Vector(0.0,1.5))
                fuel = fuel - 4 
        fuel += .5
              
        for i in things:
            touched = len(i.move(Vector(0,0),things+platforms))
            #print "Collision:" + str(j)
            if( i == player ):
                fuel += touched*5
            i.draw(window)
            
        for i in platforms:
            i.draw(window)
        
        if fuel > 1024: fuel = 1024    
        if fuel > 0:
            if leftPressed: 
                pygame.draw.rect(window, pygame.Color('orange'), pygame.Rect(player.right,player.centery-5,10,10))
            if downPressed: 
                pygame.draw.rect(window, pygame.Color('orange'), pygame.Rect(player.centerx-5,player.top-10,10,10))
            if rightPressed: 
                pygame.draw.rect(window, pygame.Color('orange'), pygame.Rect(player.left-10,player.centery-5,10,10))
            if upPressed: 
                pygame.draw.rect(window, pygame.Color('orange'), pygame.Rect(player.centerx-7,player.bottom,15,15))  
        pygame.draw.rect(window, pygame.Color('orange'), pygame.Rect(0,0,fuel,10))
        
        #draw current click
        if firstclick != None and tempsecondclick != None:
            pygame.draw.rect(window,pygame.Color('firebrick'),pygame.Rect(firstclick,(tempsecondclick[0] - firstclick[0], tempsecondclick[1] - firstclick[1])),1)
        window.blit(text, textRect)
        pygame.display.flip()
        pygame.time.Clock().tick(30)
    pygame.display.quit()
    pygame.quit()
        
            
if __name__ == "__main__":
    main()
        
