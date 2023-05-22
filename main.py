import pygame
import sys
from button import Button
import subprocess
import pygame.mixer

import os
import random

pygame.init()
pygame.mixer.init()

# untuk mengatur tampilan menu dalam game
SCREEN = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Menu")

# untuk mengatur background dalam game
BG = pygame.image.load("img/Background1.png")

# untuk memutar sound dalam game
backsound = pygame.mixer.Sound("sounds/home.wav")
backsound.play()

# untuk menjalankan game dengan level tertentu
def run_game(level_code):
    subprocess.call(["python", level_code])
    
# untuk menampilkan menu play dalam game
def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        pygame.display.set_caption("Play")
        
        FILL = pygame.image.load("img/Level.png")

        SCREEN.blit(FILL, (0, 0))
        
        # untuk inisialisasi objek tombol menggunakan kelas Button untuk tampilan menu game
        PLAY_BACK = Button(image=pygame.image.load("img/x.png"), pos=(950, 50))
        EASY_BUTTON = Button(image=pygame.image.load("img/Easy Rect.png"), pos=(500, 370))
        MEDIUM_BUTTON = Button(image=pygame.image.load("img/Medium Rect.png"), pos=(500, 520))
        HARD_BUTTON = Button(image=pygame.image.load("img/Hard Rect.png"), pos=(500, 670)) 
        
        for button in [PLAY_BACK, EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON]:
            button.update(SCREEN)
        
        # untuk menghandle beberapa menu dalam main menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if EASY_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    backsound.stop()
                    run_game("easy.py")    
                if MEDIUM_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    backsound.stop()
                    run_game("medium.py")
                if HARD_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    backsound.stop()
                    run_game("hard.py")

        pygame.display.update()

# untuk menampilkan menu about dalam game
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

# fungsi utama yang menjalankan menu utama dalam game
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # untuk inisialisasi objek tombol menggunakan kelas Button untuk tampilan main menu game
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
