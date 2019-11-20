from enum import Enum
import pygame as pygrame
import sys
pygrame.init()

colors = {
    "BLACK" : pygrame.Color(0, 0, 0),
    "RED"   : pygrame.Color(228, 59, 59),
    "BLUE"  : pygrame.Color(81, 72, 208),
    "GREEN" : pygrame.Color(48, 139, 57)
}

class Fighter:
    def __init__(self, color, rect):
        self.color = color
        self.rect = rect

    def draw(self, surface):
        pygrame.draw.rect(surface, self.color, self.rect)

class Ground:
    def __init__(self, color, rect):
        self.color = color
        self.rect = rect

    def draw(self, surface):
        pygrame.draw.rect(surface, self.color, self.rect)

def game_loop():
    screen = pygrame.display.set_mode((500, 400))
    clock = pygrame.time.Clock()

    ground = Ground(colors["RED"], pygrame.Rect(50, 250, 400, 100))
    fighter1 = Fighter(colors["BLUE"], pygrame.Rect(60, 210, 25, 40))
    fighter2 = Fighter(colors["GREEN"], pygrame.Rect(400, 210, 25, 40))
    while True:
        clock.tick(60)
        for event in pygrame.event.get():
            if event.type is pygrame.QUIT:
                sys.exit()

        # TODO: Optimize so that we clear only a portion of the screen
        # rather than the entire screen.
        screen.fill(colors["BLACK"])
        fighter1.draw(screen)
        fighter2.draw(screen)
        ground.draw(screen)
        pygrame.display.flip()

def main():
    game_loop()

if __name__== "__main__":
  main()
