from constructs.box.box import Box


class Label(Box):

    def __init__(self, origin=(0, 0), offset=(0, 0), width=100, height=100, draw_manager=None):
        Box.__init__(self, origin, offset, width, height, draw_manager=draw_manager)

    def build(self):
        for cont in self.controllers:
            cont.build()

    def set_text(self, text):
        for cont in self.controllers:
            cont.set_text(text)

    def set_uifont(self, uifont):
        for cont in self.controllers:
            cont.set_uifont(uifont)