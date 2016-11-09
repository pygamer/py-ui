

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

    def __init__(self, origin=(0, 0), offset=(0, 0), width=100, height=100, container_manager=None, draw_controller=None, resizable=False, parent=None, callback=None, callback_params=[]):
        self.origin = origin
        self.offset = offset
        self.width = width
        self.height = height
        self.container_manager = container_manager
        self.draw_controller = draw_controller
        self.resizable = resizable
        self.callback = callback
        self.callback_params = []
        self.parent = parent

        self.controllers = []
        if self.draw_controller is not None:
            self.controllers.append(self.draw_controller)
        if self.container_manager is not None:
            self.controllers.append(self.container_manager)
        for cont in self.controllers:
            cont.set_origin(origin)
            cont.set_offset(offset)
            cont.set_width(width)
            cont.set_height(height)


    # Call this function if you want to resize the box
    # Takes a new width and height
    def resize(self, width, height):
        for cont in self.controllers:
            cont.resize(width, height)
        self.width = width
        self.height = height


    #Used to tack a container object onto the box
    def add_container(self, container):
        container.set_parent(self)
        for cont in self.controllers:
            cont.add_container(container)
        else:
            print "No container_manager on box_id: {}".format(self.box_id)


    #This function should be called automatically by some manager somewhere idk
    def update(self, dt):
        for cont in self.controllers:
            cont.update(dt)

    #call this function if you want to call the button's callback
    def callback(self):
        if self.callback is not None:
            return self.callback(*self.callback_params)
        print "No callback set for box_id: {}".format(self.box_id)

    #This function determines whether the point given lies within the box's constraints
    def collide_point(self, point):
        x, y = point
        return x >= self.origin[0] and x <= self.origin[0] + self.offset[0] and y >= self.origin[1] and y <= self.origin[1] + self.offset[1]

    def draw(self, surface):
        for cont in self.controllers:
            cont.draw(surface)


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
        if self.resizable:
            for cont in self.controllers:
                cont.set_width(width)
            self.width = width

    def set_height(self, height):
        if self.resizable:
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
