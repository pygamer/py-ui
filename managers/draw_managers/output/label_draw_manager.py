from constructs.output.label import Label
import pygame

class LabelDrawManager(Label):

    def __init__(self, color=(0, 0, 0), angle=0, antialias=True, background_color=None, text="", uifont=None):
        Label.__init__(self)
        self.text = text
        self.uifont = uifont
        self.rect = pygame.Rect(self.get_real_origin(), self.uifont.font.size(self.text))
        self.color = color
        self.angle = angle
        self.antialias = antialias
        self.background_color = background_color
        self.build()

    def build(self):
        self.surface = self.uifont.font.render(self.text, self.antialias, self.color)
        self.rect = pygame.Rect(self.get_real_origin(), self.uifont.font.size(self.text))
        if self.angle:
            pass

    def draw(self, surface):
        surface.blit(self.surface, self.rect)

    def set_color(self, color):
        self.color = color
        self.build()

    def set_angle(self, angle):
        self.angle = angle
        self.build()

    def set_antialias(self, bool):
        self.antialias = bool
        self.build()

    def set_background_color(self, color):
        self.background_color = color
        self.build()