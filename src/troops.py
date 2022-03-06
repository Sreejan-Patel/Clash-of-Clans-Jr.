from operator import le
from colorama import Fore, Style, Back
import numpy as np

class Troops():

    def __init__(self,start,end):
        self.troops_color = Back.BLUE+' '+Style.RESET_ALL
        self.x = np.zeros((10), type(int))
        self.y = np.zeros((10), type(int))
        self.status = np.zeros((10), type(int))
        self.health = np.full((10), 30)
        self.troop = np.arange(10)
        self.count = 0
        self.damage = 10
        self.initialize(start,end)

    def initialize(self,start,end):
        """Initializing troops."""
        length = 2
        for i in range(10):
            if self.status[i] == 0:
                self.x[i] = start + i*length + 3*length
                self.y[i] = 11

    def spawn(self, key):
        """Spawning troops."""
        if self.count < 10:
            if key == 'i':
                self.x[self.count] = 7
                self.y[self.count] = 7
                self.status[self.count] = 1
                self.count += 1
            elif key == 'j':
                self.x[self.count] = 73
                self.y[self.count] = 19
                self.status[self.count] = 1
                self.count += 1
            elif key == 'k':
                self.x[self.count] = 32
                self.y[self.count] = 12
                self.status[self.count] = 1
                self.count += 1
            else:
                pass