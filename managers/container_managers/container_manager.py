from constructs.box.box import Box
from managers.container_managers.manager_types.free_form import Freeform
from managers.container_managers.manager_types.column_grid import ColumnGrid


class ContainerManager(Box):

    def __init__(self, manager_type=None):
        Box.__init__(self)
        if manager_type is None:
            manager_type = ColumnGrid()
        self.containers = []
        self.type = manager_type

    def build_layout(self):
        self.type.build(self, self.containers)

    def get_box_point(self, point):
        for cont in self.containers:
            box = cont.get_box_point(point)
            if box is not None:
                return box

    def check_event(self, event):
        final_ret = False
        for cont in self.containers:
            res = cont.check_event(event)
            if res:
                final_ret = True
        return final_ret


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
