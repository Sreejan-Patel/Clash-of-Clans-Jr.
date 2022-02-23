from colorama import Fore, Style, Back
import numpy as np

class Troops():

    def __init__(self):
        self.troops_color = Back.MAGENTA+' '+Style.RESET_ALL
        self.x = np.zeros((10), type(int))
        self.y = np.zeros((10), type(int))
        self.alive = np.zeros((10), type(int))
        self.count = 0

    def spawn(self, key):
        """Spawning troops."""
        if self.count < 10:
            if key == 'i':
                self.x[self.count] = 7
                self.y[self.count] = 7
                self.alive[self.count] = 1
                self.count += 1
            elif key == 'j':
                self.x[self.count] = 73
                self.y[self.count] = 19
                self.alive[self.count] = 1
                self.count += 1
            elif key == 'k':
                self.x[self.count] = 32
                self.y[self.count] = 12
                self.alive[self.count] = 1
                self.count += 1
            else:
                pass