import pygame

class Paddle:
    Xpos = []
    Ypos = []
    Width = []
    Height = []
    Rectx = []
    Speed = []
    Color = (255, 255, 255)

    def __init__(self, Screen, Speed, x, y, w, h):
        self.Xpos = x       #offset
        self.Ypos = y       #offset
        self.Width = w
        self.Height = h
        self.Speed = Speed
        self.Rectx = pygame.Rect(self.Xpos, self.Ypos, self.Width, self.Height)
        self.Rectx.bottom = Screen.get_height() - self.Height*2
        self.Rectx.left = (Screen.get_width() - self.Width)/2


    def Move(self, screen, button):
        if (button[pygame.K_LEFT] and self.Rectx.left > 0):
            self.Rectx.left -= self.Speed
        if (button[pygame.K_RIGHT] and self.Rectx.right < screen.get_width()):
            self.Rectx.right += self.Speed
    
    def Draw(self, ScreenRender):
        pygame.draw.rect(ScreenRender, self.Color, self.Rectx, 0)

    def Start(self, screen, ball):
        pass

    
        