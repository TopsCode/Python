import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_RADIUS = 10
PADDLE_SPEED = 6
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Fonts
FONT = pygame.font.SysFont("comicsans", 30)

# Initialize paddles and ball
player = pygame.Rect(WIDTH - 20, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent = pygame.Rect(5, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_RADIUS * 2, BALL_RADIUS * 2)

ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))

player_score = 0
opponent_score = 0

clock = pygame.time.Clock()

# Main loop
run = True
while run:
    clock.tick(60)
    WIN.fill(BLACK)

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Key controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += PADDLE_SPEED

    # Opponent AI
    if opponent.top < ball.y:
        opponent.y += PADDLE_SPEED - 2
    if opponent.bottom > ball.y:
        opponent.y -= PADDLE_SPEED - 2

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Collision with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Collision with paddles
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    # Scoring
    if ball.left <= 0:
        player_score += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed_x *= random.choice((1, -1))

    if ball.right >= WIDTH:
        opponent_score += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed_x *= random.choice((1, -1))

    # Draw elements
    pygame.draw.rect(WIN, WHITE, player)
    pygame.draw.rect(WIN, WHITE, opponent)
    pygame.draw.ellipse(WIN, WHITE, ball)
    pygame.draw.aaline(WIN, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    player_text = FONT.render(f"Player: {player_score}", True, WHITE)
    opponent_text = FONT.render(f"Opponent: {opponent_score}", True, WHITE)
    WIN.blit(player_text, (WIDTH - 180, 20))
    WIN.blit(opponent_text, (20, 20))

    pygame.display.flip()

pygame.quit()
