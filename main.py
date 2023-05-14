import pygame, sys
from button import Button
import subprocess

pygame.init()

SCREEN = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Menu")

BG = pygame.image.load("img/Background1.png")
    
def run_game(level_code):
    subprocess.call(["python", level_code])

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        pygame.display.set_caption("Play")
        
        FILL = pygame.image.load("img/Level.png")

        SCREEN.blit(FILL, (0, 0))
        
        PLAY_BACK = Button(image=pygame.image.load("img/x.png"), pos=(950, 50))
        EASY_BUTTON = Button(image=pygame.image.load("img/Easy Rect.png"), pos=(500, 370))
        MEDIUM_BUTTON = Button(image=pygame.image.load("img/Medium Rect.png"), pos=(500, 520))
        HARD_BUTTON = Button(image=pygame.image.load("img/Hard Rect.png"), pos=(500, 670)) 
        
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
                    run_game("easy.py")    
                if MEDIUM_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    run_game("medium.py")
                if HARD_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    run_game("hard.py")

        pygame.display.update()
    
def about():
    while True:
        ABOUT_MOUSE_POS = pygame.mouse.get_pos()
        pygame.display.set_caption("About")
        
        FILL = pygame.image.load("img/About.png")

        SCREEN.blit(FILL, (0, 0))
        
        ABOUT_BACK = Button(image=pygame.image.load("img/x.png"), pos=(950, 50))

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

        PLAY_BUTTON = Button(image=pygame.image.load("img/Play Rect.png"), pos=(250, 300))
        ABOUT_BUTTON = Button(image=pygame.image.load("img/About Rect.png"), pos=(250, 450))
        EXIT_BUTTON = Button(image=pygame.image.load("img/Exit Rect.png"), pos=(250, 600)) 

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