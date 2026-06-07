import pygame as pg
class Button: 
    def __init__(self, x, y, w, h, text, action = None):
        self.rect = pg.Rect(x, y, w,h)
        self.action = action
        self.text = text
        self.color_idle = (220, 220, 220)
        self.color_hover = (180, 180, 180)
        self.text_color = (0,0,0)
    def draw(self, screen, font):
        mouse_position = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_position):
            color = self.color_hover
        else:
            color = self.color_idle
        pg.draw.rect(screen, color, self.rect)
        pg.draw.rect(screen, (0,0,0), self.rect,2)
        text = font.render(self.text, True, self.text_color)
        recttext = text.get_rect(center = self.rect.center)
        screen.blit(text, recttext)
    def handle_events(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and self.action:
                self.action()