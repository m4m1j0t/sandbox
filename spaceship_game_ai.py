import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Загрузка картинки котика
cat_image = pygame.image.load('image_for_game.jpg')
cat_image = pygame.transform.scale(cat_image, (50, 50)) # Изменение размера картинки, если необходимо

# Начальные координаты котика
cat_x = screen_width / 2
cat_y = screen_height / 2

# Скорость движения котика
speed = 5

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        cat_y -= speed
    if keys[pygame.K_DOWN]:
        cat_y += speed
    if keys[pygame.K_LEFT]:
        cat_x -= speed
    if keys[pygame.K_RIGHT]:
        cat_x += speed

    # Проверка границ экрана
    if cat_x < 0:
        cat_x = 0
    elif cat_x > screen_width - cat_image.get_width():
        cat_x = screen_width - cat_image.get_width()
    if cat_y < 0:
        cat_y = 0
    elif cat_y > screen_height - cat_image.get_height():
        cat_y = screen_height - cat_image.get_height()

    # Очистка экрана и рисование котика
    screen.fill((0, 0, 0)) # Заливка экрана черным цветом
    screen.blit(cat_image, (cat_x, cat_y))

    # Обновление экрана
    pygame.display.flip()
    pygame.time.Clock().tick(60)