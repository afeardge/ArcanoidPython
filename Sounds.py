import pygame

class SSounds:
    
    sound_boom = []
    sound_pop = []

    def __init__(self):
        self.sound_boom = pygame.mixer.Sound("Sounds/boom.wav")
        # self.sound_pop = pygame.mixer.Sound("Sounds/boom.wav")
        self.sound_pop = pygame.mixer.Sound("Sounds/pop.wav")
        