import pygame as pg
sounds = {}
def soundsdownloads():
    for note in ["c6", "d6", "e6", "f6", "g6", "a6", "b6"]:
        path = f"assets/sounds/{note}.mp3"
        sounds[note] = pg.mixer.Sound(path)
def playnote(note):
    if note in sounds:
        sounds[note].play()