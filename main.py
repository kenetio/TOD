import pygame
import sys
from player import Player
from Mumia import mymia
from Yasher import yasher
from test_file import bullet
from blood import blood
import math


pygame.init()


# Константы
WIDTH = 800
HEIGHT = 600
FPS = 60


# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TOD")
clock = pygame.time.Clock()

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

# Спрайты
pygame.mixer.music.load("music.mp3")
player = Player((200, 200))
def room():

    roomimg = pygame.image.load(f"image/комната .png")
    screen.blit(roomimg, (0, 0))


gm = pygame.image.load(f"image/game over.png")

damageimage = pygame.image.load(f"image/урон.png")

walls = [wallrect1, wallrect2, wallrect3, wallrect4]

enemys = []

bloodys = []

u = False
r = False
d = False
l = False


mymy = mymia((500, 500))
mymy1 = mymia((300, 500))
asher = yasher((700, 700))
ashetr = yasher((100, 400))

enemys.append(mymy)
enemys.append(mymy1)
enemys.append(asher)
enemys.append(ashetr)

bullets = []


flag = False

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
        elif i.type == pygame.MOUSEBUTTONDOWN:
            pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            playerDirection = math.degrees(math.atan2(player.rect.y-pos[1], player.rect.x-pos[0]))
            bulle = bullet(player.rect.centerx, player.rect.centery, playerDirection-180)
            bullets.append(bulle)




    # Рендеринг

    room()
    for i in bloodys:
        i.draw(screen)
    for i in bullets:
        i.draw(screen)
    player.draw(screen)
    for i in enemys:
        i.draw(screen)

    pygame.draw.rect(screen, (0, 0, 0),
                     (0, 0, 140, 60))
    pygame.draw.rect(screen, (255, 0, 0),
                     (10, 10, 20+player.hp, 40))
    if damagetime > 0:
        screen.blit(damageimage, (0, 0))
    pygame.display.update()




    # Обновление спрайтов
    player.update(u, d, l, r, walls)
    for i in enemys:
        if i.check():
            bloodik = blood(i.rect.topleft)
            bloodys.append(bloodik)
            enemys.remove(i)
        i.update(player.rect, bullets)
        if i.t == True:
            bullets.pop(i.hit)
        if i.checkolide(player.colliderect) and damagetime < 0:
            if i.type == "mymia":
                player.hp -= 10
            else:
                player.hp -= 5
            print(player.hp)
            flag = True
    for i in bullets:

        if i.check(enemys):
            bullets.remove(i)
        i.update()
    if flag == True:
        damagetime = 100
        flag = False

    if player.hp <= 0:
        running = False

    damagetime -= 1

    # Обновление экрана
running = True
while running:
    # Частота обновления экрана
    clock.tick(FPS)