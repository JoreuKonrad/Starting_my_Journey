import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações de tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Plataforma Game")

# Cores
white = (255, 255, 255)
blue = (0, 0, 255)

# Jogador
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height
player_vel = 5

# Clock para controle de FPS
clock = pygame.time.Clock()

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimentação do jogador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_vel
    if keys[pygame.K_RIGHT]:
        player_x += player_vel

    # Limitar o jogador à tela
    player_x = max(0, min(player_x, screen_width - player_width))

    # Atualizar a tela
    screen.fill(white)
    pygame.draw.rect(screen, blue, (player_x, player_y, player_width, player_height))
    pygame.display.update()

    # Controlar FPS
    clock.tick(30)

# Encerramento do Pygame
pygame.quit()
sys.exit()
