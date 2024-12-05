import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Цвета
bg_color = (128, 0, 128)  # Сиреневый
paddle1_color = (0, 0, 255)  # Синий
paddle2_color = (255, 105, 180)  # Розовый
ball_color = (255, 0, 0)  # Красный
text_color = (255, 255, 255)  # Белый

# Ракетки
paddle1 = pygame.Rect(10, screen_height / 2 - 50, 10, 100)
paddle2 = pygame.Rect(screen_width - 20, screen_height / 2 - 50, 10, 100)

# Мяч
ball = pygame.Rect(screen_width / 2, screen_height / 2, 10, 10)
ball_speed = [3, 3]  # Уменьшена скорость мяча

# Движение ракеток
paddle_speed = 5

# Пауза
paused = False

# Счёт
score1 = 0
score2 = 0

# Имена игроков
player1_name = "Папа"
player2_name = "Ярослава"

# Основной цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

    keys = pygame.key.get_pressed()
    if not paused:
        if keys[pygame.K_w]:
            paddle1.y -= paddle_speed
        if keys[pygame.K_s]:
            paddle1.y += paddle_speed
        if keys[pygame.K_a]:
            paddle1.x -= paddle_speed
        if keys[pygame.K_d]:
            paddle1.x += paddle_speed

        if keys[pygame.K_UP]:
            paddle2.y -= paddle_speed
        if keys[pygame.K_DOWN]:
            paddle2.y += paddle_speed
        if keys[pygame.K_LEFT]:
            paddle2.x -= paddle_speed
        if keys[pygame.K_RIGHT]:
            paddle2.x += paddle_speed

        # Ограничение движения ракеток
        if paddle1.x < 0:
            paddle1.x = 0
        elif paddle1.x > screen_width / 2 - paddle1.width:
            paddle1.x = screen_width / 2 - paddle1.width

        if paddle2.x < screen_width / 2:
            paddle2.x = screen_width / 2
        elif paddle2.x > screen_width - paddle2.width:
            paddle2.x = screen_width - paddle2.width

        # Движение мяча
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        # Отскок от краев
        if ball.y < 0 or ball.y > screen_height - ball.height:
            ball_speed[1] *= -1
        if ball.x < 0:
            score2 += 1
            ball.x = screen_width / 2
            ball.y = screen_height / 2
        elif ball.x > screen_width - ball.width:
            score1 += 1
            ball.x = screen_width / 2
            ball.y = screen_height / 2

        # Отскок от ракеток
        if ball.colliderect(paddle1):
            ball_speed[0] = abs(ball_speed[0])  # Мяч отскакивает вправо
        elif ball.colliderect(paddle2):
            ball_speed[0] = -abs(ball_speed[0])  # Мяч отскакивает влево

        # Проверка победителя
        if score1 >= 7:
            print(f"Победитель: {player1_name}!")
            pygame.quit()
            sys.exit()
        elif score2 >= 7:
            print(f"Победитель: {player2_name}!")
            pygame.quit()
            sys.exit()

    # Отрисовка
    screen.fill(bg_color)
    pygame.draw.rect(screen, paddle1_color, paddle1)
    pygame.draw.rect(screen, paddle2_color, paddle2)
    pygame.draw.ellipse(screen, ball_color, ball)  # Мяч стал круглым
    pygame.draw.aaline(screen, (255, 255, 255), (screen_width / 2, 0), (screen_width / 2, screen_height))

    # Вывод счёта
    font = pygame.font.Font(None, 36)
    text = font.render(f"{player1_name}: {score1} - {player2_name}: {score2}", True, text_color)
    screen.blit(text, (screen_width / 2 - text.get_width() / 2, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(60)