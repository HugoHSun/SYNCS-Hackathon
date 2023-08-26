import pygame
import random

# Initialize Pygame
pygame.init()

# Set up game window
width, height = 640, 480
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Paddle and ball properties
paddle_width, paddle_height = 15, 100
ball_size = 20
ball_speed_x = 5
ball_speed_y = 5

# Paddle positions
player_y = height // 2 - paddle_height // 2
opponent_y = height // 2 - paddle_height // 2

# Ball position
ball_x = width // 2 - ball_size // 2
ball_y = height // 2 - ball_size // 2

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= 5
    if keys[pygame.K_DOWN] and player_y < height - paddle_height:
        player_y += 5

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collisions
    if ball_y <= 0 or ball_y >= height - ball_size:
        ball_speed_y *= -1

    if ball_x <= 0 or ball_x >= width - ball_size:
        ball_speed_x *= -1

    if (ball_y > (player_y + paddle_height/2) and ball_x <= paddle_width) or (ball_y < (player_y - paddle_height/2) and ball_x <= paddle_width)  :
        print("hi")

    # Drawing
    win.fill(black)
    pygame.draw.rect(win, white, (0, player_y, paddle_width, paddle_height))
    pygame.draw.rect(win, white, (width - paddle_width, opponent_y, paddle_width, paddle_height))
    pygame.draw.ellipse(win, white, (ball_x, ball_y, ball_size, ball_size))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
