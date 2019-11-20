from enum import Enum
import pygame as pg
import sys
pg.init()

colors = {
    "BLACK" : pg.Color(0, 0, 0),
    "RED"   : pg.Color(228, 59, 59),
    "BLUE"  : pg.Color(81, 72, 208),
    "GREEN" : pg.Color(48, 139, 57)
}

class Fighter:
    def __init__(self, color, rect):
        self.color = color
        self.rect = rect

    def draw(self, surface):
        pg.draw.rect(surface, self.color, self.rect)

class Ground:
    def __init__(self, color, rect):
        self.color = color
        self.rect = rect

    def draw(self, surface):
        pg.draw.rect(surface, self.color, self.rect)

def game_loop():
    screen = pg.display.set_mode((500, 400))
    clock = pg.time.Clock()

    ground = Ground(colors["RED"], pg.Rect(50, 250, 400, 100))
    fighter1 = Fighter(colors["BLUE"], pg.Rect(60, 210, 25, 40))
    fighter2 = Fighter(colors["GREEN"], pg.Rect(400, 210, 25, 40))
    while True:
        clock.tick(60)
        for event in pg.event.get():
            if event.type is pg.QUIT:
                sys.exit()

        # TODO: Optimize so that we clear only a portion of the screen
        # rather than the entire screen.
        screen.fill(colors["BLACK"])
        fighter1.draw(screen)
        fighter2.draw(screen)
        ground.draw(screen)
        pg.display.flip()

def main():
    game_loop()

if __name__== "__main__":
  main()
