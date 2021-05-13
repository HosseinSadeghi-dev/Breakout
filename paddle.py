import random
import pygame.draw
import main
from shared.color import Color


class Paddle:
    def __init__(self):
        self.w = 60
        self.h = 5
        self.life = 3
        self.score = 0

        self.x = random.randint(self.w, main.Game.width - self.w)
        self.y = main.Game.height - self.h
        self.color = Color.white

    def show(self):
        pygame.draw.rect(main.Game.screen, self.color, [self.x, self.y, self.w, self.h])

    def move(self, new_x):
        self.x = new_x
        if self.x + self.w > main.Game.width:
            self.x = main.Game.width - self.w
