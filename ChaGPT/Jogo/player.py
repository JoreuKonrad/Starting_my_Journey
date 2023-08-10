import pygame

class Player:
    def __init__(self, x, y):
        self.width = 50
        self.height = 50
        self.x = x - self.width // 2
        self.y = y - self.height
        self.vel = 5
        screen_width = 800
        screen_height = 600

    def update(self):
        keys = pygame.key.get_pressed()
        screen_width = 800
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x < screen_width - self.width:
            self.x += self.vel

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.width, self.height))
