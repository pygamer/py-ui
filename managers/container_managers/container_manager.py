from constructs.box.box import Box
from managers.container_managers.manager_types.free_form import Freeform


class ContainerManager(Box):

    def __init__(self, manager_type=Freeform()):
        Box.__init__(self)
        self.containers = []
        self.type = manager_type

    def build_layout(self):
        self.type.build(self, self.containers)

    def get_box_point(self, point):
        for cont in self.containers:
            box = cont.get_box_point(point)
            if box is not None:
                return box


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
