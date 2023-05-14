import pygame, sys
from button import Button
# from easy import *
# from medium import *
# from hard import *

pygame.init()

SCREEN = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        pygame.display.set_caption("Play")
        
        FILL = pygame.image.load("assets/Level.png")

        SCREEN.blit(FILL, (0, 0))
        
        PLAY_BACK = Button(image=pygame.image.load("assets/x.png"), pos=(950, 50))
        EASY_BUTTON = Button(image=pygame.image.load("assets/Easy Rect.png"), pos=(500, 370))
        MEDIUM_BUTTON = Button(image=pygame.image.load("assets/Medium Rect.png"), pos=(500, 520))
        HARD_BUTTON = Button(image=pygame.image.load("assets/Hard Rect.png"), pos=(500, 670)) 
        
        for button in [PLAY_BACK, EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON]:
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if EASY_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    exec(open("easy.py").read())
                if MEDIUM_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    exec(open("medium.py").read())
                if HARD_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    exec(open("hard.py").read())
                    # pygame.quit()
                    # sys.exit()

        pygame.display.update()
    
def about():
    while True:
        ABOUT_MOUSE_POS = pygame.mouse.get_pos()
        pygame.display.set_caption("About")
        
        FILL = pygame.image.load("assets/About.png")

        SCREEN.blit(FILL, (0, 0))
        
        ABOUT_BACK = Button(image=pygame.image.load("assets/x.png"), pos=(950, 50))

        ABOUT_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ABOUT_BACK.checkForInput(ABOUT_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(250, 300))
        ABOUT_BUTTON = Button(image=pygame.image.load("assets/About Rect.png"), pos=(250, 450))
        EXIT_BUTTON = Button(image=pygame.image.load("assets/Exit Rect.png"), pos=(250, 600)) 

        for button in [PLAY_BUTTON, ABOUT_BUTTON, EXIT_BUTTON]:
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if ABOUT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    about()
                if EXIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
