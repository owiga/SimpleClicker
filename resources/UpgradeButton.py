import pygame

from settings import BUTTON_SIZE

class UpgradeButton(pygame.sprite.Sprite):
    def __init__(self, id, price):
        pygame.sprite.Sprite.__init__(self)
        self.source = f"resources/images/{id}.png"
        self.original_image = pygame.Surface(BUTTON_SIZE, pygame.SRCALPHA)
        self.loaded_image = pygame.image.load(self.source).convert_alpha()
        self.original_image = pygame.transform.scale(self.loaded_image, BUTTON_SIZE)
        self.image = self.original_image
        self.rect = self.original_image.get_rect()
        self.price = price
        self.id = id
        self.set_rounded(5)

    def get_id(self):
        return self.id

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def set_rounded(self, roundness):
        size = self.original_image.get_size()
        self.rect_image = pygame.Surface(size, pygame.SRCALPHA)
        pygame.draw.rect(self.rect_image, (255, 255, 255), (0, 0, *size), border_radius=roundness)
        self.image = self.original_image.copy().convert_alpha()
        self.image.blit(self.rect_image, (0, 0), None, pygame.BLEND_RGBA_MIN)
