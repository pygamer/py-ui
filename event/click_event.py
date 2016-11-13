from ui_event import UIEvent
from event import Event
from pygame.locals import MOUSEBUTTONUP, MOUSEBUTTONDOWN


class ClickEvent(Event):

    def __init__(self, button=1, down_callback=None, up_callback=None, collide_func=None):
        self.down_event = UIEvent(MOUSEBUTTONDOWN, self.down_event_callback, pygame_button=button)
        self.up_event = UIEvent(MOUSEBUTTONUP, self.up_event_callback, pygame_button=button)
        self.down_callback = down_callback
        self.up_callback = up_callback
        self.collide_func = collide_func


    def up_event_callback(self, event):
        if self.up_callback is not None:
            return self.up_callback()

    def down_event_callback(self, event):
        if self.down_callback is not None:
            if self.collide_func is not None:
                if self.collide_func(event.pos):
                    return self.down_callback()
                return False
            return self.down_callback()

    def check_event(self, event):
        if self.down_event.check_event(event):
            return True
        if self.up_event.check_event(event):
            return True
        return False