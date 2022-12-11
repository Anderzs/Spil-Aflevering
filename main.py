#               Hurtigt spil lavet til Programmering C på 3 moduler samlet
#
#               Start ide: Basis "Infinite jumper" platformer spil med pygame
#                          

import pygame
import sys

from config import ConfigHandler
from map import Map, Platform
from player import Player

class Game:
    def __init__(self) -> None:
        # ----------- CONFIG ----------- #
        pygame.init()

        self.config: ConfigHandler = ConfigHandler("config.json")
        self.game_data: dict = self.config.get_data("GAME_DATA")
        self.font = pygame.font.SysFont("American Typewriter", 64)

        # ----------- GAME & WINDOW SETTINGS ----------- #
        self.game_status: str = 'waiting'

        # ----------- GAME & WINDOW SETTINGS ----------- #
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.width, self.height = self.game_data['WIDTH'], self.game_data['HEIGHT']
        self.fps: int = self.game_data['FPS']
        self.screen: pygame.Surface = pygame.display.set_mode((self.width, self.height))

        # ----------- CAMERA ----------- #
        self.camera: CameraBox = CameraBox(self.config.get_data("CAMERA_BORDERS"))

        # ----------- GAME & WINDOW SETTINGS ----------- #
        self.map: Map = Map(self.game_data, self.add_to_camera)

        # ----------- PLAYER ----------- #
        player_data: dict = self.config.get_data("PLAYER_DATA")
        self.player: pygame.sprite.GroupSingle = pygame.sprite.GroupSingle(Player(player_data, self.set_game_status))
        self.camera.add(self.player.sprite)

    def set_game_status(self, status: str) -> None:
        self.game_status = status.lower()
        
    def add_to_camera(self, sprite: pygame.sprite.Sprite) -> None:
        self.camera.add(sprite)

    def check_collisions(self) -> None:
        # Check ground collision
        player = self.player.sprite
        rect = player.rect

        # ----------- GROUND & WINDOW COLLISIONS ----------- #

        if rect.bottom >= self.map.start_pos[1] and self.game_status == 'waiting':
            rect.bottom = self.map.start_pos[1]
            player.direction.y = 0.8
            player.on_ground = True
        elif rect.top > self.map.start_pos[1]:
            self.set_game_status('lost')

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
                


    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                    
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            self.screen.fill('white')
            
            if self.game_status != 'lost':
                self.check_collisions()

                self.camera.update()
                self.camera.custom_draw(self.screen, target=self.player.sprite)
            elif self.game_status == 'lost':
                text = self.font.render('Du tabte!', True, 'black', 'white')
                text_rect = text.get_rect()
                text_rect.center = (self.width // 2, self.height // 2)
                self.screen.blit(text, text_rect)

            if self.game_status == 'waiting':
                self.map.draw_ground(self.screen)
            
            pygame.display.update()
            self.clock.tick(self.fps)


class CameraBox(pygame.sprite.Group):
    """Camera Box"""
    def __init__(self, camera_borders: dict) -> None:
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.camera_borders = camera_borders


    def custom_draw(self, screen: pygame.Surface, target: pygame.sprite.Sprite) -> None:
        if target.rect.top < self.camera_borders['TOP']:
            self.offset.y = -(self.camera_borders['TOP'] - target.rect.centery)

        for sprite in self.sprites():
            offset_rect = sprite.rect.copy()
            offset_rect.center -= self.offset
            screen.blit(sprite.image, offset_rect)


if __name__ == "__main__":
    game = Game()
    game.run()