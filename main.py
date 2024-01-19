import pygame
import sys
from player import Player


pygame.init()


# Константы
WIDTH = 800
HEIGHT = 600
FPS = 60


# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TOD")
clock = pygame.time.Clock()


# Спрайты
player = Player((200, 200))



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
    player.draw(screen)
    pygame.display.update()




    # Обновление спрайтов
    player.update(0, 0, 1, 0)



    # Обновление экрана
