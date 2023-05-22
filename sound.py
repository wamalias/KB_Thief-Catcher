import pygame
import pygame.mixer

class SoundEffectGame:
    def __init__(self):
        pygame.mixer.init()
        self.sound_effects = {}
    
    def load_sound_effect(self, name, filepath):
        sound = pygame.mixer.Sound(filepath)
        self.sound_effects[name] = sound
    
    def play_sound_effect(self, name):
        sound = self.sound_effects.get(name)
        if sound:
            sound.play()

    def stop_sound_effect(self, name):
        if name in self.sound_effects:
            sound_effect = self.sound_effects[name]
            sound_effect.stop()

    def stop_all_sound_effects(self):
        pygame.mixer.stop()
        for sound_effect in self.sound_effects.values():
            sound_effect.stop()

# # Contoh penggunaan
# game_sound = SoundEffectGame()

# # Memuat efek suara
# game_sound.load_sound_effect("explosion", "sounds/explosion.wav")
# game_sound.load_sound_effect("powerup", "sounds/powerup.wav")

# # Memainkan efek suara
# game_sound.play_sound_effect("explosion")

# # Menghentikan efek suara
# game_sound.stop_sound_effect("explosion")

# # Menghentikan semua efek suara
# game_sound.stop_all_sound_effects()
