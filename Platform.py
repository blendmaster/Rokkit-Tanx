from PhysicsObject import *


FRICTION = .95


#Images
#PANELBleft = pygame.image.load("C:\\Documents and Settings\\catapult\\workspace\\Rocket Tanks\\src\\bpanelleft.png")
PANELBcenter = pygame.image.load("bpanelcenter.png")
#PANELBright = pygame.image.load("C:\\Documents and Settings\\catapult\\workspace\\Rocket Tanks\\src\\bpanelright.png")

#PANELRleft = pygame.image.load("C:\\Documents and Settings\\catapult\\workspace\\Rocket Tanks\\src\\rpanelleft.png")
PANELRcenter = pygame.image.load("rpanelcenter.png")
#PANELRright = pygame.image.load("C:\\Documents and Settings\\catapult\\workspace\\Rocket Tanks\\src\\rpanelright.png")

#PANELGleft = pygame.image.load("C:\\Documents and Settings\\catapult\\workspace\\Rocket Tanks\\src\\gpanelleft.png")
PANELGcenter = pygame.image.load("gpanelcenter.png")
#PANELGright = pygame.image.load("C:\\Documents and Settings\\catapult\\workspace\\Rocket Tanks\\src\\gpanelright.png")

#PANELPleft = pygame.image.load("C:\\Documents and Settings\\catapult\\workspace\\Rocket Tanks\\src\\ppanelleft.png")
PANELPcenter = pygame.image.load("ppanelcenter.png")
#PANELPright = pygame.image.load("C:\\Documents and Settings\\catapult\\workspace\\Rocket Tanks\\src\\ppanelright.png")

#PANELYleft = pygame.image.load("C:\\Documents and Settings\\catapult\\workspace\\Rocket Tanks\\src\\ypanelleft.png")
PANELYcenter = pygame.image.load("ypanelcenter.png")
#PANELYright = pygame.image.load("C:\\Documents and Settings\\catapult\\workspace\\Rocket Tanks\\src\\ypanelright.png")

#PANELOleft = pygame.image.load("C:\\Documents and Settings\\catapult\\workspace\\Rocket Tanks\\src\\opanelleft.png")
PANELOcenter = pygame.image.load("opanelcenter.png")
#PANELOright = pygame.image.load("C:\\Documents and Settings\\catapult\\workspace\\Rocket Tanks\\src\\opanelright.png")

SIDE = pygame.image.load("Sides.PNG")


HEIGHT = 27

#collision on surfaces other than up
OTHER_BOUNCEMOD = 1

class Platform(PhysicsRect):
    """
    Those stupid platforms.
    I think these have a grid x and y as well
    so they can move around the screen maybe?
    """
    
    def __init__(self,x,y,width,bouncemod):
        PhysicsRect.__init__(self,x,y,width,HEIGHT,bouncemod,FRICTION)
        
        self.timesToJump = self.bouncemod / 10
        
        #if self.bouncemod == 0: 
            #self.color = pygame.Color('grey')
        if self.bouncemod == 10: 
            #self.color = pygame.Color('red')
            #self.leftImage = PANELRleft
            self.centerImage = PANELRcenter
            #self.rightImage = PANELRright
        elif self.bouncemod == 20: 
            #self.color = pygame.Color('orange')
            #self.leftImage = PANELOleft
            self.centerImage = PANELOcenter
            #self.rightImage = PANELOright
        elif self.bouncemod == 30: 
            #self.color = pygame.Color('yellow')
            #self.leftImage = PANELYleft
            self.centerImage = PANELYcenter
            #self.rightImage = PANELYright
        elif self.bouncemod == 40: 
            #self.color = pygame.Color('green')
            #self.leftImage = PANELGleft
            self.centerImage = PANELGcenter
            #self.rightImage = PANELGright
        else: #self.bouncemod == 50: 
            #self.color = pygame.Color('firebrick')
            #self.leftImage = PANELBleft
            self.centerImage = PANELBcenter
            #self.rightImage = PANELBright
            
        #makes it the right length
        self.leftImage = SIDE
        self.rightImage = SIDE
        
        self.centerImage = pygame.transform.scale(self.centerImage,(int(self.width),int(self.centerImage.get_rect().height)))
            
        
        #else: 
        #    #self.color = pygame.Color('purple')
        #    self.leftImage = PANELRleft
        #    self.centerImage = PANELRcenter
        #    self.centerImage = PANELRright

        pygame.font.init()
        self.text = pygame.font.Font(None,20).render(str(self.bouncemod)+"00",True,(255,255,255,128))
        self.textRect = self.text.get_rect()
        
    def draw(self,win):

        #pygame.draw.rect(win,self.color,self.hull)
        
        
        #center
        centerrect = self.centerImage.get_rect()
        centerrect.topleft = self.topleft
        win.blit(self.centerImage,centerrect)
        
        #left
        leftrect = self.leftImage.get_rect()
        leftrect.topleft = self.topleft
        win.blit(self.leftImage,leftrect)
        
        #right
        rightrect = self.rightImage.get_rect()
        rightrect.topright = self.topright
        win.blit(self.rightImage,rightrect )
        

        
        self.textRect.center = self.hull.center
        win.blit(self.text,self.textRect)
        
    def rectCollision(self,o):
        """
        changes other object's velocity accordingly when
        it collides with this platform
        """
        posRel = o.posRelTo(self)
        
        #NOTE:
        # this really isn't a modifier to the y velocity, it just changes it to the value
        # for the top surface
        
        if posRel == 1:
            if abs(o.velocity.y) < self.bouncemod:
                o.velocity.y = self.bouncemod
            else:
                o.velocity.y = -o.velocity.y
            o.velocity.x = o.velocity.x*self.friction
        elif posRel == 2: 
            o.velocity.x = -o.velocity.x*OTHER_BOUNCEMOD
            o.velocity.y = o.velocity.y*self.friction
        elif posRel == 3: 
            o.velocity.x = -o.velocity.x*OTHER_BOUNCEMOD
            o.velocity.y = o.velocity.y*self.friction
        elif posRel == 4: 
            #o.velocity.y = -o.velocity.y*OTHER_BOUNCEMOD
            o.velocity.y = 0
            o.velocity.x = o.velocity.x*self.friction
        else: 
            o.velocity.y = -o.velocity.y*self.bouncemod #just bounce it up
            o.velocity.x = o.velocity.x*self.friction
       
   
