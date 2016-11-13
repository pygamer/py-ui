

class Box(object):

    """
     Takes the origin in which the context specifies.
     If a box is within another box for instance,
     the inner box uses the out box's offset as the origin

     Also takes it's own offset coordinates from it's origin.
     Essentially, that will make this box's start coordinates equal to
     origin + offset, where origin is in the form (x, y) and offset is also
     in the form (x, y)
    """

    box_counter = 0

    def __init__(self, origin=(0, 0), offset=(0, 0), width=100, height=100, container_manager=None, draw_manager=None, resizable=False, parent=None, callback=None, callback_params=[], events=[]):
        self.origin = origin
        self.offset = offset
        self.width = width
        self.height = height
        self.container_manager = container_manager
        self.draw_controller = draw_manager
        self.resizable = resizable
        self.callback_func = callback
        self.callback_params = []
        self.parent = parent
        self.events = events

        self.controllers = []
        # DRAW CONTROLLER MUST BE FIRST IN self.controllers (if it exists at all)!!!
        if self.draw_controller is not None:
            self.controllers.append(self.draw_controller)
        if self.container_manager is not None:
            self.controllers.append(self.container_manager)
        for cont in self.controllers:
            cont.set_origin(origin)
            cont.set_offset(offset)
            cont.set_width(width)
            cont.set_height(height)
            cont.set_resizable(resizable)


    # Call this function if you want to resize the box
    # Takes a new width and height
    def resize(self, width, height):
        for cont in self.controllers:
            cont.resize(width, height)
        self.width = width
        self.height = height

    def check_event(self, event):
        for cont in self.controllers:
            ret = cont.check_event(event)
            if ret:
                return ret
        for ev in self.events:
            ret = ev.check_event(event)
            if ret:
                return ret

    def build(self):
        for cont in self.controllers:
            cont.build()

    def get_box_point(self, point):
        for cont in self.controllers:
            box = cont.get_box_point(point)
            if box is not None:
                return box
        return self if self.collide_point(point) else None

    #Used to tack a container object onto the box
    def add_container(self, container):
        container.set_parent(self)
        for cont in self.controllers:
            cont.add_container(container)

    def get_real_origin(self):
        return self.origin[0] + self.offset[0], self.origin[1] + self.offset[1]

    #This function should be called automatically by some manager somewhere idk
    def update(self, dt):
        for cont in self.controllers:
            cont.update(dt)

    #call this function if you want to call the button's callback
    def callback(self):
        if self.callback_func is not None:
            return self.callback_func(*self.callback_params)

    #This function determines whether the point given lies within the box's constraints
    def collide_point(self, point):
        x, y = point
        return x >= self.origin[0] + self.offset[0] and x <= self.origin[0] + self.offset[0] + self.width and y >= self.origin[1] + self.offset[1] and y <= self.origin[1] + self.offset[1] + self.height

    def draw(self, surface):
        for cont in self.controllers:
            cont.draw(surface)

    def hover_over(self):
        self.draw_controller.hover_over()
        return True

    def hover_off(self):
        self.draw_controller.hover_off()
        return True

    def press_down(self):
        self.draw_controller.press_down()
        return True

    def press_up(self):
        self.draw_controller.press_up()
        return True

    #SETTERS
    def set_origin(self, origin):
        for cont in self.controllers:
            cont.set_origin(origin)
        self.origin = origin

    def set_offset(self, offset):
        for cont in self.controllers:
            cont.set_offset(offset)
        self.offset = offset

    def set_width(self, width):
        for cont in self.controllers:
            cont.set_width(width)
        self.width = width

    def set_height(self, height):
        for cont in self.controllers:
            cont.set_height(height)
        self.height = height

    def set_parent(self, parent):
        for cont in self.controllers:
            cont.set_parent(parent)
        self.parent = parent

    def set_resizable(self, boolean):
        for cont in self.controllers:
            cont.set_resizable(boolean)
        self.resizable = boolean

    #PRIVATE...
