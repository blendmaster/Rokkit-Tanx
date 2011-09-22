from PhysicsObject import *
pygame.init()

class Player(PhysicsCircle):
    def __init__(self,x,y,width,height,mass,image,velocity=Vector(0,0)):
        PhysicsCircle.__init__(self,x,y,width,height,mass, velocity)
        self.image = image
        self.image_rect = self.image.get_rect().move(self.centerx,self.centery)
        self.image_rect.center = self.center
        
    def draw(self,win):
        PhysicsCircle.draw(self,win)
        win.blit(self.image,self.image_rect)
        PhysicsCircle.draw(self,win)
        win.blit(self.image,self.image_rect)
        
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
        
        self.image_rect.centerx = self.centerx
        
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
        
        self.image_rect.centery = self.centery
    def isCircle(self):
        return True

if __name__ == "__main__":
    
    import random
    
    window = pygame.display.set_mode((500,500),0,32)
    pygame.display.set_caption("Physics Test")
    player = Player( 250, 250, 50,50,15,pygame.image.load("rgirlfly.png"))
    playera = Player( 150, 150, 50,50,15,pygame.image.load("rgirl.png"))
    
    things = [player]
    leftPressed = False
    rightPressed = False
    downPressed = False
    upPressed = False
    fuel = 500.0
    
    things2 = [playera]
    aPressed = False
    dPressed = False
    sPressed = False
    wPressed = False
    fuel = 500.0
     
    text = pygame.font.Font(None, 15).render('Fuel', True, (255,255, 255))
    textRect = text.get_rect()
    textRect.x = 20
    textRect.y = 0
    
    
    platforms = [PhysicsRect(0,20,20,460,.5,.90),PhysicsRect(0,0,500,20,.5,.90),PhysicsRect(480,20,20,460,.5,.90),PhysicsRect(0,480,500,20,.5,.90),PhysicsRect(100,150,300,50,.5,.90)]
    
    while True:
        window.fill(pygame.Color('black'))
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                newDiam = random.randint(10,30)
                newVector = Vector((event.pos[0] - player.x)/10.0, (player.y - event.pos[1])/10.0)
                newNormal = newVector.getUnitVector()
                newCenterx = player.centerx + newNormal.multiply(player.width/2.0 + newDiam/2.0).x
                newCentery = player.centery - newNormal.multiply(player.width/2.0 + newDiam/2.0).y
                newX = newCenterx - newDiam/2.0
                newY = newCentery - newDiam/2.0
                newThing = PhysicsCircle(newX,newY,newDiam ,newDiam , newDiam/10.0, newVector,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))    
                things.append(newThing)
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    upPressed = True
                if event.key == K_LEFT:
                    leftPressed = True
                if event.key == K_RIGHT:
                    rightPressed = True
                if event.key == K_DOWN:
                    downPressed = True
            elif event.type == KEYUP:
                if event.key == K_UP:
                    upPressed = False
                if event.key == K_LEFT:
                    leftPressed = False
                if event.key == K_RIGHT:
                    rightPressed = False
                if event.key == K_DOWN:
                    downPressed = False
                    
            elif event.type == KEYDOWN:
                if event.key == K_W:
                    upPressed = True
                if event.key == K_A:
                    leftPressed = True
                if event.key == K_D:
                    rightPressed = True
                if event.key == K_S:
                    downPressed = True
            elif event.type == KEYUP:
                if event.key == K_W:
                    upPressed = False
                if event.key == K_A:
                    leftPressed = False
                if event.key == K_D:
                    rightPressed = False
                if event.key == K_S:
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
                
        if fuel > 0:
            if aPressed: 
                player.addVelocity(Vector(-1.0,0))
                fuel = fuel - 2 
            if sPressed: 
                player.addVelocity(Vector(0.0,-1.0))
                fuel = fuel - 2 
            if dPressed: 
                player.addVelocity(Vector(1.0,0.0))
                fuel = fuel - 2 
            if wPressed: 
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
        
        if fuel > 500: fuel = 500    
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
        window.blit(text, textRect)
        pygame.display.flip()
        pygame.time.Clock().tick(30)
               
    
