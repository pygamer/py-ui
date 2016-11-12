from constructs.box.box import Box
from managers.container_managers.manager_types.grid import Grid


class ContainerManager(Box):

    def __init__(self, manager_type=Grid()):
        Box.__init__(self)
        self.containers = []
        self.type = manager_type

    def build_layout(self):
        print self.width, self.height
        self.type.build(self, self.containers)

    def build(self):
        self.build_layout()
        for cont in self.containers:
            cont.build()

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
    cm.set_type(Grid())
