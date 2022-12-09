import pygame

class Map:
    def __init__(self, game_settings: dict) -> None:
        self.start_pos: tuple[int, int] = (0, game_settings['HEIGHT'] - 100)
        self.end_pos: tuple[int, int] = (game_settings['WIDTH'], game_settings['HEIGHT'] - 100)


    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.line(screen, 'black', start_pos=self.start_pos, end_pos=self.end_pos, width=10)