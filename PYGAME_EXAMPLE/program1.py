import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My First Pygame Program")

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (RGB)
    screen.fill((0, 128, 255))  # Light blue background

    # Update the display
    pygame.display.flip()  # update entire screen 

# Quit Pygame
pygame.quit()
sys.exit()
