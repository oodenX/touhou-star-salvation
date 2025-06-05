import pygame

from .. import constant as C

class Failure:
    def __init__(self):
        self.image = C.failure_image
        self.next = 'exit'
        self.finished = False

    def update(self, surface, keys):
        image = pygame.image.load(self.image)
        surface.blit(image, (0, 0))
        if keys[pygame.K_ESCAPE]:
            self.next = 'exit'
            self.finished = True
            print('再试一次吧！')
