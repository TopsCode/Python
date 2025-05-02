import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Move Shape")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Define shape
rect_x, rect_y = 100, 100
rect_width, rect_height = 50, 50
speed = 5

# Game loop
running = True
while running:
    screen.fill(WHITE)  # Clear the screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= speed
    if keys[pygame.K_RIGHT]:
        rect_x += speed
    if keys[pygame.K_UP]:
        rect_y -= speed
    if keys[pygame.K_DOWN]:
        rect_y += speed

    # Clamp the rectangle within the window boundaries
    rect_x = max(0, min(rect_x, width - rect_width))
    rect_y = max(0, min(rect_y, height - rect_height))

    # Draw rectangle
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))

    pygame.display.flip()  # Update the screen
    pygame.time.Clock().tick(60)  # Limit to 60 FPS

pygame.quit()
sys.exit()
