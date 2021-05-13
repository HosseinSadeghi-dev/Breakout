import random
import pygame.draw
import main
from shared.color import Color


class Tile:
    width = 50
    height = 10

    def __init__(self, x, y):
        self.w = Tile.width
        self.h = Tile.height
        self.score = 0

        self.x = x
        self.y = y
        colors = [Color.red, Color.blue, Color.yellow, Color.silver, Color.green, Color.orange]
        self.color = random.choice(colors)

    def show(self):
        pygame.draw.rect(main.Game.screen, self.color, [self.x, self.y, self.w, self.h])

    def get_hit(self):
        del self
