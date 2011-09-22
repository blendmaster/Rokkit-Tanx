import pygame
from pygame.locals import *
pygame.init()
pygame.font.init()
from Player import *
from Platform import *
from Star import *
import random

# CAUTION CHANGE THESE IN THE STAR CLASS TOO
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768

FPS = 40

SIDE_DAMPENING = .90

# how far you can move the screen down before you fall off
SCROLL_DOWN_PADDING = 100

SCROLL_ACCELERATION = .005

NUM_PLATFORMS = 10

SMALLFONT = pygame.font.Font(None, 18)
BIGFONT = pygame.font.Font(None,50)

BOING = pygame.mixer.Sound("boing.wav")
OMGWTFBBQ = pygame.mixer.Sound("OHMYGOD.wav")
pygame.mixer.music.load("steven.wav")


class RokkitTanx:
    """ 
    ignore all that about networking, this is just 1 player FOOLS!
    """
    def __init__(self,players):
        self.window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),0,32)
        pygame.display.set_caption("Rokkit Tanx")
        
        self.players = players
        
        
        if len(self.players) == 2:
            NUM_PLATFORMS = 15
            SCROLL_ACCELERATION = .008
        
        
        
        
        
        self.isRunning = True
        
        #let's do this super manually
        self.platforms = [
#                     Platform(0,20,20,460,10),
#                     Platform(480,20,20,460,10),
#                     Platform(0,480,500,20,10),
#                     Platform(100,150,300,50,20),
#                     Platform(0,WINDOW_HEIGHT*3/4,WINDOW_WIDTH,500,0)
                     ]
        
#        for i in range(NUM_PLATFORMS):
#            self.platforms.append(Platform(
#                                           random.randint(0,WINDOW_WIDTH-200),
#                                           -WINDOW_HEIGHT+i*(WINDOW_HEIGHT*3/(NUM_PLATFORMS-1)),
#                                           random.randint(150,WINDOW_WIDTH/2),
#                                           random.randint(1,5)*10))
        
        # how abouts we draw some stars that move down
        # that'll look cool, he said
        # that'll be easy to program, HE SAID
        #AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
        
        self.stars = []
        for i in range(15):
            self.stars.append(Star(random.randint(0,WINDOW_WIDTH),random.randint(-WINDOW_HEIGHT*1.5,WINDOW_HEIGHT*1.5),random.randint(1,9)))
        for i in range(1000):
            self.stars.append(Star(random.randint(0,WINDOW_WIDTH),random.randint(-WINDOW_HEIGHT*1.5,WINDOW_HEIGHT*1.5),13))
            
                
        self.scrollspeed = 1.0
        
        self.bg_image = pygame.Surface((WINDOW_WIDTH,WINDOW_HEIGHT),0,32)
        self.bg_image.fill([0,0,0])
        
    def processEvents(self,events):
        for event in events:
                if event.type == QUIT:
                    exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.players[0].upPressed = True
                    elif event.key == K_LEFT:
                        self.players[0].leftPressed = True
                    elif event.key == K_RIGHT:
                        self.players[0].rightPressed = True
                    elif event.key == K_DOWN:
                        self.players[0].downPressed = True
                        
                    if len(self.players)==2:    
                        if event.key == K_w:
                            self.players[1].upPressed = True
                        elif event.key == K_a:
                            self.players[1].leftPressed = True
                        elif event.key == K_d:
                            self.players[1].rightPressed = True
                        elif event.key == K_s:
                            self.players[1].downPressed = True
                    
                     
                elif event.type == KEYUP:
                    if event.key == K_UP:
                        self.players[0].upPressed = False
                    elif event.key == K_LEFT:
                        self.players[0].leftPressed = False
                    elif event.key == K_RIGHT:
                        self.players[0].rightPressed = False
                    elif event.key == K_DOWN:
                        self.players[0].downPressed = False
                        
                    if len(self.players)==2:    
                        if event.key == K_w:
                            self.players[1].upPressed = False
                        elif event.key == K_a:
                            self.players[1].leftPressed = False
                        elif event.key == K_d:
                            self.players[1].rightPressed = False
                        elif event.key == K_s:
                            self.players[1].downPressed = False
    
    def movePlayers(self):
        #mod players       
        for i in self.players:
            if i.isDead: continue   
            stuff = i.move(Vector(0,0),self.platforms+self.players)
            #Score handling goes here
            for o in stuff:
                    #nao scoring?
                    # STUPID STUPID HACK
                    if i.multiplier < 1:
                        i.score += o.bouncemod*100
                    else:
                        i.score += o.bouncemod*(i.multiplier-1)*100
                    
                    o.timesToJump -= 1
                    if o.timesToJump < 1:
                        self.platforms.remove(o)
                        
                    #I assume this will only play once
                    BOING.play()
                        
                        
        #this constrains the x position to inside the window
        for i in self.players:
            if i.isDead: continue  
            if i.left < 0:
                i.setX(0)
                i.velocity.x = -i.velocity.x*SIDE_DAMPENING
                BOING.play()
            if i.right > WINDOW_WIDTH:
                i.setX(WINDOW_WIDTH-i.width)
                i.velocity.x = -i.velocity.x*SIDE_DAMPENING
                BOING.play()
            if i.top < 0 and not (len(self.players) == 1 or (self.players[0].isDead and not self.players[1].isDead ) or (self.players[0].isDead and not self.players[1].isDead )):
                #keep player on top
                i.setY(0)
                #no velocity change
                
            if i.top > WINDOW_HEIGHT:
            #   i.setY(0)
                i.deathCounter += 1.0/FPS
                i.isDying = True
                if i.deathCounter > 3:
                    i.isDead = True
                    #self.isRunning = False
            else:
                i.deathCounter = 0
                i.isDying = False
                    
        #Game over testing
        lolololol = True
        for i in self.players:
            if not i.isDead: lolololol = False
        #LOOK AT MY ADVANCED CODING
        # I ARE TEH LEET
        self.isRunning = not lolololol
                  
    def moveScreen(self):
        
        #YAY THIS IS TERRIBLE HACK
        
        #one playar
        if len(self.players) == 1 or (self.players[0].isDead and not self.players[1].isDead ) or (not self.players[0].isDead and self.players[1].isDead ):
            #I HAVE A BETTER IDEA
            #This keeps the the highest player roughly in the middle of the screen
            highest = 0
            
            #I hope this keeps player 2 if p1 is dead
            highestplayer = self.players[0]
            for i in self.players:
                if i.isDead: continue
                deltay = (i.y - WINDOW_HEIGHT*2/3)
                if deltay < highest:
                    highest = deltay
                    highestplayer = i
                
            deltay = highest
            #and an even _BETTER_ Idea
            #don't scroll the camera if they move down
            if deltay < SCROLL_DOWN_PADDING:
                deltay = deltay * abs((highestplayer.y - WINDOW_HEIGHT*2/3)/(WINDOW_HEIGHT))
                deltay -= self.scrollspeed
            #autoscroll
            else: 
                deltay = -self.scrollspeed
        else:
            deltay = -self.scrollspeed        
        
        for i in self.players:
            if i.isDead: continue  
            i.setY(i.y-deltay)
            
            #this is very hacky and moves everything but the player and holds the player at the middle of the screen
            i.prevCenterY = i.prevCenterY - deltay
            
        #move starfield
        for i in self.stars:
            i.move(deltay)
        for i in self.platforms:
            i.setY(i.y - deltay)
    
    def changePlatforms(self):
        #cocurrent list modification is bad
        tempPlatforms = []
        for i in self.platforms:
            #since we're looping through the platforms anyway
            #This removes stupid platforms way beneath the screen
            if i.y < WINDOW_HEIGHT*3: tempPlatforms.append(i)
            ##this loops em like stars
            #if i.y > WINDOW_HEIGHT*2: i.setY(-WINDOW_HEIGHT*2)
            #else: print "removing "+str(i)
                      
        self.platforms = tempPlatforms
        
        #if len(self.platforms) < NUM_PLATFORMS:
        for i in range(NUM_PLATFORMS-len(self.platforms)):
                self.platforms.append(Platform(
                                               random.randint(0,WINDOW_WIDTH),
                                               -WINDOW_HEIGHT*2,
                                               random.randint(150,WINDOW_WIDTH/2),
                                               random.randint(1,5)*10))
                
        self.scrollspeed += SCROLL_ACCELERATION
     
    def draw(self):
        #this is michaels, and it makes the screen blury
        mags = 0
        for i in self.players:
            if i.isDead: continue
            if i.velocity.getMagnitude() > mags:
                mags = i.velocity.getMagnitude()
        #mags = [player.velocity.getMagnitude() for player in self.players]
        alf = max(50,255-mags*2)
        #print alf
        self.bg_image.set_alpha(alf)
        self.window.blit(self.bg_image,(0,0))
   
        #stars
        for i in self.stars:
            i.draw(self.window)
        for i in self.platforms:
            i.draw(self.window)
        for i in self.players:
            i.draw(self.window)
        
        if not self.players[0].isDead:
            color = (max(0,min(255,255-int((self.players[0].fuel/MAXFUEL)*255))),max(0,min(255,int((self.players[0].fuel/MAXFUEL)*255))),0)
            #print color
            pygame.draw.rect(self.window, color, pygame.Rect(0,0,WINDOW_WIDTH*self.players[0].fuel/MAXFUEL,10))
    
    
            text = SMALLFONT.render("P1 Score: "+str(self.players[0].score), True, (255,255, 255))
            textRect = text.get_rect()
            textRect.topleft = (10,30)
            self.window.blit(text,textRect)
            
            text = SMALLFONT.render("P1 Combo: "+str(self.players[0].multiplier)+"X", True, (255,255, 0))
            textRect = text.get_rect()
            textRect.topleft = (10,55)
            self.window.blit(text,textRect)
            
            if self.players[0].isDying:
                text = BIGFONT.render("P1 OH NOES: %.3f" % (3 - self.players[0].deathCounter), True, (255,255, 0))
                textRect = text.get_rect()
                textRect.topleft = (40,100)
                self.window.blit(text,textRect)
                
                
        if len(self.players) == 2 and not self.players[1].isDead:
            color = (max(0,min(255,255-int((self.players[1].fuel/MAXFUEL)*255))),max(0,min(255,int((self.players[1].fuel/MAXFUEL)*255))),0)
            #print color
            pygame.draw.rect(self.window, color, pygame.Rect(0,WINDOW_HEIGHT-10,WINDOW_WIDTH*self.players[1].fuel/MAXFUEL,10))
    
    
            text = SMALLFONT.render("P2 Score: "+str(self.players[1].score), True, (255,255, 255))
            textRect = text.get_rect()
            textRect.topleft = (10,WINDOW_HEIGHT-30)
            self.window.blit(text,textRect)
            
            text = SMALLFONT.render("P2 Combo: "+str(self.players[1].multiplier)+"X", True, (255,255, 0))
            textRect = text.get_rect()
            textRect.topleft = (10,WINDOW_HEIGHT-55)
            self.window.blit(text,textRect)
            
            if self.players[1].isDying:
                text = BIGFONT.render("P2 OH NOES: %.3f" % (3 - self.players[1].deathCounter), True, (255,255, 0))
                textRect = text.get_rect()
                textRect.topleft = (40,WINDOW_HEIGHT-100)
                self.window.blit(text,textRect)
                
    def start(self):
        #This sucks in 2 player mode so i remove it
        
        if not len(self.players) == 2:
            #This is the 5 second leadup
            OMGWTFBBQ.play()
            #this adds an upward boost so you don't die if you don't hold up
            
            for i in self.players:
                i.velocity = Vector(0, 100)
            
            counter = float(4.0*FPS)
            while counter > 0:
                counter -=1
                self.processEvents(pygame.event.get())
                self.movePlayers()
                #infinite fuel during warning
                for i in self.players:
                    i.fuel = MAXFUEL
                self.moveScreen()
                
                
                self.draw()
                
                text = BIGFONT.render("WARNING GAME START IN: %.3f" % (counter/FPS), True, (255,0, 0))
                textRect = text.get_rect()
                textRect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
                self.window.blit(text,textRect)
                
                pygame.display.flip() 
                
                pygame.time.Clock().tick(FPS)
        
        for i in range(NUM_PLATFORMS):
            self.platforms.append(Platform(
                                           random.randint(0,WINDOW_WIDTH-200),
                                           -WINDOW_HEIGHT*2+i*(WINDOW_HEIGHT*5/(NUM_PLATFORMS)),
                                           random.randint(150,WINDOW_WIDTH/2),
                                           random.randint(1,5)*10))
        
        
        pygame.mixer.music.play(-1)
        while self.isRunning:
            #events
            self.processEvents(pygame.event.get())
            #mod players       
            self.movePlayers()
            
            self.moveScreen()
            
            self.changePlatforms()
            
            self.draw()
            
            pygame.display.flip() 
            pygame.time.Clock().tick(FPS)

        #gameover
        #clear screen
        self.isGameOver = True
        while self.isGameOver:
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    exit()
                if event.type == KEYUP and event.key == K_ESCAPE:
                    exit()
                if event.type == MOUSEBUTTONUP:
                    exit()    
            
            self.window.fill((0,0,0))
            gameover = pygame.image.load("Game_Over.png")
            self.window.blit(gameover,gameover.get_rect())
            #text = BIGFONT.render("A WINNER IS NOT YOU...", True, (255,255, 255))
            #textRect = text.get_rect()
            #textRect.center = self.window.get_rect().center
            #self.window.blit(text,textRect)
            text = BIGFONT.render("P1 SCORE: "+str(self.players[0].score), True, (255,255, 255))
            textRect = text.get_rect()
            textRect.center = self.window.get_rect().center
            textRect.centery = textRect.centery + 300
            self.window.blit(text,textRect)
            if len(self.players) == 2:
                text = BIGFONT.render("P2 SCORE: "+str(self.players[1].score), True, (255,255, 255))
                textRect = text.get_rect()
                textRect.center = self.window.get_rect().center
                textRect.centery = textRect.centery + 350
                self.window.blit(text,textRect)
            
            pygame.display.flip()
        
                            
#dammit why didn't i see that coming
if __name__ == "__main__":
    game = RokkitTanx(
                      [Player(WINDOW_WIDTH*3/4,WINDOW_HEIGHT*1/4,
                             pygame.image.load("rgirl.png"),
                             pygame.image.load("rgirlfly.png"),
                             pygame.image.load("rgirlfly2.png"),
                            Vector(0,10))
#                     ,Player(WINDOW_WIDTH*1/4,WINDOW_HEIGHT*1/4,
#                             pygame.image.load("gguy.png"),
#                             pygame.image.load("gguyfly.png"),
#                             pygame.image.load("gguyfly2.png"),
#                            Vector(0,10))
                      ]
                    )
    game.start()
