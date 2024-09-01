from objects.manager import Manager


class UI:
    def __init__(self, manager: Manager):
        self.manager = manager

    def on_key_event(self, event):
        self.manager.create_sound(event.name)
