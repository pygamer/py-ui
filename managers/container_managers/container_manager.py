from constructs.box.box import Box
from managers.container_managers.manager_type import ManagerType
from math import ceil, sqrt






class ContainerManager(Box):

    def __init__(self, manager_type=ManagerType.GRID()):
        super(Box, self).__init__()
        self.containers = []
        self.type = manager_type

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
