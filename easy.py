import os
import shlex
import sys
import random
import pygame
from button import Button
# from main import *
 
# Class for the orange dude
class Player(object):
    
    def __init__(self):
        self.image_surf = pygame.image.load("img/detective.png").convert_alpha()
        self.resized = pygame.transform.scale(self.image_surf, (55, 55))
        self.x = 10
        self.y = 643
 
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
        self.resized = pygame.transform.scale(self.end_rect, (55, 55))
        self.x = 950
        self.y = 90

class Wall(object) :
    
    def __init__(self, img, x, y):
        self.bg = pygame.image.load(img).convert()
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
        self.question = 1
        Hints.append(self)
        
def checkWall(player, Walls, maskP) :
    sign = 0
    for wall in Walls:
        maskW = pygame.mask.from_surface(wall.resized)
        offset = (wall.x - player.x, wall.y - player.y)
        if maskP.overlap(maskW, offset):
            sign = 1
        
    return sign

def checkHint(player, Hints, maskP) :
    sign = 0
    for hint in Hints:
        maskH = pygame.mask.from_surface(hint.resized)
        offset = (hint.x - player.x, hint.y - player.y)
        if maskP.overlap(maskH, offset):
            if(hint.question == 1) : sign = 2
            hint.question = 0
            break

    return sign
        
def win_page():
    pygame.display.set_caption("Congratulations!")

    FILL = pygame.image.load("img/win.png")
    SCREEN = pygame.display.set_mode((1000, 800))
    SCREEN.blit(FILL, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        
class ImageSelector:
    def __init__(self, folder_path):
        self.folder_path = folder_path
    
    def get_random_image_path(self):
        image_files = [f for f in os.listdir(self.folder_path) if os.path.isfile(os.path.join(self.folder_path, f))]
        if image_files:
            return os.path.join(self.folder_path, random.choice(image_files))
        return None
    
class Questions:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 800))
        self.image_selector = ImageSelector("riddles")
        self.displayed_image_path = None

    def display(self):
        while True:
            Q_MOUSE_POS = pygame.mouse.get_pos()
            pygame.display.set_caption("Guess The Answer!")

            if not self.displayed_image_path:
                self.displayed_image_path = self.image_selector.get_random_image_path()
                if self.displayed_image_path:
                    image = pygame.image.load(self.displayed_image_path)
                    self.screen.blit(image, (0, 0))

            Q_BACK = Button(image=pygame.image.load("img/x.png"), pos=(950, 50))
            Q_BACK.update(self.screen)
            
            A_ANS = Button(image=pygame.image.load("img/A.png"), pos=(200, 700))
            A_ANS.update(self.screen)
            
            B_ANS = Button(image=pygame.image.load("img/B.png"), pos=(500, 700))
            B_ANS.update(self.screen)
            
            C_ANS = Button(image=pygame.image.load("img/C.png"), pos=(800, 700))
            C_ANS.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if A_ANS.checkForInput(Q_MOUSE_POS):
                        if self.displayed_image_path == "riddles/Riddle 1.png":
                            self.displayed_image_path = None
                            return
                        if self.displayed_image_path == "riddles/Riddle 5.png":
                            self.displayed_image_path = None
                            return
                        if self.displayed_image_path == "riddles/Riddle 11.png":
                            self.displayed_image_path = None
                            return
                        if self.displayed_image_path == "riddles/Riddle 12.png":
                            self.displayed_image_path = None
                            return
                        if self.displayed_image_path == "riddles/Riddle 15.png":
                            self.displayed_image_path = None
                            return
                        if self.displayed_image_path == "riddles/Riddle 17.png":
                            self.displayed_image_path = None
                            return
                        if self.displayed_image_path == "riddles/Riddle 19.png":
                            self.displayed_image_path = None
                            return
                    elif B_ANS.checkForInput(Q_MOUSE_POS):
                        if self.displayed_image_path == "riddles/Riddle 2.png":
                            self.displayed_image_path = None
                            return
                        if self.displayed_image_path == "riddles/Riddle 4.png":
                            self.displayed_image_path = None
                            return
                        if self.displayed_image_path == "riddles/Riddle 6.png":
                            self.displayed_image_path = None
                            return
                        if self.displayed_image_path == "riddles/Riddle 8.png":
                            self.displayed_image_path = None
                            return
                        if self.displayed_image_path == "riddles/Riddle 9.png":
                            self.displayed_image_path = None
                            return
                        if self.displayed_image_path == "riddles/Riddle 10.png":
                            self.displayed_image_path = None
                            return
                        if self.displayed_image_path == "riddles/Riddle 13.png":
                            self.displayed_image_path = None
                            return
                        if self.displayed_image_path == "riddles/Riddle 18.png":
                            self.displayed_image_path = None
                            return
                        if self.displayed_image_path == "riddles/Riddle 20.png":
                            self.displayed_image_path = None
                            return
                    elif C_ANS.checkForInput(Q_MOUSE_POS):
                        if self.displayed_image_path == "riddles/Riddle 3.png":
                            self.displayed_image_path = None
                            return
                        if self.displayed_image_path == "riddles/Riddle 7.png":
                            self.displayed_image_path = None
                            return
                        if self.displayed_image_path == "riddles/Riddle 14.png":
                            self.displayed_image_path = None
                            return
                        if self.displayed_image_path == "riddles/Riddle 16.png":
                            self.displayed_image_path = None
                            return
                        if self.displayed_image_path == "riddles/Riddle 21.png":
                            self.displayed_image_path = None
                            return
                    elif Q_BACK.checkForInput(Q_MOUSE_POS):
                        self.displayed_image_path = None
                        return

            pygame.display.update()
    
# class ImageSelector:
#     def __init__(self, folder_path):
#         self.folder_path = folder_path
    
#     def get_random_image_path(self):
#         image_files = [f for f in os.listdir(self.folder_path) if os.path.isfile(os.path.join(self.folder_path, f))]
#         if image_files:
#             return os.path.join(self.folder_path, random.choice(image_files))
#         return None

# class Questions:
#     def __init__(self):
#         pygame.init()
#         self.screen = pygame.display.set_mode((1000, 800))
#         self.image_selector = ImageSelector("riddles")
#         self.displayed_image_path = None
#         self.buttons = []

#     def display(self):
#         while True:
#             Q_MOUSE_POS = pygame.mouse.get_pos()
#             pygame.display.set_caption("Guess The Answer!")

#             if not self.displayed_image_path:
#                 self.displayed_image_path = self.image_selector.get_random_image_path()
#                 if self.displayed_image_path:
#                     image = pygame.image.load(self.displayed_image_path)
#                     self.screen.blit(image, (0, 0))

#                     self.buttons = []
#                     button_positions = [
#                         (200, 700),  # A_ANS position
#                         (500, 700),  # B_ANS position
#                         (800, 700)   # C_ANS position
#                     ]
#                     for position in button_positions:
#                         button = Button(pygame.image.load("img/button.png"), position)
#                         self.buttons.append(button)
#                         button.update(self.screen)

#             Q_BACK = Button(pygame.image.load("img/x.png"), (950, 50))
#             Q_BACK.update(self.screen)

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     for button in self.buttons:
#                         if button.checkForInput(Q_MOUSE_POS):
#                             self.handle_answer(button)
#                     if Q_BACK.checkForInput(Q_MOUSE_POS):
#                         self.displayed_image_path = None
#                         return

#             pygame.display.update()

    # def handle_answer(self, button):
    #     answer_mapping = {
    #         "img/A.png": {
    #             "riddles/Riddle 1.png": True,
    #             "riddles/Riddle 5.png": True,
    #             "riddles/Riddle 11.png": True,
    #             "riddles/Riddle 12.png": True,
    #             "riddles/Riddle 15.png": True,
    #             "riddles/Riddle 17.png": True,
    #             "riddles/Riddle 19.png": True
    #         },
    #         "img/B.png": {
    #             "riddles/Riddle 2.png": True,
    #             "riddles/Riddle 4.png": True,
    #             "riddles/Riddle 6.png": True,
    #             "riddles/Riddle 8.png": True,
    #             "riddles/Riddle 9.png": True,
    #             "riddles/Riddle 10.png": True,
    #             "riddles/Riddle 13.png": True,
    #             "riddles/Riddle 18.png": True,
    #             "riddles/Riddle 20.png": True
    #         },
    #         "img/C.png": {
    #             "riddles/Riddle 3.png": True,
    #             "riddles/Riddle 7.png": True,
    #             "riddles/Riddle 14.png": True,
    #             "riddles/Riddle 16.png": True,
    #             "riddles/Riddle 21.png": True
    #         }
    #     }

    #     if button.image in answer_mapping:
    #         if self.displayed_image_path in answer_mapping[button.image]:
    #             self.displayed_image_path = None
    #             return
    #     else:
    #         self.displayed_image_path = None
    #         return
        
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
            Wall("img/background.png", x, y)
        if col == "E":
            enemy = Enemy(x, y)
        if col == "P":
            Wall("img/pohon.png", x, y)
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
        
        sign = checkWall(player, Walls, maskP)
        if sign == 1:
            player.move(1, 0)
        
        sign = checkHint(player, Hints, maskP)
        if sign == 2:
            QUESTION = Questions()
            QUESTION.display()
            # print("Ini Hint")

    if key[pygame.K_RIGHT]:
        sign = 0
        player.move(1, 0)
        
        sign = checkWall(player, Walls, maskP)
        if sign == 1:
            player.move(-1, 0)
        
        sign = checkHint(player, Hints, maskP)
        if sign == 2:
            QUESTION = Questions()
            QUESTION.display()
            # print("Ini Hint")
            
    if key[pygame.K_UP]:
        sign = 0
        player.move(0, -1)
        
        sign = checkWall(player, Walls, maskP)
        if sign == 1:
            player.move(0, 1)
        
        sign = checkHint(player, Hints, maskP)
        if sign == 2:
            QUESTION = Questions()
            QUESTION.display()
            # print("Ini Hint")
            
    if key[pygame.K_DOWN]:
        sign = 0
        player.move(0, 1)
        
        sign = checkWall(player, Walls, maskP)
        if sign == 1:
            player.move(0, -1)
        
        sign = checkHint(player, Hints, maskP)
        if sign == 2:
            QUESTION = Questions()
            QUESTION.display()
            # print("Ini Hint")
 
    maskP = pygame.mask.from_surface(player.resized)
    maskE = pygame.mask.from_surface(enemy.resized)
    
    offset = (enemy.x - player.x, enemy.y - player.y)
    if maskP.overlap(maskE, offset):
        #print("Collision detected!")
        win_page()
        # pygame.quit()
        # sys.exit()
            
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
