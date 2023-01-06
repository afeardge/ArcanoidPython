from operator import truediv
import pygame
import math


SIZE = 35
SPEED = 5
LIFES = 3

class Vectorx:
    X = 0
    Y = 0
    Angle = 0
    Length = 0

    def __init__(self, Length, Angle):
        Length = Length
        Angle = Angle
        self.Recalc()

    def copy(self, object):
        self = object

    def Angle_set(self, Angle):
        self.Angle = Angle
        AngleCoef = Angle/(math.pi*2);
        Angle = Angle - AngleCoef * math.pi*2
        self.Recalc()

    def Recalc(self):
        self.X = math.cos(self.Angle) * self.Length
        self.Y = math.sin(self.Angle) * self.Length

    def Getx(self):
        return self.X

    def Gety(self):
        return -self.Y

    def GetAbs(self):
        return (math.sqrt(self.X * self.X + self.Y * self.Y))

    def SetAbs(self, L):
        self.Length = L
        self.Recalc()
        

class Ball:
    Speed = Vectorx(SPEED, 0)

    Xpos = []
    Ypos = []
    Size = []
    Rectx = []
    Hitbox = []
    Speedx = []
    Speedy = []
    SpeedModule = SPEED
    Radius = []

    SpeedVectorx = 1
    SpeedVectory = -1
    SpeedVector = (1, -1)
    Life = []


    Color = (200, 255, 100)




    def __init__(self, Speed = 0, x = 0, y = 0):
        self.Speed = Vectorx(SPEED, 0)
        self.Xpos = x       #offset
        self.Ypos = y       #offset
        self.Size = SIZE
        self.Speedx = 0
        self.Speedy = 0
        self.SpeedModule
        self.Life = LIFES
        self.Radius = self.Size/2
        self.Rectx = pygame.Rect(self.Xpos, self.Ypos, self.Size, self.Size)


    def copy(self, object):
        self = object
        

    def Move(self, screen, paddle):
        if (self.Speed.GetAbs() == 0):
            self.SetPos(paddle)
            
        else:
            self.Xpos += self.Speed.Getx()
            self.Ypos += self.Speed.Gety()

    
    def Draw(self, ScreenRender):
        pygame.draw.circle(ScreenRender,self.Color, (self.Xpos, self.Ypos), self.Radius)

    def Start(self, button):
        if (button[pygame.K_SPACE]):
            self.Speed.SetAbs(SPEED)
            self.Speed.Angle_set((math.pi)/4)
            return True
        else:
            self.Speed.SetAbs(0)
            return False


    def SetPos(self, PLayer):
        self.Xpos = PLayer.Rectx.centerx
        self.Ypos = PLayer.Rectx.top - self.Radius

    def Collision_block(self, object) -> bool:
        #ball
        #top or bottom collision
        object.Cdetect = 0
        if ((self.Xpos >= object.Rectx.left) and (self.Xpos <= object.Rectx.right)):
            #bottom
            if(self.Ypos - self.Radius <= object.Rectx.bottom and self.Ypos > object.Rectx.top):
                self.Speed.Angle_set(-self.Speed.Angle)
                object.Cdetect = 1
            #top
            if(self.Ypos + self.Radius >= object.Rectx.top and self.Ypos < object.Rectx.bottom):
                self.Speed.Angle_set(-self.Speed.Angle)
                object.Cdetect = 1 
        #left or right collision
        if (self.Ypos >= object.Rectx.top and self.Ypos <= object.Rectx.bottom):
            #left
            if (self.Xpos + self.Radius >= object.Rectx.left and self.Xpos < object.Rectx.right):
                self.Speed.Angle_set(math.pi -self.Speed.Angle)
                object.Cdetect = 1 
            if (self.Xpos - self.Radius <= object.Rectx.right and self.Xpos > object.Rectx.left):
                self.Speed.Angle_set(math.pi -self.Speed.Angle)
                object.Cdetect = 1
        if (object.Cdetect == 1):
            object.Life -= 1
            object.ChangeColor()   
        return object.Cdetect



    # def Collision_paddle(self, paddle) -> bool:
    #     if ((self.Xpos >= paddle.Rectx.left) and (self.Xpos <= paddle.Rectx.right) and (self.Ypos + self.Radius == paddle.Rectx.top)):# and (self.Ypos + self.Radius < paddle.Rectx.bottom)):
    #         self.Speed.Angle_set(math.pi/2 + math.pi/4*(paddle.Rectx.centerx - self.Xpos)/(paddle.Rectx.width/2))
    #         return True

    def Change_Speed(self, Xsign, Ysign):
        self.Change_SpeedVector(Xsign, Ysign)
        if (Xsign < 0):
            self.Speedx = -math.sqrt(1 - self.Speedy*self.Speedy)
        if (Xsign > 0):
            self.Speedx = math.sqrt(1 - self.Speedy*self.Speedy)
        if (Ysign < 0):
            self.Speedy = -math.sqrt(1 - self.Speedx*self.Speedx)
        if (Ysign > 0):
            self.Speedy = math.sqrt(1 - self.Speedx*self.Speedx)

    def Change_SpeedVector(self, Xvect, Yvect):
        self.SpeedVectorx = Xvect
        self.SpeedVectory = Yvect



