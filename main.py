import random
import pygame
from shared.color import Color
import ball
import paddle
import tile
import time


class Game:
    width = 700
    height = 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Breaker')
    clock = pygame.time.Clock()
    fps = 60

    @staticmethod
    def play():
        pygame.mouse.set_visible(False)
        pygame.init()
        font = pygame.font.Font('assets/fonts/arial.ttf', 18)

        user = paddle.Paddle()
        bl = ball.Ball(user)
        tiles = []

        # i == y , j == x
        for i in range(2, (tile.Tile.height + 2) * 7, tile.Tile.height + 2):
            for j in range(4, (tile.Tile.width + 4) * 13, tile.Tile.width + 4):
                tiles.append(tile.Tile(j, i))

        while True:

            Game.screen.fill(Color.black)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    user.move(pygame.mouse.get_pos()[0])
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    exit()

            if user.life == 0 or user.score == len(tiles):
                bl = None
            else:
                bl.show()
                if bl.move(user, tiles) == False:
                    bl = ball.Ball(user)
            user.show()
            for _tile in tiles:
                _tile.show()

            score = font.render(f'Score: {user.score}', True, Color.white)
            score_box = score.get_rect(center=(Game.width / 4, Game.height / 2))

            life = font.render(f'Balls: {user.life}', True, Color.white)
            cpu_box = life.get_rect(center=(Game.width * 0.75, Game.height / 2))

            Game.screen.blit(score, score_box)
            Game.screen.blit(life, cpu_box)
            pygame.display.update()
            Game.clock.tick(Game.fps)


def main():
    Game.play()


if __name__ == "__main__":
    main()
