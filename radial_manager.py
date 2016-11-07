from math import pi, sqrt
from pygame.locals import *
import pygame
import random

class RadialManager(object):

    def __init__(self, origin, offset, radius, active_radius, randomize_radius=False, random_scale=.5):
        self.radial_containers = []
        self.origin = origin
        self.offset = offset
        self.radius = radius
        self.active_radius = active_radius
        self.randomize_radius = randomize_radius
        self.random_scale = random_scale

    def build(self):
        self.real_center = self.origin[0] + self.offset[0], self.origin[1] + self.offset[1]
        max_arc_len = 2 * pi * self.radius
        arc_len = max_arc_len/len(self.radial_containers)
        d_angle = 2 * pi/len(self.radial_containers)
        for i, cont in enumerate(self.radial_containers):
            cont.set_origin(self.real_center)
            cont.set_bisect_angle(i*d_angle)
            if self.randomize_radius:
                cont.set_radius(self.radius + random.randrange(0, self.radius) * self.random_scale, self.active_radius)
            else:
                cont.set_radius(self.radius, self.active_radius)
            cont.set_width(arc_len)
            cont.set_arcr(d_angle)
            cont.build()

    def check_event(self, event):
        dx = event.pos[0] - (self.origin[0] + self.offset[0])
        dy = event.pos[1] - (self.origin[1] + self.offset[1])
        dist = sqrt(dx**2 + dy**2)
        if dist > self.radius:
            for cont in self.radial_containers:
                cont.unhover()
                cont.press_up()
            return True
        if event.type == MOUSEMOTION:
            for cont in self.radial_containers:
                if cont.collide_point(event.pos):
                    cont.hover()
                else:
                    cont.unhover()
            return True
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            for cont in self.radial_containers:
                if cont.collide_point(event.pos):
                    cont.press_down()
            return True
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            for cont in self.radial_containers:
                cont.press_up()
            return True
        return False

    def update(self, dt):
        for cont in self.radial_containers:
            cont.update(dt)

    def get_containers(self):
        return self.radial_containers

    def set_radius(self, radius):
        self.radius = radius
        self.build()

    def set_origin(self, origin):
        self.origin = origin
        self.build()

    def set_offset(self, offset):
        self.offset = offset
        self.build()

    def add_container(self, container):
        self.radial_containers.append(container)

    def draw(self, surface):
        for cont in self.radial_containers:
            cont.draw(surface)
        for cont in self.radial_containers:
            cont.draw_outline(surface)

if __name__ == "__main__":
    import constructs.radial_container as rc
    import radial_draw_manager as rdm
    rm = RadialManager((0, 0), (300, 300), 100, 150)
    total_rads = 6
    for x in range(total_rads):
        color = ((155/total_rads) * x + 100, (255/(total_rads*2)) * x, (255/(total_rads*3)) * x)
        color = list(color)
        random.shuffle(color)
        color = tuple(color)
        rad_draw_mgr = rdm.RadialDrawManager(background_color=color, hover_color=color)
        rad_c = rc.RadialContainer(draw_controller=rad_draw_mgr)
        rm.add_container(rad_c)
    rm.build()
    import pygame
    import pygame.locals
    pygame.init()
    s = pygame.display.set_mode((800,600))
    s.fill((255, 255, 255))
    rm.draw(s)
    while True:
        update = False
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
            if event.type == MOUSEMOTION or event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
                update = rm.check_event(event)
        if update:
            s.fill((255, 255, 255))
        rm.update(1)
        rm.draw(s)
        pygame.display.update()

