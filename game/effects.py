import pygame as pg
def keydraw(screen, rectangle, ispressed):
    if ispressed:
        bgcolor= (170, 220, 255)
    else:
        bgcolor = (220, 220, 220)
    pg.draw.rect(screen, bgcolor, rectangle, border_radius = 8)
    pg.draw.rect(screen, (0,0,0), rectangle,2, border_radius = 8)