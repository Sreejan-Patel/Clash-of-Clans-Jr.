from colorama import Fore, Style, Back
from src.input import Get, input_to
from src.king import King
from src.troops import Troops
import numpy as np
import os
import time
import random
import math

class Village():

    def __init__(self):
        self.rows = 39
        self.cols = 78
        self.village_color = Back.LIGHTCYAN_EX+' '+Style.RESET_ALL
        self.border_color = Back.BLACK+' '+Style.RESET_ALL
        self.village = np.zeros((self.rows, self.cols))
        self.getch = Get()
        self.king = King()
        self.troops = Troops()
        self.render()

    def get_key(self):
        """Getting key from user."""
        key = input_to(self.getch)
        
        if(key == 'b' and self.king.alive == False):
            self.king.spawn()
        if(key == 'w' or 'a' or 's' or 'd' or 'space' and self.king.alive == True):
            self.king.move(key)
        if(key == 'i' or 'j' or 'k' and self.troops.count < 10):
            self.troops.spawn(key)

        return key

    def render(self):
        """Printing village."""
        clear = lambda: os.system('clear')
        clear()
        self.village = [[self.village_color for i in range(self.cols)] for j in range(self.rows)]
        
        # Drawing village border
        self.village = np.insert(self.village, 0, self.border_color, axis=0)
        self.village = np.insert(self.village, self.rows+1, self.border_color, axis=0)
        self.village = np.insert(self.village, 0, self.border_color, axis=1)
        self.village = np.insert(self.village, self.cols+1, self.border_color, axis=1)


        self.village[self.king.y][self.king.x] = self.king.king_color
        
        for counter in range(self.troops.count):
            if self.troops.alive[counter] == 1:
                self.village[self.troops.y[counter]][self.troops.x[counter]] = self.troops.troops_color

        print('\n'.join([''.join(row) for row in self.village]))


