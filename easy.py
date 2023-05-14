import os
import sys
import random
import pygame
 
 
# Class for the orange dude
class Player(object):
    
    def __init__(self):
        self.image_surf = pygame.image.load("img/detective.png").convert_alpha()
        self.resized = pygame.transform.scale(self.image_surf, (45, 45))
        self.x = 10
        self.y = 650
 
    def move(self, dx, dy):
        
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0,)
        if dy != 0:
            self.move_single_axis(0, dy,)
    
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.x += dx
        self.y += dy
        self._player_rect = pygame.Rect(self.x, self.y, self.resized.get_width(), self.resized.get_height())
        self._player_rect.center = (self.x, self.y)
 
class Enemy(object):
    
    def __init__(self):
        self.end_rect = pygame.image.load("img/thief.png").convert_alpha()
        self.resized = pygame.transform.scale(self.end_rect, (70, 70))
        self.x = 900
        self.y = 55

class Wall(object) :
    
    def __init__(self, x, y):
        self.bg = pygame.image.load("img/pohon.png").convert()
        self.resized = pygame.transform.scale(self.bg, (50, 50))
        self.x = x
        self.y = y
        Walls.append(self)
        
class Road(object) :
    
    def __init__(self, img, x, y):
        self.model = pygame.image.load(img).convert()
        self.resized = pygame.transform.scale(self.model, (50, 50))
        self.x = x
        self.y = y
        Roads.append(self)

class Hint(object) :
    
    def __init__(self, img, x, y):
        self.hint = pygame.image.load(img).convert()
        self.resized = pygame.transform.scale(self.hint, (50, 50))
        self.x = x
        self.y = y
        Hints.append(self)
            
# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
 
# Set up the display
pygame.display.set_caption("Help Detective to Catch the Thief!")
screen = pygame.display.set_mode((1000, 800))
 
clock = pygame.time.Clock()
Walls = []
Roads = []
Hints = []
player = Player() # Create the player
enemy = Enemy()
 
# Holds the level layout in a list of strings.
level = [
    "WWWWWWWWWWWWWWWWWPWW",
    "WPPPPPPPPPPPPPPPPBPP",
    "WP3DDQDDDDDD1PYQDFDD",
    "WPNPPNPPPPPPNPPZPNPP",
    "PYFDDRPP3DDDFD1PPNPW",
    "WPNPP2XPNPPPNPNPYRPW",
    "WPNPPPPPNPPPNPNPPNPW",
    "WPNP3DQDSDDDRPNPPNPW",
    "WPTDRPNPPPPPNPNPPNPW",
    "WPNPNPTDQXPP2DFDQ4PW",
    "WPNPNPNPNPPPPPNPNPPW",
    "WPNPZP2DRP3DDDRPNPPW",
    "PPNPPPPPNPNPPPNPNPPW",
    "DDSDXPYDSD4PPYSD4PPW",
    "PPPPPPPPPPPPPPPPPPPW",
    "WWWWWWWWWWWWWWWWWWWW",
]
 
# Parse the level string above. W = wall, E = exit
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Hint("img/background.png", x, y)
        if col == "E":
            enemy = Enemy(x, y)
        if col == "P":
            Wall(x, y)
        if col == "F":
            Hint("img/perempatan.png", x, y)
        if col == "D":
            Road("img/datar.png", x, y)
        if col == "N":
            Road("img/naik.png", x, y)
        if col == "B":
            Road("img/buntu-b.png", x, y)
        if col == "X":
            Road("img/buntu-x.png", x, y)
        if col == "Y":
            Road("img/buntu-y.png", x, y)
        if col == "Z":
            Road("img/buntu-z.png", x, y)
        if col == "1":
            Road("img/turn-1.png", x, y)
        if col == "2":
            Road("img/turn-2.png", x, y)
        if col == "3":
            Road("img/turn-3.png", x, y)
        if col == "4":
            Road("img/turn-4.png", x, y)
        if col == "Q":
            Hint("img/pertigaan-u.png", x, y)
        if col == "R":
            Hint("img/pertigaan-r.png", x, y)
        if col == "S":
            Hint("img/pertigaan-d.png", x, y)
        if col == "T":
            Hint("img/pertigaan-l.png", x, y)
        x += 50
    y += 50
    x = 0
 
running = True
while running:
    
    clock.tick(60)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
 
    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        sign = 0
        player.move(-1, 0)
        
        for wall in Walls:
            maskW = pygame.mask.from_surface(wall.resized)
            offset = (wall.x - player.x, wall.y - player.y)
            if maskP.overlap(maskW, offset):
                sign = 1
        
        if sign == 1:
            player.move(1, 0)
    if key[pygame.K_RIGHT]:
        sign = 0
        player.move(1, 0)
        
        for wall in Walls:
            maskW = pygame.mask.from_surface(wall.resized)
            offset = (wall.x - player.x, wall.y - player.y)
            if maskP.overlap(maskW, offset):
                sign = 1
        
        if sign == 1:
            player.move(-1, 0)
    if key[pygame.K_UP]:
        sign = 0
        player.move(0, -1)
        
        for wall in Walls:
            maskW = pygame.mask.from_surface(wall.resized)
            offset = (wall.x - player.x, wall.y - player.y)
            if maskP.overlap(maskW, offset):
                sign = 1
        
        if sign == 1:
            player.move(0, 1)
    if key[pygame.K_DOWN]:
        sign = 0
        player.move(0, 1)
        
        for wall in Walls:
            maskW = pygame.mask.from_surface(wall.resized)
            offset = (wall.x - player.x, wall.y - player.y)
            if maskP.overlap(maskW, offset):
                sign = 1
        
        if sign == 1:
            player.move(0, -1)
 
    maskP = pygame.mask.from_surface(player.resized)
    maskE = pygame.mask.from_surface(enemy.resized)
    
    offset = (enemy.x - player.x, enemy.y - player.y)
    if maskP.overlap(maskE, offset):
        #print("Collision detected!")
        pygame.quit()
        sys.exit()
            
    # Draw the scene
    screen.fill((213, 206, 163))
    #screen.fill((0, 0, 0))
    for wall in Walls:
         screen.blit(wall.resized, (wall.x, wall.y))
    for road in Roads:
         screen.blit(road.resized, (road.x, road.y))
    for hint in Hints:
         screen.blit(hint.resized, (hint.x, hint.y))
    screen.blit(enemy.resized, (enemy.x, enemy.y))
    screen.blit(player.resized, (player.x, player.y))
    
    pygame.display.flip()
    clock.tick(360)
 
pygame.quit()
