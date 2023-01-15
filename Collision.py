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

    def ballToObject(self, ball: Ball, object) -> CollisionParams:
        if (type(object) == Paddle):
            return self.ballToPaddle(ball, object)
        if (type(object) == Block):
            return self.ballToBlock(ball, object)
        else:
            return self.ballToScreen(ball, object)




    def ballToScreen(ball: Ball, screen) -> CollisionParams:
        collisionResult = CollisionParams()
        speed = ball.Speed
        #right
        if ((ball.Xpos + ball.Radius) >= screen.get_width()):
            if (ball.Speed.Angle < math.pi/2 or ball.Speed.Angle > math.pi * 1.5):
                collisionResult.CollisionEvent = True              
        #left
        if ((ball.Xpos - ball.Radius) <= 0):
            if (ball.Speed.Angle > math.pi/2 or ball.Speed.Angle < math.pi * 1.5):
                collisionResult.CollisionEvent = True
        #bottom
        if ((ball.Ypos + ball.Radius) >= screen.get_height()):
            if (ball.Speed.Angle > 0 or ball.Speed.Angle < math.pi):
                collisionResult.CollisionEvent = True
                collisionResult.OutScreenEvent = True
        #top        
        if ((ball.Ypos - ball.Radius) <= 0):
            if (ball.Speed.Angle > math.pi or ball.Speed.Angle < 2 * math.pi):
                collisionResult.CollisionEvent = True
        if (collisionResult.CollisionEvent == True):
            speed.Angle_set( math.pi - ball.Speed.Angle)     
        collisionResult.speed = ball.Speed          
        return collisionResult

    def ballToPaddle(ball: Ball, paddle: Paddle) -> CollisionParams:
        collisionResult = CollisionParams()
        speed = ball.Speed
        if ((ball.Xpos >= paddle.Rectx.left) and (ball.Xpos <= paddle.Rectx.right) and (ball.Ypos + ball.Radius == paddle.Rectx.top)):# and (self.Ypos + self.Radius < paddle.Rectx.bottom)):
            if (ball.Speed.Angle > 0 or ball.Speed.Angle < math.pi):
                collisionResult.CollisionEvent = True
        if (collisionResult.CollisionEvent == True):
            speed.Angle_set(math.pi/2 + math.pi/4*(paddle.Rectx.centerx - ball.Xpos)/(paddle.Rectx.width/2))
        collisionResult.speed = ball.Speed
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


















