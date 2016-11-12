from constructs.box.box import Box
from constructs.box.partition import Partition
from constructs.output.label import Label
from managers.draw_managers.output.label_draw_manager import LabelDrawManager
from managers.container_managers.container_manager import ContainerManager
from managers.draw_managers.box_draw_manager import BoxDrawManager
from fonts.font_loader import FontLoader

class ConstructGenerator(object):

    @staticmethod
    def create_default_box(origin=(0, 0), offset=(0, 0), width=100, height=100, container_manager=None, draw_manager=None, resizable=False, parent=None, callback=None, callback_params=[]):
        if draw_manager is None:
            draw_manager = BoxDrawManager(origin, offset, width, height, background_color=(200, 200, 200))
        if container_manager is None:
            container_manager = ContainerManager()
        return Box(origin, offset, width, height, container_manager, draw_manager, resizable, parent, callback, callback_params)


    @staticmethod
    def create_default_partition(origin=(0, 0), offset=(0, 0), width=100, height=100, containter_manager=None, draw_manager=None, resizable=None):
        return Partition(origin, offset, width, height, containter_manager, draw_manager, resizable)


    @staticmethod
    def create_default_label(origin=(0, 0), offset=(0, 0), width=100, height=100, text="", uifont=None, draw_manager=None):
        if uifont is None:
            uifont = FontLoader().get_default_font()
        if draw_manager is None:
            draw_manager = LabelDrawManager(uifont=uifont, text=text)
        return Label(origin, offset, width, height, draw_manager)

if __name__ == "__main__":
    import pygame
    import pygame.locals
    b = ConstructGenerator.create_default_box(width=500, height=500)
    b.add_container(ConstructGenerator.create_default_label(offset=(100, 100), text="Hello"))
    b.build()
    pygame.init()
    s = pygame.display.set_mode((800, 600))
    s.fill((255, 255, 255))
    b.draw(s)
    while True:
        update = False
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
        pygame.display.update()