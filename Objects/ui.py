from Objects.manager import Manager

class UI:  #
    def __init__(self):
        self.manager = Manager()
    def on_key_event(self, event):
        self.manager.create_sound(event.name)