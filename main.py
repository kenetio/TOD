import pygame
import sys


pygame.init()


# Константы
WIDTH = 700
HEIGHT = 500
FPS = 60


# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Chrome")
clock = pygame.time.Clock()


# Спрайты




running = True
while running:
    # Частота обновления экрана
    clock.tick(FPS)


    # События/Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Рендеринг




    # Обновление спрайтов




    # Обновление экрана
