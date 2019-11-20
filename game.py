from enum import Enum
import pygame as pygrame
import sys
pygrame.init()

class Ground:
    def __init__(self, color, rect):
        self.color = color
        self.rect = rect

    def draw(self, surface):
        pygrame.draw.rect(surface, self.color, self.rect)

def game_loop():
    screen = pygrame.display.set_mode((500, 400))
    ground = Ground(pygrame.Color(228, 59, 59), pygrame.Rect(50, 250, 400, 100))
    while True:
        for event in pygrame.event.get():
            if event.type is pygrame.QUIT:
                sys.exit()
        ground.draw(screen)
        pygrame.display.flip()

def main():
    game_loop()

if __name__== "__main__":
  main()
