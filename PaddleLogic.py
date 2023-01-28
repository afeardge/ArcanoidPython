import pygame
from Pictures import PictureEngine

class Paddle:
    Xpos = []
    Ypos = []
    Width = []
    Height = []
    Rectx = []
    Speed = []
    Color = (255, 255, 255)
    pic = []

    def __init__(self, Screen, Speed, x, y, w, h, spic: PictureEngine):
        self.Xpos = x       #offset
        self.Ypos = y       #offset
        self.Width = w
        self.Height = h
        self.Speed = Speed
        self.Rectx = pygame.Rect(self.Xpos, self.Ypos, self.Width, self.Height)
        self.Rectx.bottom = Screen.get_height() - self.Height*2
        self.Rectx.left = (Screen.get_width() - self.Width)/2
        self.Ypos = (self.Rectx.bottom + self.Rectx.top) /2 - self.Height/2
        self.pic = spic


    def Move(self, screen, button):
        # if (button[pygame.K_LEFT] and self.Rectx.left > 0):
        if (button[pygame.K_LEFT] and (self.Xpos > 0)):
            self.Xpos -= self.Speed
            if (self.Xpos < 0): 
                self.Xpos =0
        # if (button[pygame.K_RIGHT] and self.Rectx.right < screen.get_width()):
        if (button[pygame.K_RIGHT] and (self.Xpos + self.Width < screen.get_width())):
            self.Xpos += self.Speed
            if (self.Xpos > screen.get_width()):
                self.Xpos = screen.get_width() - self.Width
    
    def Draw(self, ScreenRender):
        ScreenRender.blit(self.pic.picture_paddle, ( self.Xpos, self.Ypos))
        # pygame.draw.rect(ScreenRender, self.Color, self.Rectx, 0)

    def Start(self, screen, ball):
        pass

    
        