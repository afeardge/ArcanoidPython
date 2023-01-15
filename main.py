from cgitb import text
import math
from os import remove
from random import random
from turtle import color, right
from typing import Text
import pygame
import sys
import random
import Collision

import BlockLogic
import BallLogic
from BlockLogic import Block
from PaddleLogic import Paddle
from BallLogic import Ball
from TextContol import Texts
from BallLogic import SPEED
from Sounds import SSounds
from Collision import CollisionHandler

#main
pygame.init()

CHandler = CollisionHandler


soundlib = SSounds()
soundlib.__init__()


#window
WIDTH, HEIGHT = 675, 1200
sc = pygame.display.set_mode((WIDTH, HEIGHT))
fps = 60
clock = pygame.time.Clock()

#player and ball
PADDLEWIDTH = WIDTH/4
PADDLEHEIGHT = HEIGHT/32
PADDLESPEED = 15
player = Paddle(sc, PADDLESPEED,  200, 200, PADDLEWIDTH, PADDLEHEIGHT)

#ball
BALLSPEED = 15
ballx = Ball(BALLSPEED, 300, 300)

#blocks
BLOCKSCNTX = 10
BLOCKSCNTY = 5
BLOCKWIDTH = WIDTH/10
BLOCKHEIGHT = HEIGHT/32


xpat_1 = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
xpat_2 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
xpat_3 = [1, 1, 1, 0, 1, 1, 0, 1, 1, 1]

blocks  = []

for i in range(BLOCKSCNTX):
    for j in range(BLOCKSCNTY):
        if (random.randint(0, 1) == 1):
            blocks.append(BlockLogic.Block(i * BLOCKWIDTH, (j + 1)*BLOCKHEIGHT + BLOCKHEIGHT, BLOCKHEIGHT, BLOCKWIDTH))

#game control
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
SCORE = 0
LIVES = -1
Txt_Score = Texts(40)
Txt_Lives = Texts(40) 
RUN = False
GAMEY = 0
GAMEBLOCKS = 0
#main game cycle
while True:
#calc
    if ((ballx.Ypos <  10 * BLOCKHEIGHT) and ballx.Speed.Y > 0):
        for i in blocks:
            i.Ypos += 1
        GAMEY += 1
        if GAMEY >= BLOCKHEIGHT:
            GAMEY = 0
            GAMEBLOCKS += 1
            for i in range(BLOCKSCNTX):
                if (random.randint(0, 1) == 1):
                    blocks.append(BlockLogic.Block(i * BLOCKWIDTH, BLOCKHEIGHT + BLOCKHEIGHT, BLOCKHEIGHT, BLOCKWIDTH))
    ballx.SpeedModule = SPEED + GAMEBLOCKS/100
    Txt_Score.place('Score = ' + str(SCORE), 20, 0)
    Txt_Lives.place('Lives = ' + str(LIVES), WIDTH - 200, 0)
    player.Move(sc, pygame.key.get_pressed())
    ballx.Move(sc, player)
    if (RUN == False or blocks.count == 0):
        RUN = ballx.Start(pygame.key.get_pressed())
    else:
        for i in blocks:
            CParamsx = CHandler.ballToBlock(ballx, i)
            if (CParamsx.BlockDamagedEvent == True):
                ballx.Speed = CParamsx.speed
                i.Life -= 1
                i.ChangeColor()
                if(i. Life != 0):
                    soundlib.sound_pop.play()
                else:
                    blocks.remove(i)
                    soundlib.sound_pop.play()
                    SCORE += 1

        CParams = [
            CHandler.ballToPaddle(ballx, player),
            CHandler.ballToScreen(ballx, sc)
        ]
        if (CParams[0].CollisionEvent == True):
            ballx.Speed = CParams[0].speed
            soundlib.sound_pop.play()

        if (CParams[1].CollisionEvent == True):
            ballx.Speed = CParams[1].speed
            soundlib.sound_pop.play()
        if (CParams[1].OutScreenEvent == True):
            RUN = False
            LIVES -= 1            
    for i in blocks: 
        if i.Ypos > (player.Rectx.top - 2 * BLOCKHEIGHT):
            blocks.remove(i)
    #draw
    sc.fill((0,0,0))
    pygame.draw.line(sc, (255, 255, 255), (0, BLOCKHEIGHT*2), (WIDTH, BLOCKHEIGHT*2), 3)

    player.Draw(sc)
    ballx.Draw(sc)
    for i in range(blocks.__len__()):
        blocks[i].Draw(sc)
    Txt_Score.Draw(sc)
    Txt_Lives.Draw(sc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or LIVES == 0:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    clock.tick(fps)
