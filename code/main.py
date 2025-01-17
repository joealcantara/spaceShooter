# Currently on 42:23

import pygame
import random
import os

os.chdir('/Users/joe/Documents/spaceShooter/')

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True

# plain surface
surf = pygame.Surface((100, 200))
surf.fill('orange')
x = 100

# importing an image
player_surf = pygame.image.load('images/player.png').convert_alpha()

# place 20 stars
star_surf = pygame.image.load('images/star.png').convert_alpha()
star_positions = [(random.randint(1, WINDOW_WIDTH), random.randint(1, WINDOW_HEIGHT)) for i in range(20)]

while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the game
    x += 0.1
    display_surface.fill('dark grey')
    
    for star in star_positions:
        display_surface.blit(star_surf, star)
    display_surface.blit(player_surf, (x, 250))
    pygame.display.update()

pygame.quit()