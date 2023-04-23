#Zoe Baker
#4/22/2023
#Simple shooter game where GoodTimesWithScar HoTgUys Grian
#################################################
import pygame
from random import randint, choice
from Constants import *

#Grian movement
#Detect scar shoot
#Detect grian hit
#Detect wall hit (missed shot)
#Point system
#Countdown - when ends, lose game

class ScarSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = WIDTH/2
        self.y = HEIGHT - (HEIGHT/6)
        self.image = pygame.image.load("Hotguy.png")
        self.width = self.image.get_width()
    
    def getPosition(self):
        return (self.x, self.y)
    
    #moves Scar to the left
    def goLeft(self, amount=1):
        if(self.x >= 0):
            self.x -= amount
    
    #moves Scar to the right
    def goRight(self, amount=1):
        if(self.x <= WIDTH - self.width):
            self.x += amount
    
    def process(self, pK):
        if pK[K_LEFT]:
            self.goLeft()
        if pK[K_RIGHT]:
            self.goRight()
        if pK[K_SPACE]:
            p.draw()
    
class GrianSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.setRandomPosition()
        self.image = pygame.image.load("Cuteguy.png")
        self.width = self.image.get_width()
    
    #position (X & y)
    def setRandomPosition(self):
        self.x = randint(0, WIDTH)
        self.y = randint(0, HEIGHT/2)
    
    def getPosition(self):
        return (self.x, self.y)
    
    def moveGrian(self):
        direction = randint(0, 1)
        if(direction == 0):
            if(grian.x < WIDTH - self.width):
                self.x += 10
        else:
            if(grian.x >= 0):
                self.x -= 10

class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        self.x = WIDTH/2
        self.y = HEIGHT/2
        
    def draw(self):
        pygame.draw.circle(screen, BLACK, (self.x, self.y), 75)
        
####MAIN####
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#create sprite objects - Scar = "wizard"; Grian = "spider"
scar = ScarSprite()
grian = GrianSprite()
p = Projectile()

RUNNING = True
while(RUNNING):
    for event in pygame.event.get():
        #Check if game has been quit
        if(event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE)):
            RUNNING = False
        
    #Otherwise, process what has been pressed and move Scar
    pressedKeys = pygame.key.get_pressed()
    scar.process(pressedKeys)
    
    #Move Grian
    grian.moveGrian()
    
    #Establish screen
    screen.fill(WHITE)
    screen.blit(scar.image, scar.getPosition())
    screen.blit(grian.image, grian.getPosition())
    pygame.display.flip()