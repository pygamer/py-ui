from math import ceil, sqrt, floor


class GRID(object):

    def __init__(self, cols=1):
        self.master = None
        self.cols = cols


    def set_master(self, master):
        self.master = master


    def build(self, containers):
        if self.master is not None:
            container_width = self.master.width / self.cols
            container_height = self.master.height / ceil(len(containers) / self.cols)
            origin = self.master.origin + self.master.offset
            i = 0
            row = 0
            while i < len(containers):
                for c in range(self.cols):
                    x = c * container_width
                    y = row * container_height
                    containers[i].set_origin((x, y))
                    containers[i].set_height(container_height)
                    containers[i].set_width(container_width)
                    i += 1
                row += 1

    def __eq__(self, other):
        return isinstance(other, GRID)