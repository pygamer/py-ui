from constructs.box.box import Box
from constructs.box.partition import Partition
from constructs.output.label import Label
from managers.draw_managers.output.label_draw_manager import LabelDrawManager
from managers.container_managers.container_manager import ContainerManager
from managers.draw_managers.box_draw_manager import BoxDrawManager
from fonts.font_loader import FontLoader

class ConstructGenerator(object):

    @staticmethod
    def create_box(origin=(0, 0), offset=(0, 0), width=100, height=100, container_manager=None, draw_manager=None, resizable=False, parent=None, callback=None, callback_params=[], events=[]):
        if draw_manager is None:
            draw_manager = BoxDrawManager(origin, offset, width, height, background_color=(200, 200, 200))
        if container_manager is None:
            container_manager = ContainerManager()
        return Box(origin, offset, width, height, container_manager, draw_manager, resizable, parent, callback, callback_params, events)


    @staticmethod
    def create_partition(origin=(0, 0), offset=(0, 0), width=100, height=100, containter_manager=None, draw_manager=None, resizable=False):
        if containter_manager is None:
            containter_manager = ContainerManager()
        if draw_manager is None:
            draw_manager = BoxDrawManager(origin, offset, width, height, background_color=(200, 200, 200))
        return Partition(origin, offset, width, height, containter_manager, draw_manager, resizable)


    @staticmethod
    def create_label(origin=(0, 0), offset=(0, 0), width=100, height=100, text="", uifont=None, draw_manager=None):
        if uifont is None:
            uifont = FontLoader().get_default_font()
        if draw_manager is None:
            draw_manager = LabelDrawManager(uifont=uifont, text=text)
        return Label(origin, offset, width, height, draw_manager)

if __name__ == "__main__":
    import pygame
    import pygame.locals
    from managers.container_managers.manager_types.horizontal import Horizontal
    from event.click_event import ClickEvent
    from event.mouse_motion_event import MouseMotionEvent
    c = ContainerManager(Horizontal())
    d = BoxDrawManager()

    b = ConstructGenerator.create_box(origin=(50, 50), width=500, height=500, container_manager=c)
    ce = ClickEvent(down_callback=b.press_down, up_callback=b.press_up, collide_func=b.collide_point)
    me = MouseMotionEvent(hover_callback=b.hover_over, off_callback=b.hover_off, collide_func=b.collide_point)
    b.events = [ce, me]

    b.add_container(ConstructGenerator.create_label(text="Hello"))
    b.add_container(ConstructGenerator.create_label(text="Gooby"))
    b.add_container(ConstructGenerator.create_label(text="Pls"))
    b.add_container(ConstructGenerator.create_label(text="Hello"))
    b.add_container(ConstructGenerator.create_label(text="Gooby"))
    b.add_container(ConstructGenerator.create_label(text="Pls"))
    b.add_container(ConstructGenerator.create_label(text="Hello"))
    b.add_container(ConstructGenerator.create_label(text="Gooby"))
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
            if b.check_event(event):
                update = True
        if update:
            b.build()
            s.fill((255, 255, 255))
            b.draw(s)
        pygame.display.update()