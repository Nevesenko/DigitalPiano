import pygame
from Data.constants import *


class Sound:
    def __init__(self):
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)  # стандартный запуск
        pygame.mixer.set_num_channels(64)
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
        wave = AMPLITUDE_RATE * np.sin(RAD * frequency / FREQUENCY_RATIO  * self.t)
        wave = np.clip(wave * INT16, -32767, 32767).astype(np.int16)
        start = int(len(wave) * 0.8)
        tail_len = len(wave) - start
        tail_x = np.linspace(0, 1, tail_len)
        damping = np.exp(-10 * tail_x)
        wave[start:] = (wave[start:] * damping).astype(np.int16)
        # возможно стоит вписать преобразование tobinary()
        return wave
