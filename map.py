from random import randint
import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]) -> None:
        super().__init__()
        self.image = pygame.Surface(size=(300, 20))
        self.rect = self.image.get_rect(topleft = pos)


class Map:
    def __init__(self, game_settings: dict) -> None:
        self.start_pos: tuple[int, int] = (0, game_settings['HEIGHT'] - 100)
        self.end_pos: tuple[int, int] = (game_settings['WIDTH'], game_settings['HEIGHT'] - 100)

        # ----------- PLATFORMS ----------- #
        self.platforms: pygame.sprite.Group = pygame.sprite.Group()
        self.create_start_platforms()

        for plat in self.platforms:
            print(plat)
            
    def create_start_platforms(self) -> None:
        x_pos = 0
        y_pos = self.start_pos[1] + 100 # Height
        for i in range(3):
            y_pos -= 300
            x_pos = randint(0, self.end_pos[0] - 300)
            self.platforms.add(Platform(pos=(x_pos, y_pos)))


    def draw(self, screen: pygame.Surface) -> None:
        for plat in self.platforms:
            screen.blit(plat.image, dest=plat.rect)

        pygame.draw.line(screen, 'black', start_pos=self.start_pos, end_pos=self.end_pos, width=10)

    def get_platforms(self) -> pygame.sprite.Group:
        return self.platforms

    