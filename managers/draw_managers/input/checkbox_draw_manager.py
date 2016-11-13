from constructs.input.checkbox import Checkbox
import pygame


class CheckboxDrawManager(Checkbox):

    def __init__(self, origin=(0, 0), offset=(0, 0), size=20, checked=False, background_color=(100, 100, 100), border_color=(0, 0, 0), check_color=(0, 0, 0), check_image=None, center_checkbox=True):
        Checkbox.__init__(origin, offset, size, checked)
        self.surface = None
        self.rect = None
        self.background_color = background_color
        self.border_color = border_color
        self.check_color = check_color
        self.check_image = check_image
        self.center_checkbox = center_checkbox
        self.build()

    def build(self):
        self.surface = pygame.Surface((self.size, self.size))
        self.rect = pygame.Rect(self.get_real_origin(), (self.size, self.size))
        self.surface.fill(self.background_color)
        if self.checked:
            if self.check_image:
                self.surface.blit(self.check_image, pygame.Rect((0, 0), (0, 0)))
            else:
                q_w = self.width/4
                h_w = self.width/2
                pygame.draw.rect(self.surface, self.check_color, pygame.Rect((q_w, q_w), (h_w, h_w)))
        pygame.draw.rect(self.surface, self.border_color, pygame.Rect((0, 0), (0, 0)))

    def draw(self, surface):
        surface.blit(self.surface, self.rect)

