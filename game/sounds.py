import pygame as pg

def soundsdownloads(notes):
    sounds = {}
    for note in notes:
        path = f"assets/sounds/{note}6.mp3"
        sounds[note] = pg.mixer.Sound(path)
    return sounds
def playnote(note):
    if note in sounds:
        sounds[note].play()