import pygame
import sys

from config import ConfigHandler
from map import Map
from player import Player

class Game:
    def __init__(self) -> None:
        # ----------- CONFIG ----------- #
        self.config = ConfigHandler("config.json")
        self.game_data = self.config.get_data("GAME_DATA")

        # ----------- GAME & WINDOW SETTINGS ----------- #
        self.clock = pygame.time.Clock()
        self.width, self.height = self.game_data['WIDTH'], self.game_data['HEIGHT']
        self.fps = self.game_data['FPS']
        self.screen = pygame.display.set_mode((self.width, self.height))

        # ----------- GAME & WINDOW SETTINGS ----------- #
        self.map = Map(self.game_data)

        # ----------- PLAYER ----------- #
        player_data = self.config.get_data("PLAYER_DATA")
        self.player = pygame.sprite.GroupSingle(Player(player_data))

    def check_collisions(self) -> None:
        # Check ground collision
        if (self.player.sprite.rect.x <= self.map.start_pos[0]):
            self.player.sprite.rect.x = self.map.start_pos[0]


    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            self.screen.fill('white')
            
            self.player.update()
            self.player.draw(self.screen)

            self.map.draw(self.screen)
            self.check_collisions()
            
            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    game = Game()
    game.run()