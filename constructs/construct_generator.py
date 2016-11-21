from constructs.box.box import Box
from constructs.box.partition import Partition
from constructs.output.label import Label
from constructs.input.checkbox import Checkbox
from managers.draw_managers.output.label_draw_manager import LabelDrawManager
from managers.container_managers.container_manager import ContainerManager
from managers.draw_managers.box_draw_manager import BoxDrawManager
from managers.draw_managers.input.checkbox_draw_manager import CheckboxDrawManager
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

    @staticmethod
    def create_checkbox(origin=(0, 0), offset=(0, 0), size=20, checked=False, draw_manager=None):
        if draw_manager is None:
            draw_manager = CheckboxDrawManager()
        return Checkbox(origin, offset, size, checked, draw_manager)
