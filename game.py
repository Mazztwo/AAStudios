import pygame as pygrame
import sys
pygrame.init()

def game_loop():
    screen = pygrame.display.set_mode((500, 400))
    while True:
        for event in pygrame.event.get():
            if event.type is pygrame.QUIT:
                sys.exit()

def main():
    game_loop()

if __name__== "__main__":
  main()
