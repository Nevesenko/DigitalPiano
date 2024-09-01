import keyboard
import utils.decorators as decorators
from objects.manager import Manager
from objects.sound import Sound
from objects.sound_lab import SoundLab
from objects.ui import UI
import pygame


@decorators.add_logger
def main():
    pygame.init()
    pygame.mixer.init()
    csv_path = "./data/tonesData.csv"
    manager = UI(Manager(csv_path, Sound(), SoundLab()))

    keyboard.hook(
        lambda event: (
            manager.on_key_event(event) if event.event_type == "down" else None
        )
    )

    keyboard.wait("esc")


if __name__ == "__main__":
    main()
