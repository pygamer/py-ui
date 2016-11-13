from __future__ import division
from math import ceil, sqrt, floor
from managers.container_managers.manager_types.manager_type import ManagerTypeInterface


class ColumnGrid(ManagerTypeInterface):
    """
    This manager type is for organizing a layout of the children in grid form.

    This manager can be given a cols parameter, designating the number of columns to use in the grid.
    This defaults to 5.

    The grid will set the height and width of it's children automatically.
    The width is based on the parent container's width and the number of columns
    The height is based on the number of rows filled.
    """

    def __init__(self, cols=5):
        self.cols = cols


    def build(self, master, containers):
        if master is not None:
            container_width = master.width / self.cols
            container_height = master.height / ceil(len(containers) / self.cols)
            origin = master.origin + master.offset
            i = 0
            row = 0
            while i < len(containers):
                if i != 0 and i % self.cols == 0:
                    row += 1
                x = (i % self.cols) * container_width
                y = row * container_height
                containers[i].set_offset((x, y))
                containers[i].set_origin(master.get_real_origin())
                containers[i].set_height(container_height)
                containers[i].set_width(container_width)
                i += 1

    def __eq__(self, other):
        return isinstance(other, ColumnGrid)