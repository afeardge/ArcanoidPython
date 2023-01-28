import pygame

class PictureEngine:
    picture_wallpaper = []
    picture_wallpaper_sizeY = []
    picture_block_life = []
    picture_ball = []
    picture_paddle = []

    def __init__(self):
        self.picture_wallpaper = pygame.image.load("Pictures/wallpaper_default.jpg").convert()
        self.picture_wallpaper_sizeY = self.picture_wallpaper.get_height()
        self.picture_block_life = [pygame.image.load("Pictures/block_life1.png"),
                                    pygame.image.load("Pictures/block_life2.png"),
                                    pygame.image.load("Pictures/block_life3.png")]
        self.picture_ball = pygame.image.load("Pictures/ball.png")
        self.picture_paddle = pygame.image.load("Pictures/paddle.png")
