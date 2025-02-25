# Инициализация Pygame
import pygame
import random
import os
# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Урок Pygame: Простая игра")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Параметры игрока (квадрата)
player_size = 25
player_x, player_y = (100 - player_size / 2), (100 - player_size / 2)
player_speed = 0.1

# Счетчик очков
starting_score = 100
score = starting_score

# Параметры цели (зеленого квадрата)
target_size = 25
if score == starting_score:
    target_x = 700 - target_size / 2
    target_y = 500 - target_size / 2
else:
    target_x = random.randint(0, WIDTH - int(target_size / 2))
    target_y = random.randint(0, HEIGHT - int(target_size / 2))

# Таймер
game_time = 30  # Игра длится 30 секунд
start_ticks = pygame.time.get_ticks()  # Текущее время в начале игры

# Шрифт для текста
font = pygame.font.SysFont('mono', 25)

# Флаг для запуска игры
running = True
while running:
    # Проверяем события (например, выход из игры)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получаем список нажатых клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_y += player_speed

    # Ограничиваем движение игрока в пределах окна
    if player_x < 0:
        player_x = 0
    if player_x > WIDTH - player_size:
        player_x = WIDTH - player_size
    if player_y < 0:
        player_y = 0
    if player_y > HEIGHT - player_size:
        player_y = HEIGHT - player_size

    if abs(player_x - target_x) < player_size and abs(player_y-target_y) < player_size:
        score += 1
        target_x = random.randint(0,WIDTH - int(target_size))
        target_y = random.randint(0,HEIGHT - int(target_size))

    # Очищаем экран
    screen.fill(BLACK)

    # Рисуем игрока и цель
    pygame.draw.rect(screen, GREEN, (target_x, target_y, target_size, target_size))
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_size, player_size))

    # Отображаем счет на экране
    score_text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(score_text, (5, 5))

    # Считаем оставшееся время игры, вычитая прошедшие секунды со старта игры
    seconds = game_time - (pygame.time.get_ticks() - start_ticks) // 1000
    # Создаёт текст с оставшимся временем
    time_text = font.render(f"Time: {seconds}s", True, GREEN)
    # Место показа времени в окне, берёт текст из прошлой строчки кода и ставит его на указанные координаты
    screen.blit(time_text, (5, 35))

    # Проверка, что бы игра не уходила в отрицательные секунды
    if seconds == 0:
        running = False

    # Обновляем экран
    pygame.display.update()

# Score переменная содержит в себе результат игры. Нужно будет записать результат игры в файл. Что бы при каждом завершении
# игры не переписывался этот файл с предыдущими результатами

# Выводим финальный экран
screen.fill(BLACK)
end_text = font.render(f"Игра окончена! Ваши очки: {score}", True, GREEN)
screen.blit(end_text, (WIDTH // 2 - 200, HEIGHT // 2 - 20))
pygame.display.update()

# Ждем несколько секунд перед выходом
pygame.time.wait(1000)

# Завершаем Pygame
pygame.quit()

with open('Score.txt', 'a') as file:
    file.write(str(score) + '\n')