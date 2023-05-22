import pygame

# Class button berfungsi untuk merepresentasikan tombol dalam game
class Button():
    # berfungsi untuk menginisialisasi atribut-atribut objek `button` saat objek dibuat
    def __init__(self, image, pos):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        if self.image is not None:
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        else:
            self.rect = pygame.Rect(self.x_pos, self.y_pos, 0, 0)
            
    # berfungsi untuk menggambar tombol pada layar
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
            
    # berfungsi untuk memeriksa apakah tombol ditekan berdasarkan posisi klik user
    def checkForInput(self, position):
        return self.rect.collidepoint(position)
