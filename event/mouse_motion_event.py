from event import Event
from ui_event import UIEvent
from pygame.locals import MOUSEMOTION

class MouseMotionEvent(Event):

    def __init__(self, hover_callback, off_callback, collide_func=None):
        self.event = UIEvent(MOUSEMOTION, self.hover_callback)
        self.off_callback = off_callback
        self.collide_func = collide_func
        self.h_callback = hover_callback


    def hover_callback(self, event):
        ret = False
        if self.collide_func is None:
            return self.off_callback()
        else:
            if self.collide_func(event.pos):
                return self.h_callback()
            else:
                return self.off_callback()


    def check_event(self, event):
        return self.event.check_event(event)


