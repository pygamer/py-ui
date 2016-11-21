from constructs.box.box import Box

class Checkbox(Box):

    def __init__(self, origin=(0, 0), offset=(0, 0), size=20, checked=False, draw_manager=None):
        Box.__init__(self, origin, offset, width=size, height=size, draw_manager=draw_manager)
        self.checked = checked
        self.size = size

    def add_container(self, container):
        pass

    def press_down(self):
        self.checked = not self.checked
        return self.draw_controller.check()


    def press_up(self):
        return False


