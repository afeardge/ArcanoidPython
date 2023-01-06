import pygame
import BallLogic
from BallLogic import Vectorx
from BallLogic import Ball
from PaddleLogic import Paddle
import math
from BlockLogic import Block



class CollisionParams:
    CollisionEvent = False
    OutScreenEvent = False
    BlockDamagedEvent = False
    speed = Vectorx
    def __init__(self):
        pass
        

class CollisionHandler:

    def ballToScreen(ball: Ball, screen) -> CollisionParams:
        collisionResult = CollisionParams()
        NBall = ball
        Speed = ball.Speed
        #right
        if ((ball.Xpos + NBall.Radius) >= screen.get_width()):
            if (Speed.Angle < math.pi/2 or Speed.Angle > math.pi * 1.5):
                Speed.Angle_set(math.pi - Speed.Angle)
                collisionResult.CollisionEvent = True
                
        #left
        if ((NBall.Xpos - NBall.Radius) <= 0):
            if (Speed.Angle > math.pi/2 or Speed.Angle < math.pi * 1.5):
                Speed.Angle_set(math.pi - NBall.Speed.Angle)
                collisionResult.CollisionEvent = True
        #bottom
        if ((NBall.Ypos + NBall.Radius) >= screen.get_height()):
            if (Speed.Angle > 0 or Speed.Angle < math.pi):
                Speed.Angle_set(-NBall.Speed.Angle)
                collisionResult.CollisionEvent = True
                collisionResult.OutScreenEvent = True
        #top        
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

    def ballToBlock(ball: Ball, block: Block)  -> CollisionParams:
        collisionResult = CollisionParams()
        NBall = ball
        Speed = ball.Speed

        if ((NBall.Xpos > block.Rectx.left) and (NBall.Xpos < block.Rectx.right)):
            #bottom
            if (NBall.Ypos - NBall.Radius <= block.Rectx.bottom and NBall.Ypos > block.Rectx.top):
                if (Speed.Angle > math.pi or Speed.Angle < 2 * math.pi):
                    collisionResult.CollisionEvent = True
            #top
            if (NBall.Ypos + NBall.Radius >= block.Rectx.bottom and NBall.Ypos < block.Rectx.bottom):
                if (Speed.Angle > 0 or Speed.Angle < math.pi):
                    collisionResult.CollisionEvent = True
        if ((NBall.Ypos >= block.Rectx.top) and (NBall.Ypos <= block.Rectx.bottom)):
            #left
            if (NBall.Xpos + NBall.Radius >= block.Rectx.left and NBall.Xpos < block.Rectx.right) :
                if (Speed.Angle < math.pi/2 or Speed.Angle > math.pi * 1.5):
                    collisionResult.CollisionEvent = True
            #right
            if (NBall.Xpos - NBall.Radius <= block.Rectx.left and NBall.Xpos > block.Rectx.left):
                if (Speed.Angle > math.pi/2 or Speed.Angle < math.pi * 1.5):        
                    collisionResult.CollisionEvent = True
        if (collisionResult.CollisionEvent == True):
            collisionResult.BlockDamagedEvent = collisionResult.CollisionEvent
            Speed.Angle_set(-Speed.Angle)
        collisionResult.speed = Speed
        return collisionResult



    def checkAngle(Angle):
        AngleCoef = Angle/(math.pi*2);
        Angle = Angle - AngleCoef * math.pi*2
        return Angle


















