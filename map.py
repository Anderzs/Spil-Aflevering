from random import randint
import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]) -> None:
        super().__init__()
        self.image = pygame.Surface(size=(300, 20))
        self.rect = self.image.get_rect(topleft = pos)

class Map:
    def __init__(self, game_settings: dict, add_function) -> None:
        self.start_pos: tuple[int, int] = (0, game_settings['HEIGHT'] - 100)
        self.end_pos: tuple[int, int] = (game_settings['WIDTH'], game_settings['HEIGHT'] - 100)

        self.add_function = add_function

        # ----------- TRACKING VARIABLES ----------- #
        self.y_pos: int = self.start_pos[1] + 100 # Height

        # ----------- PLATFORMS ----------- #
        self.platforms: pygame.sprite.Group = pygame.sprite.Group()
        self.create_start_platforms()
            
    def create_start_platforms(self) -> None:
        for i in range(3):
            self.create_platform()
            

    def create_platform(self) -> None:
        x_pos = randint(0, self.end_pos[0] - 300)
        self.y_pos -= 300
        self.platforms.add(Platform(pos=(x_pos, self.y_pos)))
        self.add_function(Platform(pos=(x_pos, self.y_pos)))

    def draw_ground(self, screen: pygame.Surface) -> None:
        pygame.draw.line(screen, 'black', start_pos=self.start_pos, end_pos=self.end_pos, width=10)

    def get_platforms(self) -> pygame.sprite.Group:
        return self.platforms

    