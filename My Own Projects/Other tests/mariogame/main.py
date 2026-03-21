 
#create a game like super mario

import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Super Mario'
CHARACTER_SIZE = 32
CHARACTER_SPEED = 5
JUMP_HEIGHT = 10
GRAVITY = 1
GROUND = SCREEN_HEIGHT - CHARACTER_SIZE
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 10
PLATFORM_COLOR = (0, 0, 255)
PLATFORM_Y_POSITIONS = [400, 300, 200, 100]
ENEMY_SIZE = 32
ENEMY_SPEED = 2
ENEMY_COLOR = (255, 0, 0)
ENEMY_Y_POSITIONS = [400, 300, 200, 100]
FONT_COLOR = (255, 255, 255)
FONT_SIZE = 36
GAME_OVER_TEXT = 'Game Over'
GAME_OVER_X = 300

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)

# Load images
character_image = pygame.image.load('character.png')
character_image = pygame.transform.scale(character_image, (CHARACTER_SIZE, CHARACTER_SIZE))
enemy_image = pygame.image.load('enemy.png')
enemy_image = pygame.transform.scale(enemy_image, (ENEMY_SIZE, ENEMY_SIZE))

# Create character
character_x = 50
character_y = GROUND
character_y_change = 0
character_is_jumping = False

# Create platforms
platforms = []
for y in PLATFORM_Y_POSITIONS:
    platform = pygame.Rect(random.randint(0, SCREEN_WIDTH - PLATFORM_WIDTH), y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
    platforms.append(platform)

# Create enemies
enemies = []
for y in ENEMY_Y_POSITIONS:
    enemy = pygame.Rect(random.randint(0, SCREEN_WIDTH - ENEMY_SIZE), y, ENEMY_SIZE, ENEMY_SIZE)
    enemies.append(enemy)

# Create font
font = pygame.font.Font(None, FONT_SIZE)

# Game loop
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Check for key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= CHARACTER_SPEED
    if keys[pygame.K_RIGHT]:
        character_x += CHARACTER_SPEED
    if keys[pygame.K_SPACE] and not character_is_jumping:
        character_y_change = -JUMP_HEIGHT
        character_is_jumping = True

    # Apply gravity
    character_y_change += GRAVITY
    character_y += character_y_change

    # Check for collisions with platforms
    character_rect = pygame.Rect(character_x, character_y, CHARACTER_SIZE, CHARACTER_SIZE)
    character_is_jumping = True
    for platform in platforms:
        if character_rect.colliderect(platform):
            character_is_jumping = False
            character_y = platform.y - CHARACTER_SIZE
            break
    
    # Check for collisions with enemies
    for enemy in enemies:
        if character_rect.colliderect(enemy):
            game_over = True

    # Check if character has fallen off the screen
    if character_y > SCREEN_HEIGHT:
        game_over = True

    # Move enemies
    for enemy in enemies:
        enemy.x -= ENEMY_SPEED
        if enemy.right < 0:
            enemy.x = SCREEN_WIDTH
            enemy.y = random.choice(ENEMY_Y_POSITIONS)

    # Draw background
    screen.fill((0, 0, 0))

    # Draw character
    screen.blit(character_image, (character_x, character_y))

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, PLATFORM_COLOR, platform)

    # Draw enemies
    for enemy in enemies:
        screen.blit(enemy_image, (enemy.x, enemy.y))

# Draw background
screen.fill((0, 0, 0))

# Draw character
screen.blit(character_image, (character_x, character_y))

# Draw platforms
for platform in platforms:
    pygame.draw.rect(screen, PLATFORM_COLOR, platform)

# Draw enemies
for enemy in enemies:
    screen.blit(enemy_image, (enemy.x, enemy.y))

# Check if game is over
if game_over:
    text = font.render(GAME_OVER_TEXT, True, FONT_COLOR)
    screen.blit(text, (GAME_OVER_X, SCREEN_HEIGHT // 2))
    pygame.display.flip()
    time.sleep(2)  # Add delay before quitting
    pygame.quit()
    sys.exit()

# Update screen
pygame.display.flip()

# Cap the frame rate
time.sleep(0.02)



