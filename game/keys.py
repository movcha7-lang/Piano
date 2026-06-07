import effects
import pygame as pg
def keydrawing(screen, rects, pressedkeys):
    for e,rect in enumerate(rects):
        effects.keydraw(screen, rect, e in pressedkeys)
def createrect(n, startx,starty, width, height):
    rects = []
    for e in range (n):
        x = startx + width * e
        rects.append(pg.Rect(x, starty, width, height))
    return rects