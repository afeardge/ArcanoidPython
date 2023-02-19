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
import Scenario
import Config


import BlockLogic
import BallLogic
from BlockLogic import Block
from PaddleLogic import Paddle
from BallLogic import Ball
from TextContol import Texts
from Config import Config
from Menu import Button

from Sounds import SSounds
from Pictures import PictureEngine
from Collision import CollisionHandler
from Scenario import hScenario

#main
pygame.init()

CHandler = CollisionHandler

Scenario_handler = hScenario
Scenario_handler.__init__(Scenario_handler, Config.DEFAULT_SCENARIO)

soundlib = SSounds()
soundlib.__init__()


#window
sc = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
fps = 60
clock = pygame.time.Clock()
picturelib = PictureEngine()
picturelib.__init__()

#player and ball
player = Paddle(sc, Config.PADDLE_SPEED,  200, 200, Config.PADDLE_WIDTH, Config.PADDLE_HEIGHT, picturelib)

#ball
BALLSPEED = 10
ballx = Ball(picturelib, BALLSPEED, 300, 300)


xpat_1 = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
xpat_2 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
xpat_3 = [1, 1, 1, 0, 1, 1, 0, 1, 1, 1]

blocks  = []

for i in range(Config.BLOCKS_COUNT_X):
    for j in range(Config.BLOCKS_COUNT_Y):
        if (random.randint(0, 1) == 1):
            blocks.append(BlockLogic.Block(i * Config.BLOCKS_WIDTH, (j + 2)*Config.BLOCKS_HEIGHT, Config.BLOCKS_HEIGHT, Config.BLOCKS_WIDTH, picturelib))

#game control
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
SCORE = 0
LIVES = -1
Txt_Score = Texts(40)
Txt_Lives = Texts(40) 
TXT_MENU = Texts(40)
RUN = False
GAMEY = 0
GAMEBLOCKS = 0

BUTTON_MENU = Button
BUTTON_MENU.__init__(BUTTON_MENU, 150, 550, 300, 300, picturelib.picture_button, TXT_MENU)

SCLENGTH = 0

#main game cycle
while True:

    # Scenario_handler.
    if (Scenario_handler.getScenario(Scenario_handler) == 1):
        if (ballx.Start(pygame.key.get_pressed()) == 2):
            Scenario_handler.setScenario(Scenario_handler, Config.SCENARIO_GAME)
    if (Scenario_handler.getScenario(Scenario_handler) == 2):
#calc
        if ((ballx.Ypos <  10 * Config.BLOCKS_HEIGHT) and ballx.Speed.Y > 0):
            for i in blocks:
                i.Ypos += 1
                
            GAMEY += 1
            SCLENGTH += 1
            if GAMEY >= Config.BLOCKS_HEIGHT:
                GAMEY = 0
                GAMEBLOCKS += 1
                for i in range(Config.BLOCKS_COUNT_X):
                    if (random.randint(0, 1) == 1):
                        blocks.append(BlockLogic.Block(i * Config.BLOCKS_WIDTH, Config.BLOCKS_HEIGHT * 2, Config.BLOCKS_HEIGHT, Config.BLOCKS_WIDTH, picturelib))
        ballx.SpeedModule = BALLSPEED + GAMEBLOCKS/100
        Txt_Score.place('Score = ' + str(SCORE), 20, 0)
        Txt_Lives.place('Lives = ' + str(LIVES), Config.WINDOW_WIDTH - 200, 0)
        player.Move(sc, pygame.key.get_pressed())
        ballx.Move(sc, player)
        if (RUN == False or blocks.count == 0):
            if (ballx.Start(pygame.key.get_pressed()) == 1):
                RUN = True

            # RUN = ballx.Start(pygame.key.get_pressed())
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
                        soundlib.sound_boom.play()
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
            if i.Ypos > (player.Rectx.top - 2 *  Config.BLOCKS_HEIGHT):
                blocks.remove(i)
        #draw


        sc.fill((0,0,0), )

    if (Scenario_handler.getScenario(Scenario_handler)  == 1):
        sc.blit(picturelib.picture_wallpaper_menu, (0, 0))
        BUTTON_MENU.Draw(BUTTON_MENU, sc)
        TXT_MENU.Draw(sc)



    if (Scenario_handler.getScenario(Scenario_handler) == 2):
        
        
        sc.blit(picturelib.picture_wallpaper, (0, Config.WINDOW_HEIGHT - picturelib.picture_wallpaper_sizeY + SCLENGTH))
        rect =  pygame.Rect(0, 0, Config.WINDOW_WIDTH,  Config.BLOCKS_HEIGHT*2)
        pygame.draw.rect(sc, (0,0,0), rect, 0)  
        player.Draw(sc)
        ballx.Draw(sc)
        for i in range(blocks.__len__()):
            blocks[i].Draw(sc)
        Txt_Score.Draw(sc)
        Txt_Lives.Draw(sc)
        pygame.draw.line(sc, (255, 255, 255), (0, Config.BLOCKS_HEIGHT*2), (Config.WINDOW_WIDTH,  Config.BLOCKS_HEIGHT*2), 3)
    

    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or LIVES == 0:
            pygame.quit()
            sys.exit()
        
    pygame.display.flip()
        
    clock.tick(fps)
