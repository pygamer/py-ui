from event import Event

class UIEvent(Event):

    def __init__(self, pygame_type, callback, else_callback=None, pygame_button=None, pygame_key=None):
        self.pygame_type = pygame_type
        self.callback = callback
        self.pygame_button = pygame_button
        self.pygame_key = pygame_key
        self.else_callback = else_callback

    def check_event(self, event):
        if event.type == self.pygame_type:
            if self.pygame_button is not None and event.button == self.pygame_button:
                return self.callback(event)
            elif self.pygame_key is not None and event.key == self.pygame_key:
                return self.callback(event)
            elif self.pygame_button is None and self.pygame_key is None:
                return self.callback(event)
            if self.else_callback is not None:
                return self.else_callback()
        return False