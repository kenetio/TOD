import pygame.sprite


class Tile(pygame.sprite.Sprite):
    def __init__(self, coords, ):
        super().__init__()
        self.image = pygame.image.load(f"image/Игрок с пистолетомxdxd.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = coords

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, u, d, l, r):
        if u:
            self.rect.y += 3
        if d:
            self.rect.y -= 3
        if l:
            self.rect.x -= 3
        if r:
            self.rect.x += 3
