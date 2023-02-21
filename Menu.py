import pygame
from Pictures import PictureEngine
from TextContol import Texts
from Screen import Screen

class Button:
    Xpos, Ypos = [], []
    Width, Height = [], []
    Color = []
    Rectx = []
    pic = []
    text = []

    def __init__(self, xpos, ypos, height, width, spic: PictureEngine, text: Texts):
        self.Xpos = xpos
        self.Ypos = ypos
        self.Width = height
        self.Height = width
        self.Rectx = pygame.Rect(self.Xpos, self.Ypos,self.Width, self.Height)
        self.pic = spic
        self.text = text
        text.place("", self.Xpos, self.Ypos)

    def Draw(self, scren :Screen):
        self.Rectx = pygame.Rect(self.Xpos, self.Ypos,self.Width, self.Height)
        scren.render(self.pic, (self.Xpos, self.Ypos))
        scren.render(self.text.textsurface, self.text.getPos())
        # ScreenRender.blit(self.pic, ( self.Xpos, self.Ypos))
        # self.text.Draw(ScreenRender)

# def Place(self, xpos, ypos, ):

class Menu:
    PAGE_MENU = 1
    PAGE_LOOSE = 2



