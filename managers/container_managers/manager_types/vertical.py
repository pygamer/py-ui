from __future__ import division
from math import floor, ceil
from manager_type import ManagerTypeInterface

class Vertical(ManagerTypeInterface):

    def build(self, master, containers):
        width = master.width
        height = ceil(master.height / len(containers))
        for i, cont in enumerate(containers):
            cont.set_width(width)
            cont.set_height(height)
            cont.set_origin(master.get_real_origin())
            cont.set_offset((0, (i * height)))


    def __eq__(self, other):
        return isinstance(other, Vertical)