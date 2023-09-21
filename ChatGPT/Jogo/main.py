import pygame
import sys
from player import Player
from plataforms import Platform
from modification import apply_modification

# Inicialização do Pygame
pygame.init()

screen_width = 800
screen_height = 600

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jogo de Plataforma com Modificações")


# Cores
white = (255, 255, 255)

# Relógio para controle de FPS
clock = pygame.time.Clock()

# Criação do jogador
player = Player(screen_width // 2, screen_height - 50)

# Criação das plataformas

platforms = [
    Platform(100, 500),
    Platform(300, 400),
    Platform(600, 300)
]

# Lista de modificações
modifications = []

# Loop do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualização do jogador
    player.update()

    # Atualização das modificações
    for mod in modifications:
        mod.update()

    # Atualização da tela
    screen.fill(white)
    player.draw(screen)
    for platform in platforms:
        platform.draw(screen)
    for mod in modifications:
        mod.draw(screen)
    pygame.display.update()
    clock.tick(60)

# Encerramento do Pygame
pygame.quit()
sys.exit()
