from __future__ import division
from math import ceil
from managers.container_managers.manager_types.manager_type import ManagerTypeInterface

class RowGrid(ManagerTypeInterface):

    def __init__(self, rows=5):
        self.rows = rows


    def build(self, master, containers):
        if master is not None:
            container_width = master.width / ceil(len(containers) / self.rows)
            container_height = master.height / self.rows
            origin = master.origin + master.offset
            i = 0
            col = 0
            while i < len(containers):
                if i != 0 and i % self.rows == 0:
                    col += 1

                x = col * container_width
                y = (i % self.rows) * container_height
                containers[i].set_offset((x,y))
                containers[i].set_origin(master.get_real_origin())
                containers[i].set_height(container_height)
                containers[i].set_width(container_width)
                i += 1


    def __eq__(self, other):
        return isinstance(other, RowGrid)