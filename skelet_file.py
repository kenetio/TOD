import pygame

class skelet(pygame.sprite.sprite):
    def __init__(self):
        super().__init__()

        self.image('image/Скелетончик.png')
        self.original_image('image/Скелетончик.png')
