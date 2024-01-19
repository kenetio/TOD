import pygame.sprite


class Tile(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__()
        self.image = pygame.image.load(f"images/tiles/Tile2.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = coords
        self.xvel = 0
        self.yvel = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, rectplayer):
        if rectplayer.y:
            self.xvel -= 1
        if right:
            self.xvel += 1
        if forward:
            self.yvel += 1
        if back:
            self.yvel -= 1