import pygame.sprite


class Tile(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__()
        self.image = pygame.image.load(f"images/tiles/Tile2.png")
        self.image = pygame.transform.scale(self.image,
                                                (self.image.get_width() * 5, self.image.get_height() * 5))
        self.rect = self.image.get_rect()
        self.rect.topleft = coords

    def draw(self, surface):
        surface.blit(self.image, self.rect)