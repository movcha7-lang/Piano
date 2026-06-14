import pygame as pg
import settings 
import sounds
import keys
import buttons 

pg.init()
screen = pg.display.set_mode((settings.WINDOWWIDTH, settings.WINDOWHEIGHT))
pg.display.set_caption("Piano")
sounds = sounds.soundsdownloads(settings.SOUNDS)
keyrects = keys.createrect(len(settings.SOUNDS))
keyslist = list(settings.SOUNDS.keys())
font = pg.font.SysFont("Areal", 24)
pressedkeys = set()

def startgame():
    ...

def opensettings():
    ...


def exitgame():
    pg.quit()


buttons = [buttons.Button(60,20,120,40, "SETTINGS",opensettings)]

running = True
while running == True:
    screen.fill(settings.WHITE)
    for button in buttons:
        button.draw(screen,font)
    keys.keydrawing(screen,keyrects,pressedkeys)
    pg.display.flip()
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False
        for button in buttons:
            button.handle_events(e)
        if e.type == pg.KEYDOWN:
            k = pg.key.name(e.key)
            if k in sounds:
                sounds[k].play()
                indx = keyslist.index(k)
                pressedkeys.add(indx)
        if e.type == pg.KEYUP:
            k = pg.key.name(e.key)
            if k in sounds:
                indx = keyslist.index(k)
                if indx in pressedkeys:
                    pressedkeys.remove(indx)

