import pandas as pd
from objects.sound import Sound
from objects.sound_lab import SoundLab
import utils.decorators as decorators


class Manager:
    """Здесь мы обычно делаем описание того, для чего нужен класс (что он умеет, какие параметры на вход принимает).

    Attributes:
       csv_path: Путь до исходного файла csv.
    """

    def __init__(self, csv_path: str, sound: Sound, sound_lab: SoundLab):
        self.tones = pd.read_csv(csv_path, delimiter=" ")
        self.tones.set_index("index", inplace=True)
        self.sound = sound
        self.sound_lab = sound_lab

    @decorators.add_time_logger
    def create_sound(self, key_name):
        """Создает ноту."""

        fr = self.tones.loc[key_name, "frequency"]
        self.sound.create_wave(fr)
