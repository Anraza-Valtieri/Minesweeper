import pygame
import random
import os

width = 360 # width of window
height = 480 # height of window
fps = 30 # frame per second

#define the colors here
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#shapes with numbers
(SQUARE1, SQUARE2, SQUARE3, SQUARE4, SQUARE5, SQUARE6, SQUARE7, SQUARE8) = \
    ("sq1", "sq2", "sq3", "sq4", "sq5", "sq6", "sq7", "sq8")

#dictionary for converting numbers to shapes with numbers
squareDict = {
    1:SQUARE1,
    2:SQUARE2,
    3:SQUARE3,
    4:SQUARE4,
    5:SQUARE5,
    6:SQUARE6,
    7:SQUARE7,
    8:SQUARE8,
}

#set up where the folder are (for image)
game_folder = os.path.dirname("C:\JetBrains\PyCharm Community Edition 2016.2.3\Projects\ICT 1008 PROJECT")
img_folder = os.path.join(game_folder, "img")

#sprite is going to be an object
class Player(pygame.sprite.Sprite):
    #sprite for the player
    def _init_(self): #set the properties for the sprite
        pygame.sprite.Sprite._init_(self) #always required
        #self.img_load()
        #self.image = pygame.Surface((50,50))#how the sprite looks like
        self.image = pygame.image.load(os.path.join(img_folder,"MINESWEEPER_F.png")).convert() #load image to pygame #.convert() convert to pygame way
        self.image.set_colorkey(black) #ignore or make the color transparant
        self.image = pygame.transform.scale(self.image,(60, 60))
        #self.image.fill(green) #fill the surface green color
        self.rect = self.image.get_rect() #rectangle that enclose the sprite like boundaries
        self.rect.center = (width/2, height/2) # set it to center

    def img_load(self, img):
        self.image = img
        self.image.set_colorkey(black)
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height/2)

#initialize pygame and create window
pygame.init()
pygame.mixer.init() #for sound
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Minesweeper")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group() #put every sprite i make here
player = Player()
all_sprites.add(player)

#game loop
running = True
while running:
    #keep looping running at the right speed
    clock.tick(fps)
    #process input (events)
    #for the red cross of the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #update
    #all_sprites.update()

    #draw / render
    screen.fill(white) #display screen background as black
    all_sprites.draw(screen) #draw sprites on the screen
    # after drawing everything, flip the display
    pygame.display.flip()