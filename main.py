import pygame
import sys
from player import Player
from Mumia import mymia
from Yasher import Yasher


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
pygame.mixer.music.load("music.mp3")

wall1 = pygame.image.load(f"image/Walls/Wall1.png")
wallrect1 = wall1.get_rect()
wallrect1.topleft = (0,0)
wall2 = pygame.image.load(f"image/Walls/Wall2.png")
wallrect2 = wall2.get_rect()
wallrect2.topleft = (0,0)
wall3 = pygame.image.load(f"image/Walls/Wall3.png")
wallrect3 = wall3.get_rect()
wallrect3.topleft = (778,0)
wall4 = pygame.image.load(f"image/Walls/Wall4.png")
wallrect4 = wall4.get_rect()
wallrect4.topleft = (0,577)

damageimage = pygame.image.load(f"image/урон.png")

walls = [wallrect1, wallrect2, wallrect3, wallrect4]


u = False
r = False
d = False
l = False

temple = [[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,3,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0]]
mymy = mymia(500, 500)
yasher = Yasher(300, 300)

for i in temple:
    pass

for i in temple:
    print(*i)

damagetime = 0
pygame.mixer.music.play(-1)
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
    mymy.draw(screen)
    yasher.draw(screen)
    if damagetime > 0:
        screen.blit(damageimage, (0, 0))
    pygame.display.update()




    # Обновление спрайтовw
    player.update(u, d, l, r, walls)
    mymy.update(player.rect)
    if mymy.checkolide(player.colliderect) and damagetime < 0:
        player.hp -= 10
        print(player.hp)
        damagetime = 100

    yasher.update(player.rect)
    if yasher.checkolide(player.colliderect) and damagetime < 0:
        player.hp -= 5
        print(player.hp)
        damagetime = 100

    damagetime -= 1

    # Обновление экрана
