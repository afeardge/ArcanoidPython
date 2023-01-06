from cmath import rect
from enum import auto
import pygame
import random



BLOCKCLRLOW, BLOCKCLRHIGH = 200, 255
LIFES = 3

class Block:
    #hitbox
    Xpos, Ypos = [], []
    Height = []
    Width = []
    Color = []
    #Color = (random.randint(BLOCKCLRLOW, BLOCKCLRHIGH), random.randint(BLOCKCLRLOW, BLOCKCLRHIGH), random.randint(BLOCKCLRLOW, BLOCKCLRHIGH))
    #render
    Rectx = []
    Cdetect = 0
    Life = []


    #functions
    def __init__(self, xpos, ypos, height, width):
        self.Xpos = xpos
        self.Ypos = ypos
        self.Height = height
        self.Width = width
        self.Life = random.randint(1, LIFES)
        self.Rectx = pygame.Rect(self.Xpos, self.Ypos,self.Width, self.Height)
        self.ChangeColor()

    def Draw(self, ScreenRender):
        self.Rectx = pygame.Rect(self.Xpos, self.Ypos,self.Width, self.Height)
        pygame.draw.rect(ScreenRender, self.Color, self.Rectx, 0)

    
    def ChangeColor(self):
        if (self.Life == LIFES):
            self.Color = (0, random.randint(BLOCKCLRLOW, BLOCKCLRHIGH), 0)
        if (self.Life == 2):
            self.Color = (random.randint(BLOCKCLRLOW, BLOCKCLRHIGH), random.randint(BLOCKCLRLOW, BLOCKCLRHIGH), 0)
        if (self.Life == 1):
           self.Color = (random.randint(BLOCKCLRLOW, BLOCKCLRHIGH), 0, 0)

        