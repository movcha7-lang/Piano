import pygame as pg

class Slider():
    def __init__(self, x, y, w, minimum, maximum):
        self.rect = pg.Rect(x,y,w,6)
        self.min = float(minimum)
        self.max = float(maximum)
        self.step = 1
    def bordercheck(self, p):
        ...
        