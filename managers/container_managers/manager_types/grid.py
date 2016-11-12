from __future__ import division
from math import ceil, sqrt, floor


class Grid(object):

    def __init__(self, cols=5):
        self.cols = cols


    def build(self, master, containers):
        if master is not None:
            print "got into master check"
            container_width = master.width / self.cols
            container_height = master.height / ceil(len(containers) / self.cols)
            print container_width, container_height
            print master
            origin = master.origin + master.offset
            i = 0
            row = 0
            while i < len(containers):
                if i != 0 and i % self.cols == 0:
                    row += 1
                x = (i % self.cols) * container_width
                y = row * container_height
                containers[i].set_origin((x, y))
                containers[i].set_height(container_height)
                containers[i].set_width(container_width)
                i += 1

    def __eq__(self, other):
        return isinstance(other, Grid)