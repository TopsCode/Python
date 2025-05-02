import pygame 

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing Shapes")

clock = pygame.time.Clock()
running = True    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("lightblue")  #
    """
    pygame.draw.rect(surface, color, rect)

    surface → where to draw (usually screen)

    color → (R, G, B)

    rect → (x, y, width, height)
    """
    pygame.draw.rect(screen, (255, 215, 215), (100, 100, 150, 80))  # rectangle

        #pygame.draw.circle(surface, color, center, radius)  
    pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50)  # Red circle

    pygame.draw.line(screen, (255, 255, 0), (100, 500), (700, 500), 5)  # Yellow lin
    pygame.display.flip()
    clock.tick(60)

pygame.quit()