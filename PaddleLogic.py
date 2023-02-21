import pygame
from Pictures import PictureEngine
from Screen import Screen

class Paddle:
    Xpos = []
    Ypos = []
    Width = []
    Height = []
    Rectx = []
    Speed = []
    Color = (255, 255, 255)
    pic = []

    def __init__(self, screen :Screen, Speed, x, y, w, h, spic: PictureEngine):
        self.Xpos = x       #offset
        self.Ypos = y       #offset
        self.Width = w
        self.Height = h
        self.Speed = Speed
        self.Rectx = pygame.Rect(self.Xpos, self.Ypos, self.Width, self.Height)
        self.Rectx.bottom = screen.height - self.Height*2
        self.Rectx.left = (screen.width - self.Width)/2
        self.Ypos = (self.Rectx.bottom + self.Rectx.top) /2 - self.Height/2
        self.pic = spic    


    def Move(self, screen :Screen, button):
        # if (button[pygame.K_LEFT] and self.Rectx.left > 0):
        if (button[pygame.K_LEFT] and (self.Xpos > 0)):
            self.Xpos -= self.Speed
            if (self.Xpos < 0): 
                self.Xpos = 0
        # if (button[pygame.K_RIGHT] and self.Rectx.right < screen.get_width()):
        if (button[pygame.K_RIGHT] and (self.Xpos + self.Width < screen.width)):
            self.Xpos += self.Speed
            if (self.Xpos > screen.width):
                self.Xpos = screen.width - self.Width
    
    def Draw(self, screen :Screen):
        screen.render(self.pic.picture_paddle, (self.Xpos, self.Ypos))
        # screen.blit(self.pic.picture_paddle, ( self.Xpos, self.Ypos))
        # pygame.draw.rect(ScreenRender, self.Color, self.Rectx, 0)

    def Start(self, screen, ball):
        pass

    
        