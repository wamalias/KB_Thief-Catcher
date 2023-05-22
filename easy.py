import os
import shlex
import sys
import random
import pygame
from button import Button
from sound import SoundEffectGame
import path
import time
# from main import *

# Class Player berfungsi untuk merepresentasikan karakter pemain dalam game
class Player(object):
    # berfungsi untuk menginisialisasi atribut objek `Player` saat objek dibuat
    def __init__(self):
        self.image_surf = pygame.image.load("img/detective.png").convert_alpha() # menggambar karakter player
        self.resized = pygame.transform.scale(self.image_surf, (55, 55)) # mengatur ukuran gambar karakter player
        self.x = 10
        self.y = 643
        self.life = 1 # menyimpan jumlah nyawa karakter player
    
    # berfungsi untuk menggerakkan player pada sumbu x atau sumbu y
    def move(self, dx, dy):
        
        if dx != 0:
            self.move_single_axis(dx, 0,)
        if dy != 0:
            self.move_single_axis(0, dy,)
    
    # berfungsi untuk menggerakkan player pada sumbu yang ditentukan
    def move_single_axis(self, dx, dy):

        self.x += dx
        self.y += dy
        self._player_rect = pygame.Rect(self.x, self.y, self.resized.get_width(), self.resized.get_height())
        self._player_rect.center = (self.x, self.y)

# Class Enemy berfungsi untuk merepresentasikan musuh dalam game
class Enemy(object):
    # berfungsi untuk menginisialisasi atribut objek`Enemy` saat objek dibuat
    def __init__(self):
        self.end_rect = pygame.image.load("img/thief.png").convert_alpha()
        self.resized = pygame.transform.scale(self.end_rect, (55, 55))
        self.x = 950
        self.y = 90

# Class Wall berfungsi untuk merepresentasikan dinding dalam suatu game
class Wall(object) :
    
    def __init__(self, img, x, y):
        self.bg = pygame.image.load(img).convert()
        self.resized = pygame.transform.scale(self.bg, (50, 50))
        self.x = x
        self.y = y
        Walls.append(self)
 
# Class Road berfungsi untuk merepresentasikan jalan dalam suatu game
class Road(object) :
    
    def __init__(self, img, x, y):
        self.model = pygame.image.load(img).convert()
        self.resized = pygame.transform.scale(self.model, (50, 50))
        self.x = x
        self.y = y
        Roads.append(self)

# Class Hint berfungsi untuk merepresentasikan hint dalam suatu game
class Hint(object) :
    
    def __init__(self, img, x, y, index):
        self.hint = pygame.image.load(img).convert() # mengambil gambar hint
        self.resized = pygame.transform.scale(self.hint, (50, 50)) # mengatur ukuran gambar hint
        self.x = x # posisi dalam koordinat x
        self.y = y # posisi dalam koordinat y
        self.index = index
        self.question = 1
        Hints.append(self)
        path.append(abs(self.x - 950), abs(self.y - 100), index) # menambahkan informasi perbedaan x dan y terhadap titik koordinat tertentu kedalam daftar path

# berfungsi untuk memeriksa adanya tabrakan antara player dengan dinding dalam game
def checkWall(player, Walls, maskP) :
    sign = 0
    for wall in Walls:
        maskW = pygame.mask.from_surface(wall.resized)
        offset = (wall.x - player.x, wall.y - player.y)
        if maskP.overlap(maskW, offset):
            sign = 1
        
    return sign

# berfungsi untuk memeriksa apakah player berinteraksi dengan hint dalam game
def checkHint(player, Hints, maskP) :
    for hint in Hints:
        maskH = pygame.mask.from_surface(hint.resized)
        offset = (hint.x - player.x, hint.y - player.y) # menghitung perbedaan posisi antara player dengan hint saat ini
        if maskP.overlap(maskH, offset):
            if(hint.question == 1) : 
                QUESTION = Questions() # untuk menampilkan pertanyaan terkait hint pada player
                correction = QUESTION.display(player) # mengembalikan koreksi jawaban yang diberikan oleh player
                if correction == "Benar" : 
                    if hint.index != 'C' : 
                        next = path.find(hint.index, 'C')
                        if(next == 1) : hintview = HintView("img/left.png")
                        elif(next == 2) : hintview = HintView("img/up.png")
                        elif(next == 3) : hintview = HintView("img/right.png")
                        elif(next == 4) : hintview = HintView("img/down.png")
                        
                        hintview.display()
                    else :
                        hintview = HintView("img/right.png")
                        hintview.display()
                else :
                    game_sound.stop_sound_effect("play")
                    final_page("img/lose.png", "Sorry, You Lose!")
                hint.question = 0
            break
 
# berfungsi untuk menampilkan halaman akhir game
def final_page(page, caption):
    pygame.display.set_caption(caption)

    FILL = pygame.image.load(page)
    SCREEN = pygame.display.set_mode((1000, 800))
    SCREEN.blit(FILL, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

# class ImageSelector berfungsi untuk memilih path secara acak
class ImageSelector:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        
    # untuk mendapatkan path secara acak
    def get_random_image_path(self):
        image_files = [f for f in os.listdir(self.folder_path) if os.path.isfile(os.path.join(self.folder_path, f))]
        if image_files:
            return os.path.join(self.folder_path, random.choice(image_files))
        return None
    
import pygame
import sys

pygame.init()

# Class Question berfungsi untuk pengimplementasian perntanyaan dalam game
class Questions:
    def __init__(self):
        self.screen = pygame.display.set_mode((1000, 800))
        self.image_selector = ImageSelector("riddles")
        self.displayed_image_path = None
        self.font = pygame.font.Font(None, 36)
    
    # untuk menampilkan pertanyaan pada layar
    def display(self, player):
        while True:
            Q_MOUSE_POS = pygame.mouse.get_pos()
            pygame.display.set_caption("Guess The Answer!")

            if not self.displayed_image_path:
                self.displayed_image_path = self.image_selector.get_random_image_path()
                if self.displayed_image_path:
                    image = pygame.image.load(self.displayed_image_path)
                    self.screen.blit(image, (0, 0))
                    
            # untuk menampilkan pilihan jawaban A/B/C
            Q_BACK = Button(image=pygame.image.load("img/x.png"), pos=(950, 50))
            A_ANS = Button(image=pygame.image.load("img/A.png"), pos=(200, 700))
            B_ANS = Button(image=pygame.image.load("img/B.png"), pos=(500, 700))
            C_ANS = Button(image=pygame.image.load("img/C.png"), pos=(800, 700))

            for button in [Q_BACK, A_ANS, B_ANS, C_ANS]:
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # untuk menampilkan pertanyaan sesuai dengan letak jawaban benarnya
                correct_paths_set_A = {"riddles/1.png", "riddles/5.png", "riddles/11.png", "riddles/12.png", "riddles/15.png", "riddles/17.png", "riddles/19.png"}
                correct_paths_set_B = {"riddles/2.png", "riddles/4.png", "riddles/6.png", "riddles/8.png", "riddles/9.png", "riddles/10.png", "riddles/13.png", "riddles/18.png", "riddles/20.png"}
                correct_paths_set_C = {"riddles/3.png", "riddles/7.png", "riddles/14.png", "riddles/16.png", "riddles/21.png"}

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # jawaban A
                    if A_ANS.checkForInput(Q_MOUSE_POS):
                        response = "salah"
                        for element in correct_paths_set_A:
                            if element[8:10] == self.displayed_image_path[8:10]:
                                response = "Benar"

                        print(response)
                        if response == "Benar":
                            return response
                        else:
                            if player.life > 0:
                                text = self.font.render("You have 1 life left", True, (255, 0, 0))
                                text_rect = text.get_rect(center=(self.screen.get_width() // 2, 50))
                                self.screen.blit(text, text_rect)
                                player.life -= 1

                            else:
                                return
                    # jawaban B
                    if B_ANS.checkForInput(Q_MOUSE_POS):
                        response = "salah"
                        for element in correct_paths_set_B:
                            if element[8:10] == self.displayed_image_path[8:10]:
                                response = "Benar"

                        print(response)
                        if response == "Benar":
                            return response
                        else:
                            if player.life > 0:
                                text = self.font.render("You have 1 life left", True, (255, 0, 0))
                                text_rect = text.get_rect(center=(self.screen.get_width() // 2, 50))
                                self.screen.blit(text, text_rect)
                                player.life -= 1
                            else:
                                return
                    # jawaban C
                    if C_ANS.checkForInput(Q_MOUSE_POS):
                        response = "salah"
                        for element in correct_paths_set_C:
                            if element[8:10] == self.displayed_image_path[8:10]:
                                response = "Benar"

                        print(response)
                        if response == "Benar":
                            return response
                        else:
                            if player.life > 0:
                                text = self.font.render("You have 1 life left", True, (255, 0, 0))
                                text_rect = text.get_rect(center=(self.screen.get_width() // 2, 50))
                                self.screen.blit(text, text_rect)
                                player.life -= 1
                            else:
                                return

                    if Q_BACK.checkForInput(Q_MOUSE_POS):
                        self.displayed_image_path = None
                        return

            pygame.display.update()

# Class HintView untuk menampilkan tampilan hint dalam permainan
class HintView:
    def __init__(self, path):
        self.screen = pygame.display.set_mode((1000, 800))
        self.image = pygame.image.load(path)
        self.font = pygame.font.Font(None, 36)
    
    # untuk menampilkan tampilan hint
    def display(self):
        while True:
            Q_MOUSE_POS = pygame.mouse.get_pos()
            pygame.display.set_caption("Guess The Answer!")
            
            self.screen.blit(self.image, (200, 200))

            Q_BACK = Button(image=pygame.image.load("img/x.png"), pos=(950, 50))
            
            for button in [Q_BACK]:
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    if Q_BACK.checkForInput(Q_MOUSE_POS):
                        self.image = None
                        return

            pygame.display.update()
 
# untuk menampilkan timer pada layar dalam detik
def display_timer(screen, elapsed_time):
    font = pygame.font.Font(None, 36)
    timer_text = font.render("Time: " + format_time(elapsed_time), True, (0, 0, 0))
    screen.blit(timer_text, (10, 10))

def format_time(secs):
    mins = secs // 60
    secs = secs % 60
    time_format = "{:02d}:{:02d}".format(int(mins), int(secs))
    return time_format

# untuk menginisialisasi library pygame dan mengatur posisi window ke tengah layar
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
 
# Set up the display
pygame.display.set_caption("Help Detective to Catch the Thief!")
screen = pygame.display.set_mode((1000, 800))

clock = pygame.time.Clock() # untuk mengontrol kecepatan waktu game
Walls = [] # untuk menyimpan objek dinding
Roads = [] # untuk menyimpan objek jalan
Hints = [] # untuk menyimpan objek hint
player = Player() # membuat objek player dengan menggunakan class player
enemy = Enemy() # membuat objek enemy dengan menggunakan class enemy

# maps yang digunakan untuk level easy
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

# melakukan parsing dari string level yang diberikan. Setiap karakter dalam string level diperiksa dan objek yang sesuai dibuat berdasarkan karakter tersebut
x = y = 0
index = 'A'
for row in level:
    for col in row:
        if col == "W":
            Wall("img/background.png", x, y)
            path.draw("#")
        if col == "P":
            Wall("img/pohon.png", x, y)
            path.draw("#")
        if col == "F":
            Hint("img/perempatan.png", x, y, index)
            path.draw(index)
            index = chr(ord(index) + 1)
        if col == "D":
            Road("img/datar.png", x, y)
            path.draw("*")
        if col == "N":
            Road("img/naik.png", x, y)
            path.draw("*")
        if col == "B":
            Road("img/buntu-b.png", x, y)
            path.draw("!")
        if col == "X":
            Road("img/buntu-x.png", x, y)
            path.draw("!")
        if col == "Y":
            Road("img/buntu-y.png", x, y)
            path.draw("!")
        if col == "Z":
            Road("img/buntu-z.png", x, y)
            path.draw("!")
        if col == "1":
            Road("img/turn-1.png", x, y)
            path.draw("1")
        if col == "2":
            Road("img/turn-2.png", x, y)
            path.draw("2")
        if col == "3":
            Road("img/turn-3.png", x, y)
            path.draw("3")
        if col == "4":
            Road("img/turn-4.png", x, y)
            path.draw("4")
        if col == "Q":
            Hint("img/pertigaan-u.png", x, y, index)
            path.draw(index)
            index = chr(ord(index) + 1)
        if col == "R":
            Hint("img/pertigaan-r.png", x, y, index)
            path.draw(index)
            index = chr(ord(index) + 1)
        if col == "S":
            Hint("img/pertigaan-d.png", x, y, index)
            path.draw(index)
            index = chr(ord(index) + 1)
        if col == "T":
            Hint("img/pertigaan-l.png", x, y, index)
            path.draw(index)
            index = chr(ord(index) + 1)
        x += 50
    y += 50
    x = 0

path.roadMap()
path.printG()

# untuk memuat dan memainkan efek suara dalam game
game_sound = SoundEffectGame()
game_sound.load_sound_effect("play", "sounds/play.mp3")
game_sound.play_sound_effect("play")

# set waktu 3 menit / 180 detik 
MAX_PLAY_TIME = 180  # 3 minutes in seconds
start_time = time.time()
elapsed_time = 0

running = True
while running:
    clock.tick(60)   
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
 
    # untuk memeriksa tombol yang ditekan userd
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        sign = 0
        player.move(-1.5, 0)
        
        sign = checkWall(player, Walls, maskP)
        if sign == 1:
            player.move(1.5, 0)
        
        checkHint(player, Hints, maskP)

    if key[pygame.K_RIGHT]:
        sign = 0
        player.move(1.5, 0)
        
        sign = checkWall(player, Walls, maskP)
        if sign == 1:
            player.move(-1.5, 0)
        
        checkHint(player, Hints, maskP)
            
    if key[pygame.K_UP]:
        sign = 0
        player.move(0, -1.5)
        
        sign = checkWall(player, Walls, maskP)
        if sign == 1:
            player.move(0, 1.5)
        
        checkHint(player, Hints, maskP)
            
    if key[pygame.K_DOWN]:
        sign = 0
        player.move(0, 1.5)
        
        sign = checkWall(player, Walls, maskP)
        if sign == 1:
            player.move(0, -1.5)
        
        checkHint(player, Hints, maskP)
 
    maskP = pygame.mask.from_surface(player.resized)
    maskE = pygame.mask.from_surface(enemy.resized)
    
    offset = (enemy.x - player.x, enemy.y - player.y)
    if maskP.overlap(maskE, offset):
        #print("Collision detected!")
        game_sound.stop_sound_effect("play")
        final_page("img/win.png", "Congratulations! You Win!")
        # pygame.quit()
        # sys.exit()
    
    # menghitung waktu yang telah berlalu
    current_time = time.time()
    elapsed_time = current_time - start_time

    # Periksa apakah waktu putar maksimum tercapai
    if elapsed_time >= MAX_PLAY_TIME:
        game_sound.stop_sound_effect("play")
        final_page("img/lose.png", "Sorry, You Lose!")
          
    # untuk menggambar elemen-elemen dalam game pada layar
    screen.fill((213, 206, 163))
    
    for wall in Walls:
         screen.blit(wall.resized, (wall.x, wall.y))
    for road in Roads:
         screen.blit(road.resized, (road.x, road.y))
    for hint in Hints:
         screen.blit(hint.resized, (hint.x, hint.y))
    screen.blit(enemy.resized, (enemy.x, enemy.y))
    screen.blit(player.resized, (player.x, player.y))
    
    # untuk menampilkan timer
    display_timer(screen, elapsed_time)
    
    pygame.display.flip()
    clock.tick(360)
 
pygame.quit()
