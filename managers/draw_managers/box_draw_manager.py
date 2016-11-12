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
                 title_bar=True,
                 title_bar_border=True,
                 title_bar_height = 21,
                 title_text="This is a title",
                 title_color=(150, 150, 150),
                 title_border_width=3,
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
        self.title_bar = title_bar
        self.title_text = title_text
        self.title_color = title_color
        self.title_border_width = title_border_width
        self.title_bar_height = title_bar_height
        self.title_bar_border = title_bar_border
        self.build()

    def build(self):
        self.surface = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect((self.origin[0] + self.offset[0], self.origin[1] + self.offset[1]), (self.width, self.height))
        if self.background_image is not None:
            self.surface.blit(self.background_image, pygame.Rect((0, 0), (0, 0)))
            return
        if self.fill_background:
            self.surface.fill(self.background_color)
        if self.title_bar:
            pygame.draw.rect(self.surface, self.title_color, pygame.Rect(self.origin, (self.width, self.title_bar_height)))
            if self.title_bar_border:
                pygame.draw.rect(self.surface, self.border_color, pygame.Rect(self.origin, (self.width, self.title_bar_height)), self.title_border_width)
        if self.bordered:
            pygame.draw.rect(self.surface, self.border_color, pygame.Rect((0, 0), (self.width , self.height)), self.border_width)

    def draw(self, surface):
        surface.blit(self.surface, self.rect)
