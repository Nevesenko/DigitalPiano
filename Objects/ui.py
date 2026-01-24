from Objects.manager import Manager
from Objects.render import Render


class UI:
    def __init__(self):
        self.render = Render()
        self.manager = Manager()



    def on_key_event(self, event):
        self.manager.create_sound(event.name)

