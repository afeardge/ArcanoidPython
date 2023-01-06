import pygame
import BallLogic
from BallLogic import Vectorx
from BallLogic import Ball
from PaddleLogic import Paddle
import math



class CollisionParams:
    CollisionEvent = False
    OutScreenEvent = False
    speed = Vectorx
    def __init__(self):
        pass
        

class CollisionHandler:


    


    def ballToScreen(ball: Ball, screen) -> CollisionParams:
        collisionResult = CollisionParams()
        NBall = ball
        Speed = ball.Speed
        
        if ((ball.Xpos + NBall.Radius) >= screen.get_width()):
            if (Speed.Angle < math.pi/2 or Speed.Angle > math.pi * 1.5):
                Speed.Angle_set(math.pi - Speed.Angle)
                collisionResult.CollisionEvent = True
        if ((NBall.Xpos - NBall.Radius) <= 0):
            if (Speed.Angle > math.pi/2 or Speed.Angle < math.pi * 1.5):
                Speed.Angle_set(math.pi - NBall.Speed.Angle)
                collisionResult.CollisionEvent = True
        if ((NBall.Ypos + NBall.Radius) >= screen.get_height()):
            if (Speed.Angle > 0 or Speed.Angle < math.pi):
                Speed.Angle_set(-NBall.Speed.Angle)
                collisionResult.CollisionEvent = True
                collisionResult.OutScreenEvent = True
        if ((NBall.Ypos - NBall.Radius) <= 0):
            if (Speed.Angle > math.pi or Speed.Angle < 2 * math.pi):
                Speed.Angle_set(-NBall.Speed.Angle)
                collisionResult.CollisionEvent = True
                
        collisionResult.speed = Speed
        return collisionResult

    def ballToPaddle(ball: Ball, paddle: Paddle) -> CollisionParams:
        collisionResult = CollisionParams()
        NBall = ball
        Speed = ball.Speed
        if ((NBall.Xpos >= paddle.Rectx.left) and (NBall.Xpos <= paddle.Rectx.right) and (NBall.Ypos + NBall.Radius == paddle.Rectx.top)):# and (self.Ypos + self.Radius < paddle.Rectx.bottom)):
            if (Speed.Angle > 0 or Speed.Angle < math.pi):
                Speed.Angle_set(math.pi/2 + math.pi/4*(paddle.Rectx.centerx - NBall.Xpos)/(paddle.Rectx.width/2))
                collisionResult.CollisionEvent = True
        collisionResult.speed = Speed
        return collisionResult



    def checkAngle(Angle):
        AngleCoef = Angle/(math.pi*2);
        Angle = Angle - AngleCoef * math.pi*2
        return Angle


















