import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, player_data: dict, set_game_status) -> None:
        super().__init__()
        self.image: pygame.Surface = pygame.Surface(size=(player_data['WIDTH'],
                                            player_data['HEIGHT']))
        self.rect: pygame.Rect = self.image.get_rect(topleft = player_data['SPAWN_POS'])

        # ----------- PLAYER STATS ----------- #
        self.speed: int = player_data['SPEED']
        self.gravity: float = player_data['GRAVITY']
        self.jump_speed: int = player_data['JUMP_SPEED']
        self.direction: pygame.Vector2 = pygame.math.Vector2()

        # ----------- GAME STATUS FUNCTION ----------- #
        self.set_game_status = set_game_status

        # ----------- MOVEMENT & COLLISION ----------- #
        self.on_ground: bool = True 

    def input(self) -> None:
        key = pygame.key.get_pressed()
        if (key[pygame.K_UP] or key[pygame.K_w] or key[pygame.K_SPACE]) and self.on_ground:
            self.direction.y = self.jump_speed
            self.on_ground = False
            self.set_game_status('running')

        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.direction.x = -1
        elif key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def apply_gravity(self) -> None:
        if self.direction.y >= 40:
            self.set_game_status('lost')
        self.direction.y += self.gravity
        
        self.rect.y += self.direction.y

    def update(self) -> None:
        self.input()
        self.apply_gravity()
        self.rect.x += self.direction.x * self.speed
        
