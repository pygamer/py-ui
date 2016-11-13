from constructs.box.box import Box
from managers.draw_managers.input.checkbox_draw_manager import CheckboxDrawManager


class Checkbox(Box):

    def __init__(self, origin=(0, 0), offset=(0, 0), size=20, checked=False, draw_manager=None):
        Box.__init__(self, origin, offset, width=size, height=size, draw_manager=draw_manager)
        self.checked = checked
        self.size = size

    def add_container(self, container):
        pass

    def check(self):
        for cont in self.controllers:
            self.draw_controller.check()
        self.checked = True

    def uncheck(self):
        for cont in self.controllers:
            self.draw_controller.uncheck()
        self.checked = False
