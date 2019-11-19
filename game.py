import pygame as pygrame
import sys
pygrame.init()

screen = pygrame.display.set_mode((500, 400))

while True:
    for event in pygrame.event.get():
        if event.type is pygrame.QUIT:
            sys.exit()