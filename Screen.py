import pygame


class Coordinate:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        return self

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

    def render(self, surface, *pair):
        # coords = []
        # # pair = *pair
        # for num in pair:
        #     coords.append(num)
            # coords[num] = pair[num]   
        self.scInstance.blit(surface, pair)

    def flush(self):
        self.scInstance.fill((0, 0, 0), )



    # def render(self,)
