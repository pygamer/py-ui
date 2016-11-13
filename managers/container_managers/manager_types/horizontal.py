from __future__ import division
from math import floor
from manager_type import ManagerTypeInterface

class Horizontal(ManagerTypeInterface):

    def build(self, master, containers):
        width = floor(master.width / len(containers))
        height = master.height
        for i, cont in enumerate(containers):
            cont.set_width(width)
            cont.set_height(height)
            cont.set_origin(master.get_real_origin())
            cont.set_offset(((i * width), 0))
