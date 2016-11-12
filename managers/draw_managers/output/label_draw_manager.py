from constructs.output.label import Label
import pygame

class LabelDrawManager(Label):

    def __init__(self, color=(0, 0, 0), angle=0, antialias=True, background_color=None, text="", uifont=None, center_text=True):
        Label.__init__(self)
        self.text = text
        self.uifont = uifont
        self.rect = pygame.Rect(self.get_real_origin(), self.uifont.font.size(self.text))
        self.color = color
        self.angle = angle
        self.antialias = antialias
        self.background_color = background_color
        self.center_text = center_text
        self.build()

    def build(self):
        self.surface = self.uifont.font.render(self.text, self.antialias, self.color)
        print_origin = self.origin[0] + self.offset[0], self.origin[1] + self.offset[1]
        if self.center_text:
            print_origin = self.get_real_origin()[0] + (self.width/2) - (self.uifont.font.size(self.text)[0]/2), self.get_real_origin()[1] + (self.height/2) - (self.uifont.font.size(self.text)[1]/2)
        self.rect = pygame.Rect(print_origin, self.uifont.font.size(self.text))
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