import keyboard

from Objects.ui import UI
import pygame
def main():
    pygame.init()
    pygame.mixer.init()
    manager = UI()

    keyboard.hook(lambda event:
                  manager.on_key_event(event)
                  if event.event_type =='down' else None)

    keyboard.wait('esc')


if __name__ == '__main__':
    main()