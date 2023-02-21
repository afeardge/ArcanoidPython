import pygame




class Screen:
    scInstance = 0   
    width = 0
    height = 0
    framerate = 0
    clock = 0


    def __init__(self, width, height, framerate):
        self.framerate = framerate
        self.width = width
        self.height = height
        self.scInstance = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        pass

    def tick(self):
        pygame.display.flip()
        self.clock.tick(self.framerate)

    def render(self, surface, (x,y)):
        self.scInstance.blit(surface, (x, y))


    # def render(self,)
