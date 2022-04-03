import pygame
from constants import *

class Sound(object):
    def __init__(self, soundfile, loop=False):
        self.sound = pygame.mixer.Sound(soundfile)
        self.loop = loop
        self.sound.set_volume(VOLUME)
        self.is_playing = False
    
    def play(self):
        self.sound.play(-1 if self.loop else 0)
        if self.loop:
            self.is_playing = True
    
    def stop(self):
        self.sound.stop()
        self.is_playing = False

class GameSounds(object):
    def __init__(self):
        self.sounds = {INTRO: Sound("sounds/pacman_beginning.wav"),
                        CHOMP: Sound("sounds/pacman_chomp.wav", loop=True),
                        DEATH: Sound("sounds/pacman_death.wav"),
                        EATGHOST: Sound("sounds/pacman_eatghost.wav"),
                        EATFRUIT: Sound("sounds/pacman_eatfruit.wav")}
    