from ui_event import UIEvent
from event import Event
from pygame.locals import MOUSEBUTTONUP, MOUSEBUTTONDOWN


class ClickEvent(Event):

    def __init__(self, box, button=1, down_callback=None, up_callback=None):
        self.down_event = UIEvent(MOUSEBUTTONDOWN, self.down_event_callback, pygame_button=button)
        self.up_event = UIEvent(MOUSEBUTTONUP, self.up_event_callback, pygame_button=button)
        self.down_callback = down_callback
        self.up_callback = up_callback
        self.box = box


    def up_event_callback(self, event):
        if self.up_callback is None:
            return self.box.press_up()
        self.box.press_up()
        return self.up_callback(event)

    def down_event_callback(self, event):
        if self.box.collide_point(event.pos):
            if self.down_callback is None:
                return self.box.press_down()
            self.box.press_down()
            return self.down_callback(event)
        return self.up_event_callback(event)

    def check_event(self, event):
        if self.down_event.check_event(event):
            return True
        if self.up_event.check_event(event):
            return True
        return False