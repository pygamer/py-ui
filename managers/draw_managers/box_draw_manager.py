from constructs.box.box import Box
import pygame

class BoxDrawManager(Box):

    def __init__(self, origin=(0, 0),
                 offset=(0, 0),
                 width=100,
                 height=100,
                 background_color=(0, 0, 0),
                 border_color=(100, 100, 100),
                 bordered=True,
                 border_width=5,
                 fill_background=True,
                 background_image=None,
                 alpha=255):
        Box.__init__(self, origin, offset, width, height)
        self.surface = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect((self.origin[0] + self.offset[0], self.origin[1] + self.offset[1]), (self.width, self.height))
        self.fill_background = fill_background
        self.background_color = background_color
        self.border_color = border_color
        self.bordered = bordered
        self.border_width = border_width
        self.alpha = alpha
        self.background_image = background_image
        self.build()

    def update(self, dt):
        pass

    def build(self):
        self.surface = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(self.get_real_origin(), (self.width, self.height))
        if self.background_image is not None:
            self.surface.blit(self.background_image, pygame.Rect((0, 0), (0, 0)))
            return
        if self.fill_background:
            self.surface.fill(self.background_color)
        if self.bordered:
            pygame.draw.rect(self.surface, self.border_color, pygame.Rect((0, 0), (self.width , self.height)), self.border_width)

    def draw(self, surface):
        surface.blit(self.surface, self.rect)
