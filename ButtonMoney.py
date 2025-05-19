import pygame

from settings import IMAGE_SIZE


class ButtonMoney(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.Surface(IMAGE_SIZE, pygame.SRCALPHA)
        pygame.draw.circle(self.original_image, (255, 0, 0), (IMAGE_SIZE[0] // 2, IMAGE_SIZE[1] // 2),
                           IMAGE_SIZE[0] // 2)
        self.image = self.original_image
        self.rect = self.original_image.get_rect()
