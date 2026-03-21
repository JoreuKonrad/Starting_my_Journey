import pygame

class Platform:
    def __init__(self, x, y):
        self.width = 100
        self.height = 15
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.width, self.height))

