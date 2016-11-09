from __future__ import division

import pygame
from math import pi, sin, cos

from constructs.radial.radial_container import RadialContainer


class RadialDrawManager(RadialContainer):

    def __init__(self,
                 origin=(300, 300),
                 bisect_angle=0,
                 radius=100,
                 arc_radians=2 * pi,
                 width=50,
                 active_radius=60,
                 background_color=(100, 100, 100),
                 hover_color=(50, 50, 50),
                 click_color=(150, 150, 150),
                 resolution=100):
        RadialContainer.__init__(self, origin, bisect_angle, radius, arc_radians, width, active_radius)
        self.background_color = background_color
        self.pointlist = []
        self.hover_color = hover_color
        self.click_color = click_color
        self.active_color = self.background_color
        self.resolution = resolution
        self.build()

    def update(self, dt):
        if self.clicked:
            self.active_color = self.click_color
        elif self.hovered:
            self.active_color = self.hover_color
        else:
            self.active_color = self.background_color



    def build(self):
        self.pointlist = []
        self.pointlist.append(self.origin)
        col_x_diff_matrix = [cos(self.arc_radians/self.resolution), -sin(self.arc_radians/self.resolution)]
        col_y_diff_matrix = [sin(self.arc_radians/self.resolution), cos(self.arc_radians/self.resolution)]
        col_x_bis_matrix = [cos(self.bisect_angle), -sin(self.bisect_angle)]
        col_y_bis_matrix = [sin(self.bisect_angle), cos(self.bisect_angle)]
        mid_pos_x = col_x_bis_matrix[0] * self.radius
        mid_pos_y = col_y_bis_matrix[0] * self.radius
        col_x_half_matrix = [cos(self.arc_radians/2), -sin(self.arc_radians/2)]
        col_y_half_matrix = [sin(self.arc_radians/2), cos(self.arc_radians/2)]
        outerpt_1x = (col_x_half_matrix[0] * mid_pos_x) + (col_x_half_matrix[1] * mid_pos_y)
        outerpt_1y = (col_y_half_matrix[0] * mid_pos_x) + (col_y_half_matrix[1] * mid_pos_y)
        outerpt_2x = (col_x_half_matrix[0] * mid_pos_x) + (-col_x_half_matrix[1] * mid_pos_y)
        outerpt_2y = (-col_y_half_matrix[0] * mid_pos_x) + (col_y_half_matrix[1] * mid_pos_y)
        self.pointlist.append((outerpt_2x + self.origin[0], outerpt_2y + self.origin[1]))
        currx = outerpt_2x
        curry = outerpt_2y
        for x in range(self.resolution):
            currx_temp = (col_x_diff_matrix[0] * currx) + (col_x_diff_matrix[1] * curry)
            curry_temp = (col_y_diff_matrix[0] * currx) + (col_y_diff_matrix[1] * curry)
            currx = currx_temp
            curry = curry_temp
            self.pointlist.append((currx + self.origin[0], curry + self.origin[1]))


    def draw(self, surface):
        for cont in self.controllers:
            cont.draw(surface)
        pygame.draw.polygon(surface, self.active_color, self.pointlist)
    def draw_outline(self, surface):
        for cont in self.controllers:
            cont.draw_outline(surface)
        pygame.draw.aalines(surface, (0,0,0), True, self.pointlist, False)

