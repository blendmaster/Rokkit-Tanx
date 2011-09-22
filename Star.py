from PhysicsObject import *
import random

STAR1 = pygame.image.load("star1.png")
STAR2 = pygame.image.load("star2.png")
STAR3 = pygame.image.load("star3.png")
STAR4 = pygame.image.load("star4.png")
STAR5 = pygame.image.load("star5.png")
STAR6 = pygame.image.load("star6.png")
STAR7 = pygame.image.load("star7.png")
STAR8 = pygame.image.load("star8.png")
STAR9 = pygame.image.load("star9.png")

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768

class Star:
    """pretty"""
    def __init__(self,x,y,number):
        self.x = float(x)
        self.y = float(y)
        
        divide = 2
        
        if number == 1: self.image = STAR1
        elif number == 2: self.image = STAR2
        elif number == 3: self.image = STAR3
        elif number == 4: self.image = STAR4
        elif number == 5: self.image = STAR5
        elif number == 6: self.image = STAR6
        elif number == 7: self.image = STAR7
        elif number == 8: self.image = STAR8
        elif number == 9: self.image = STAR9
        else:
            self.image = None
            self.size = random.randint(1,5)
            self.color = (random.randint(200,255),random.randint(200,255),random.randint(200,255))
            divide = 15
            
            #draw a dot
        
        # how fast the star moves in relation to the playa
        self.deltamod = random.random()/divide
        
        if self.image:
            #scale once
            self.image = pygame.transform.scale(self.image,(int(self.image.get_rect().width*self.deltamod*3),int(self.image.get_rect().height*self.deltamod*3)))
            self.image_rect = self.image.get_rect()
            self.image_rect.center = (self.x,self.y)
            
        
    def draw(self,win):
        if self.image:
            win.blit(self.image,self.image_rect)
        else:
            #draw a small circle
            pygame.draw.ellipse(win,self.color,pygame.Rect(self.x,self.y,self.size,self.size))
            
    def move(self,deltay):
        self.y = self.y - deltay*self.deltamod
        
        #this keeps things about on the screen
        # in a looping (ruupu) fashion, deshou?
        if self.y > WINDOW_HEIGHT*1.5: # its off the bottom
            self.y = -WINDOW_HEIGHT*1.5 # move up to the top
        if self.y < -WINDOW_HEIGHT*1.5: # same for too high, though this shouldn't happen too much
            self.y = WINDOW_HEIGHT*1.5
        
        if self.image:
            self.image_rect.centery = self.y