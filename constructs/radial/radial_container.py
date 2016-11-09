from math import pi, sqrt, acos, asin

class RadialContainer(object):

    def __init__(self, origin=(0, 0), bisect_angle=0, radius=50, arc_radians=2*pi, width=50, active_radius=60, callback=None, callback_params=[], container_manager=None, draw_controller=None):
        self.origin = origin
        self.bisect_angle = bisect_angle
        self.radius = radius
        self.arc_radians = arc_radians
        self.width = width
        self.container_manager = container_manager
        self.draw_controller= draw_controller
        self.callback = callback
        self.callback_params = callback_params
        self.active_radius = active_radius
        self.inactive_radius = radius
        self.clicked = False
        self.hovered = False

        self.controllers = []
        if self.draw_controller is not None:
            self.controllers.append(self.draw_controller)
        if self.container_manager is not None:
            self.controllers.append(self.controllers)
        for cont in self.controllers:
            cont.set_origin(self.origin)
            cont.set_bisect_angle(self.bisect_angle)
            cont.set_radius(self.radius, self.active_radius)
            cont.set_width(self.width)
            cont.set_arcr(self.arc_radians)

    def build(self):
        for cont in self.controllers:
            cont.build()

    def callback(self):
        return self.callback(*self.callback_params)

    def collide_point(self, point):
        magnitude = sqrt((point[0] - self.origin[0])**2 + (point[1] - self.origin[1])**2)
        if magnitude > self.radius or magnitude <= 0:
            return False
        angle = acos((point[0] - self.origin[0])/magnitude)
        if point[1] < self.origin[1]:
            angle = abs(angle - pi) + pi
        return self if abs(self.bisect_angle - angle) < self.arc_radians / 2 or abs(self.bisect_angle - angle + 2 * pi) < self.arc_radians/2 else None

    def update(self, dt):
        for cont in self.controllers:
            cont.update(dt)

    def press_down(self):
        for cont in self.controllers:
            cont.press_down()
        self.clicked = True
        self.build()

    def press_up(self):
        for cont in self.controllers:
            cont.press_up()
        self.clicked = False
        self.build()

    def hover(self):
        for cont in self.controllers:
            cont.hover()
        self.radius = self.active_radius
        self.hovered = True
        self.build()

    def unhover(self):
        for cont in self.controllers:
            cont.unhover()
        self.radius = self.inactive_radius
        self.hovered = False
        self.build()

    #Setters
    def set_origin(self, origin):
        for cont in self.controllers:
            cont.set_origin(origin)
        self.origin = origin

    def set_bisect_angle(self, angle):
        for cont in self.controllers:
            cont.set_bisect_angle(angle)
        self.bisect_angle = angle

    def set_radius(self, radius, active_radius):
        for cont in self.controllers:
            cont.set_radius(radius, active_radius)
        self.radius = radius
        self.inactive_radius = radius
        self.active_radius = active_radius

    def set_width(self, width):
        for cont in self.controllers:
            cont.set_width(width)
        self.width = width

    def set_arcr(self, arcr):
        for cont in self.controllers:
            cont.set_arcr(arcr)
        self.arc_radians = arcr

    def draw(self, surface):
        for cont in self.controllers:
            cont.draw(surface)

    def draw_outline(self, surface):
        for cont in self.controllers:
            cont.draw_outline(surface)

