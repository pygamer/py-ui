from constructs.radial.radial_container import RadialContainer
from math import pi

class RadialContainerManager(RadialContainer):

    def __init__(self, origin=(0, 0),
                 bisect_angle=0,
                 radius=50,
                 arc_radians=2*pi,
                 width=50,
                 active_radius=60,
                 container = None):
        super(RadialContainerManager, self).__init__(origin, bisect_angle, radius, arc_radians,
                                                     width, active_radius)
        self.container = container

    def build(self):
        self.build_center()
        self.container.set_center(self.center)

    def collide_point(self, point):
        return self.container.collide_point(point)

    def update(self, dt):
        self.container.update(dt)

    def draw(self, surface):
        self.container.draw(surface)