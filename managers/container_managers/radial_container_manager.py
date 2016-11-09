from constructs.radial.radial_container import RadialContainer
from math import pi

class RadialContainerManager(RadialContainer):

    def __init__(self, origin=(0, 0), bisect_angle=0, radius=50, arc_radians=2*pi, width=50, active_radius=60, callback=None, callback_params=[], container_manager=None, draw_controller=None):
        super(RadialContainerManager, self).__init__(origin, bisect_angle, radius, arc_radians, width, active_radius, callback, callback_params)
        self.containers = []

    def build(self):
        pass

    def collide_point(self, point):
        for container in self.containers:
            if container.collide_point(point):
                return container
        return None

    def update(self, dt):
        for cont in self.containers:
            cont.update(dt)

    def add_container(self, container):
        self.containers.append(container)

    def draw(self, surface):
        pass