from constructs.input.checkbox import Checkbox
import pygame


class CheckTypes(object):

    class SmallBox(object):

        @staticmethod
        def draw(surface, size, check_color):
            q_w = size / 4
            h_w = size / 2
            print q_w, h_w
            pygame.draw.rect(surface, check_color, pygame.Rect((q_w, q_w), (h_w, h_w)))

    class X(object):

        @staticmethod
        def draw(surface, size, check_color):
            t_left = (0, 0)
            t_right = (0, size)
            b_left = (size, 0)
            b_right = (size, size)
            pygame.draw.line(surface, check_color, t_left, b_right, size/5)
            pygame.draw.line(surface, check_color, t_right, b_left, size/5)

    class Check(object):

        @staticmethod
        def draw(surface, size, check_color):
            mid_left = size/4, size/2
            mid_bot = size/2, size
            top_right = size - (size/4), 0
            pygame.draw.lines(surface, check_color, False, [mid_left, mid_bot, top_right], size/5)


class CheckboxDrawManager(Checkbox):

    def __init__(self, origin=(0, 0), offset=(0, 0), size=20, checked=False, background_color=(255, 255, 255), border_color=(0, 0, 0), check_color=(100, 100, 100), check_image=None, center_checkbox=True, check_type=CheckTypes.SmallBox):
        Checkbox.__init__(self, origin, offset, size, checked)
        self.surface = None
        self.rect = None
        self.background_color = background_color
        self.border_color = border_color
        self.check_color = check_color
        self.check_image = check_image
        self.center_checkbox = center_checkbox
        self.check_type = check_type
        self.build()

    def check(self):
        self.checked = not self.checked
        return True

    def build(self):
        self.surface = pygame.Surface((self.size, self.size))
        real_origin = self.get_real_origin()
        if self.center_checkbox:
            real_origin = (real_origin[0] + (self.width/2) - (self.size/2), real_origin[1] + (self.height/2) - (self.size/2))
        self.rect = pygame.Rect(real_origin, (self.size, self.size))
        self.surface.fill(self.background_color)
        if self.checked:
            if self.check_image is not None:
                self.surface.blit(self.check_image, pygame.Rect((0, 0), (0, 0)))
            else:
                self.check_type.draw(self.surface, self.size, self.check_color)
        pygame.draw.rect(self.surface, self.border_color, pygame.Rect((0, 0), (self.size, self.size)), 1)

    def draw(self, surface):
        surface.blit(self.surface, self.rect)


