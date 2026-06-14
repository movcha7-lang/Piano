import effects
import pygame as pg
def keydrawing(screen, rects, pressedkeys):
    for e,rect in enumerate(rects):
        effects.keydraw(screen, rect, e in pressedkeys)
def createrect(n, startx = 50,starty = 100, width = 100, height=250):
    rects = []
    for e in range (n):
        x = startx + width * e
        rects.append(pg.Rect(x, starty, width, height))
    return rects