import pygame

class Obstacle:
    def __init__(self, x, y):
        self.width = 30
        self.height = 30
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

# Função para aplicar uma modificação ao cenário
def apply_modification(modifications):
    x = 150  # Posição x do obstáculo (pode ser ajustada)
    y = 470  # Posição y do obstáculo (pode ser ajustada)
    obstacle = Obstacle(x, y)
    modifications.append(obstacle)
