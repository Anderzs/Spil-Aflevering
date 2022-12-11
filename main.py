#               Hurtigt spil lavet til Programmering C på 3 moduler samlet
#
#               Start ide: Basis "Infinite jumper" platformer spil med pygame
#                          

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
        player = self.player.sprite
        rect = player.rect

        # ----------- GROUND & WINDOW COLLISIONS ----------- #

        if rect.bottom >= self.map.start_pos[1]:
            rect.bottom = self.map.start_pos[1]
            player.direction.y = 0.8
            player.on_ground = True

        if rect.left <= self.map.start_pos[0]:
            rect.left = self.map.start_pos[0]
        elif rect.right >= self.width:
            rect.right = self.map.end_pos[0]


        # ----------- PLATFORM COLLISIONS ----------- #
        for platform in self.map.get_platforms():
            if platform.rect.colliderect(player.rect) and platform.rect.bottom > player.rect.bottom:
                if player.direction.y > 0:
                    rect.bottom = platform.rect.top
                    player.direction.y = 0
                    player.on_ground = True
        #if pygame.sprite.spritecollide(player, self.map.get_platforms(), dokill=False):
            #if player.direction.y > 0:
                

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            self.screen.fill('white')
            
            self.check_collisions()
            self.player.update()
            self.player.draw(self.screen)

            self.map.draw(self.screen)
            
            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    game = Game()
    game.run()