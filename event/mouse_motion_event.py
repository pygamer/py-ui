from event import Event
from ui_event import UIEvent
from pygame.locals import MOUSEMOTION

class MouseMotionEvent(Event):

    def __init__(self, box, hover_callback=None, off_callback=None):
        self.event = UIEvent(MOUSEMOTION, self.hover_callback, else_callback=self.off_event_callback)
        self.off_callback = off_callback
        self.h_callback = hover_callback
        self.box = box


    def hover_callback(self, event):
        if self.box.collide_point(event.pos):
            if self.h_callback is None:
                return self.box.hover_over()
            self.box.hover_over()
            return self.h_callback()
        return self.off_event_callback(event)

    def off_event_callback(self, event):
        if self.off_callback is None:
            return self.box.hover_off()
        self.box.hover_off()
        return self.off_callback()



    def check_event(self, event):
        return self.event.check_event(event)


