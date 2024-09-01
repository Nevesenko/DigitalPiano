import pygame
from data.constants import *


class Sound:
    def __init__(self):
        pygame.mixer.init(channels=10)
        self.duration = 1
        self.t = np.linspace(
            0, self.duration, int(SAMPLE_RATE * self.duration), endpoint=False
        )

    def create_wave(self, frequency):
        wave = self._math_for_wave(frequency)
        channel = pygame.mixer.find_channel()
        tone = pygame.mixer.Sound(wave)
        channel.play(tone)

    def _math_for_wave(self, frequency):
        wave = AMPLITUDE_RATE * np.sin(RAD * frequency / FREQUENCY_RATIO * self.t)
        wave = np.int16(wave * INT16)

        # возможно стоит вписать преобразование tobinary()
        return wave
