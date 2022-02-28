from colorama import Fore , Back , Style
import numpy as np


class Walls():

    def __init__(self):
        self.height = 1
        self.width = 1
        self.health = np.full((100), 40)
        self.wall_color = Back.BLACK + ' ' + Style.RESET_ALL
        self.y = np.full((114), 0)
        self.x = np.full((114), 0)
        self.initialize_walls()

    def initialize_walls(self):

        for i in range(43):
            self.y[i] = 14
            self.x[i] = 19+i

        for i in range(43):
            self.y[i+43] = 29
            self.x[i+43] = 19+i

        for i in range(14):
            self.y[i+86] = 15+i
            self.x[i+86] = 19

        for i in range(14):
            self.y[i+100] = 15+i
            self.x[i+100  ] = 61



        
    def health_check(self):
        '''
        This function checks the health of the hut and returns the color of the building
        '''
        