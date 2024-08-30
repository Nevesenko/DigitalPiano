import pygame
import numpy
import keyboard
import pandas as pd
from manager import Manager

class UI:  # должен обращаться к общему объекту для синхрона с свойствами
    def __init__(self):
        self.tones = pd.read_csv('tonesData.csv', delimiter=' ')
        self.tones.set_index('index', inplace=True)
        self.manager = Manager()
    def on_key_event(self, event):
        note = self.tones.loc[event.name, 'frequency']
        self.manager.create_sound()