import numpy as np
import pygame
import pandas as pd
from Objects.sound import Sound
from Objects.soundLab import SoundLab
import time
import Utils.decorators as decorators
class Manager:
    def __init__(self):
        self.tones = pd.read_csv('../DigitalPiano_/Data/tonesData.csv', delimiter=' ')
        self.tones.set_index('index', inplace=True)
        self.sound = Sound()
        self.soundLab = SoundLab()
    @decorators.add_time_logger
    def create_sound(self, keyName):
        '''создает ноту'''
        fr = self.tones.loc[keyName, 'frequency']
        self.sound.create_wave(fr)

    def change_the_scale(self):
        '''изменят текущую расстановку частот в файле данных'''
        pass

    def save_changes(self):
        '''сохраняет текущие настройки частот в файл
        (для дальнейшего переиспользования)'''
        pass