import pygame
import sys

from settings import RESOLUTION, BACKGROUND_COLOR, ID_UPGRADE_COST, BUTTON_SIZE
from resources.ButtonMoney import ButtonMoney
from resources.UpgradeButton import UpgradeButton

pygame.init()
pygame.font.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Colibri", 36)
        self.font_income = pygame.font.SysFont("Colibri", 24)

        self.money = 0
        self.multiplier = 1
        self.base_income = 1
        self.rebirth_multiplier = 1

        self.button = ButtonMoney()
        self.button.rect.center = (RESOLUTION[0] // 2, RESOLUTION[1] // 2)

        self.upgrades_buttons = []
        for i in range(0, 3):
            button = UpgradeButton(i + 1, ID_UPGRADE_COST[str(i + 1)][2])
            button.rect.x = 5
            button.rect.y = 60 * i + 10
            button_text = self.font_income.render(f"Цена: {button.get_price()}", True, (255, 255, 255))
            self.upgrades_buttons.append((button, button_text, i))

        self.balance = self.font.render(f"Баланс: {self.money}", True, (255, 255, 255))
        self.earn = self.font_income.render(
            f"Вы получите: {self.base_income * self.multiplier * self.rebirth_multiplier}", True, (255, 255, 255))


        self.balance_trigger = pygame.USEREVENT + 1
        pygame.time.set_timer(self.balance_trigger, 100)

        self.SpriteGroup = pygame.sprite.Group([self.button, *[x[0] for x in self.upgrades_buttons]])
        pygame.display.set_caption("Clicker")

    def run(self):
        while True:
            self.clock.tick(200)
            self.screen.fill(BACKGROUND_COLOR)
            self.screen.blit(self.balance, (RESOLUTION[0] // 2 - self.balance.get_rect().size[0] // 2, RESOLUTION[1] // 20))
            self.screen.blit(self.earn, (RESOLUTION[0] // 2 - self.earn.get_rect().size[0] // 2, RESOLUTION[1] // 11))
            for button, text, index in self.upgrades_buttons:
                text = self.font_income.render(f"Цена: {button.get_price()}", True, (255, 255, 255))
                self.screen.blit(text, (RESOLUTION[0] // 6, 60 * index + 25))
            self.SpriteGroup.draw(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.button.rect.collidepoint(event.pos):
                        self.money += self.base_income * self.multiplier * self.rebirth_multiplier
                    else:
                        for button in self.upgrades_buttons:
                            if button[0].rect.collidepoint(event.pos):
                                if self.money >= button[0].get_price():
                                    self.money -= button[0].get_price()
                                    if ID_UPGRADE_COST[str(button[0].get_id())][1] == "INC":
                                        self.base_income += ID_UPGRADE_COST[str(button[0].get_id())][0]
                                        button[0].set_price(round(button[0].get_price() * 1.35))
                                    else:
                                        self.multiplier *= ID_UPGRADE_COST[str(button[0].get_id())][0]
                                        button[0].set_price(round(button[0].get_price() * 2.95))


                if event.type == self.balance_trigger:
                    self.balance = self.font.render(f"Баланс: {self.money}", True, (255, 255, 255))
                    self.earn = self.font_income.render(f"Вы получите: {self.base_income * self.multiplier * self.rebirth_multiplier}", True, (255, 255, 255))
            pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()