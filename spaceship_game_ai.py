import pygame
import sys

# Инициализируем Pygame
pygame.init()

# Задаем размеры окна
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Задаем название окна
pygame.display.set_caption("Космический корабль")

# Задаем цвета
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Задаем классы для кораблей
class Spaceship(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50)
        self.speed = 5

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed

class Enemy(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50)
        self.speed = 2

    def move(self):
        self.y += self.speed

# Создаем корабль игрока
player = Spaceship(100, 100)

# Создаем список вражеских кораблей
enemies = [Enemy(200, 0), Enemy(400, 0)]

# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Движение корабля игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-1, 0)
    if keys[pygame.K_RIGHT]:
        player.move(1, 0)
    if keys[pygame.K_UP]:
        player.move(0, -1)
    if keys[pygame.K_DOWN]:
        player.move(0, 1)

    # Движение вражеских кораблей
    for enemy in enemies:
        enemy.move()
        if enemy.y > screen_height:
            enemy.y = 0

    # Проверяем столкновения
    for enemy in enemies:
        if player.colliderect(enemy):
            print("Игрок столкнулся с вражеским кораблем!")
            pygame.quit()
            sys.exit()

    # Рисуем все
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, green, player)
    for enemy in enemies:
        pygame.draw.rect(screen, red, enemy)
    pygame.display.flip()

    # Ограничиваем частоту кадров
    pygame.time.Clock().tick(60)