import pygame
import pygame.mixer

# class untuk memutar dan memainkan efek suara dalam game
class SoundEffectGame:
    
    # inisialisasi objek
    def __init__(self):
        pygame.mixer.init()
        self.sound_effects = {}
        
    # untuk memuat efek suara 
    def load_sound_effect(self, name, filepath):
        sound = pygame.mixer.Sound(filepath)
        self.sound_effects[name] = sound
        
    # untuk memutar / memainkan efek suara
    def play_sound_effect(self, name):
        sound = self.sound_effects.get(name)
        if sound:
            sound.play()
            
    # untuk menghentikan pemutaran efek suara
    def stop_sound_effect(self, name):
        if name in self.sound_effects:
            sound_effect = self.sound_effects[name]
            sound_effect.stop()
            
    # untuk menghentikan semua pemutaran efek suara yang sedang diputar dalam game
    def stop_all_sound_effects(self):
        pygame.mixer.stop()
        for sound_effect in self.sound_effects.values():
            sound_effect.stop()

