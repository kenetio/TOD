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
roomimg = pygame.image.load(f"image/комната .png")

u = False
r = False
d = False
l = False

temple = [[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0]]

print(temple)

running = True
while running:
    # Частота обновления экрана
    clock.tick(FPS)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_a:
                l = True
            elif i.key == pygame.K_d:
                r = True
            elif i.key == pygame.K_w:
                d = True
            elif i.key == pygame.K_s:
                u = True
        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_a:
                l = False
            elif i.key == pygame.K_d:
                r = False
            elif i.key == pygame.K_w:
                d = False
            elif i.key == pygame.K_s:
                u = False



    # Рендеринг
    screen.blit(roomimg, (0, 0))
    player.draw(screen)
    pygame.display.update()




    # Обновление спрайтов
    player.update(u, d, l, r)



    # Обновление экрана
