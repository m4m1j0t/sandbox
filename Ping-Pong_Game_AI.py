import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Настройка экрана
screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Настройка ракеток и мяча
paddle_width = 10
paddle_height = 100
ball_size = 10

paddle1 = pygame.Rect(0, 0, paddle_width, paddle_height)
paddle1.y = screen_height / 2 - paddle1.height / 2

paddle2 = pygame.Rect(0, 0, paddle_width, paddle_height)
paddle2.x = screen_width - paddle2.width
paddle2.y = screen_height / 2 - paddle2.height / 2

ball = pygame.Rect(0, 0, ball_size, ball_size)
ball.x = screen_width / 2 - ball.width / 2
ball.y = screen_height / 2 - ball.height / 2

ball_speed_x = random.choice([-5, 5])
ball_speed_y = random.choice([-5, 5])

# Цвета
white = (255, 255, 255)

# Основной цикл
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Движение ракеток
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.y -= 5
    if keys[pygame.K_s]:
        paddle1.y += 5
    if keys[pygame.K_UP]:
        paddle2.y -= 5
    if keys[pygame.K_DOWN]:
        paddle2.y += 5

    # Движение мяча
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Столкновения с ракетками и стенками
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1
    if ball.y < 0 or ball.y > screen_height - ball.height:
        ball_speed_y *= -1
    if ball.x < 0:
        ball.x = screen_width / 2 - ball.width / 2
        ball.y = screen_height / 2 - ball.height / 2
    if ball.x > screen_width - ball.width:
        ball.x = screen_width / 2 - ball.width / 2
        ball.y = screen_height / 2 - ball.height / 2

    # Рисование объектов
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, white, paddle1)
    pygame.draw.rect(screen, white, paddle2)
    pygame.draw.rect(screen, white, ball)
    pygame.draw.line(screen, white, (screen_width / 2, 0), (screen_width / 2, screen_height), 1)

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)