from constructs.box import Box
from math import ceil, sqrt


class ManagerType(object):


    class GRID(object):

        max__container_width = 100
        max_container_height = 100
        min_container_width = 50
        min_container_height = 50

        def __init__(self,
                     max_container_width=100,
                     max_container_height=100,
                     min_container_width=50,
                     min_container_height=50):
            self.max_container_height = max_container_height
            self.max_container_width = max_container_width
            self.min_container_width = min_container_width
            self.min_container_height = min_container_height

        def build(self, containers):
            grid_dimensions = ceil(sqrt(len(containers)))


        def __eq__(self, other):
            return isinstance(other, ManagerType.GRID)



class ContainerManager(Box):

    def __init__(self, manager_type=ManagerType.GRID()):
        super(Box, self).__init__()
        self.containers = []
        self.type = manager_type
        self.types = [ManagerType.GRID]

    def build_layout(self):
        self.type.build(self.containers)

    def set_type(self, tp):
        self.type = tp
        self.type.build(self.containers)

    def add_container(self, container):
        self.containers.append(container)

    def update(self, dt):
        for cont in self.containers:
            cont.update(dt)

    def draw(self, surface):
        for cont in self.containers:
            cont.draw(surface)

if __name__ == "__main__":
    cm = ContainerManager()
    cm.set_type(ManagerType.GRID())
