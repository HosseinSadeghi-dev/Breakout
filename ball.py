import pygame
import main
import random
from shared.color import Color


class Ball:
    def __init__(self, paddle):
        self.r = 5
        self.x = random.randint(paddle.x, paddle.x + paddle.w / 2)
        self.y = paddle.y - paddle.h
        self.speed = 4
        self.color = Color.white

        self.dir_x = random.choice([-1, 1])
        self.dir_y = round(random.uniform(-1, -0.5), 1)

    def show(self):
        pygame.draw.circle(main.Game.screen, self.color, [self.x, self.y], self.r)

    def move(self, paddle, tiles):
        ball_rect = pygame.Rect(self.x + self.r, self.y + self.r, self.r, self.r)
        paddle_x_origin = paddle.x + paddle.w / 2
        paddle_y_origin = paddle.y + paddle.h / 2
        print(paddle_y_origin)
        print(paddle.y)

        # hit side walls
        if not (0 < self.x < main.Game.width):
            self.dir_x *= -1
        elif self.y < 0:
            self.dir_y *= -1
        elif self.y > main.Game.height:
            paddle.life -= 1
            return False

        # hit paddle
        elif ball_rect.colliderect(pygame.Rect(paddle_x_origin, paddle_y_origin, paddle.w, paddle.h)):
            # ball come from right of paddle
            if self.x - paddle_x_origin >= 0:
                # hit right of paddle
                if paddle_x_origin + paddle.w / 4 <= self.x <= paddle_x_origin + paddle.w / 2:
                    self.dir_y *= -1
                    self.dir_x *= -1
                else:
                    self.dir_y *= -1
            # ball come from left of paddle
            elif self.x - paddle_x_origin < 0:
                # hit left of paddle
                if paddle_x_origin - paddle.w / 2 <= self.x <= paddle_x_origin - paddle.w / 4:
                    self.dir_y *= -1
                    self.dir_x *= -1
                # hit center of paddle
                else:
                    self.dir_y *= -1

        for tile in tiles:
            tile_x_origin = tile.x + tile.w / 2
            tile_y_origin = tile.y + tile.h / 2

            if ball_rect.colliderect(pygame.Rect(tile_x_origin, tile_y_origin, tile.w, tile.h)):
                # ball come from right of tile
                if self.x - tile_x_origin >= 0:
                    # hit right of tile
                    if tile_x_origin + tile.w / 4 <= self.x <= tile_x_origin + tile.w / 2:
                        self.dir_y *= -1
                        self.dir_x *= -1
                    else:
                        self.dir_y *= -1
                # ball come from left of tile
                elif self.x - tile_x_origin < 0:
                    # hit left of tile
                    if tile_x_origin - tile.w / 2 <= self.x <= tile_x_origin - tile.w / 4:
                        self.dir_y *= -1
                        self.dir_x *= -1
                    # hit center of tile
                    else:
                        self.dir_y *= -1
                paddle.score += 1
                tiles.remove(tile)

        self.y += self.dir_y * self.speed
        self.x += self.dir_x * self.speed

    def check_hit(self, tile):
        pass
