
from tkinter import font

import pygame
from cgitb import text

class Texts:
    x = 0
    y = 0
    fontx = 0
    textsurface = 0

    def __init__(self, size):
        self.fontx = pygame.font.SysFont('Comic Sans MS', size)

    def place(self, text, x, y):
        self.textsurface = self.fontx.render(text, False, (255, 255, 255))
        self.x = x
        self.y = y

    def getPos(self):
        return (self.x, self.y)

    def Draw(self, screen):
        screen.blit(self.textsurface, (self.x, self.y))
