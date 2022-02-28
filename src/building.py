from colorama import Fore , Back , Style
import numpy as np

class Building():

    def __init__(self):
        self.building_color_100 = Back.GREEN+' '+Style.RESET_ALL                # color of the building when the health is in the range of 50 - 100%
        self.building_color_50  = Back.YELLOW+' '+Style.RESET_ALL               # color of the building when the health is in the range of 20 - 50%
        self.building_color_20  = Back.RED+' '+Style.RESET_ALL                  # color of the building when the health is in the range of 0 - 20%


class Hut(Building):

    def __init__(self):
        Building.__init__(self)
        self.height = 1
        self.width = 1
        self.health = np.full((5), 30)
        self.y = np.full((5), 0)
        self.x = np.full((5), 0)
        self.initialize_huts()

    def initialize_huts(self):
        '''
        This function initializes the huts
        '''
        self.y[0] = 15
        self.x[0] = 20

        self.y[1] = 15
        self.x[1] = 60

        self.y[2] = 28
        self.x[2] = 20

        self.y[3] = 28
        self.x[3] = 60

        self.y[4] = 28
        self.x[4] = 40

        
    def health_check(self, i):
        '''
        This function checks the health of the hut and returns the color of the building
        '''
        if self.health[i] <= ((20/100)*20):
            return self.building_color_20
        elif self.health[i] <= ((50/100)*20):
            return self.building_color_50
        else:
            return self.building_color_100

class Cannon(Building):
    
    def __init__(self):
        Building.__init__(self)
        self.height = 2
        self.width = 3
        self.health = np.full((2), 100)
        self.y = np.full((2), 0)
        self.x = np.full((2), 0)
        self.initialize_cannons()

    def initialize_cannons(self):
        '''
        This function initializes the huts
        '''
        self.y[0] = 20
        self.x[0] = 23

        self.y[1] = 20
        self.x[1] = 55

    def health_check(self, i):
        '''
        This function checks the health of the hut and returns the color of the building
        '''
        if self.health[i] <= ((20/100)*50):
            return self.building_color_20
        elif self.health[i] <= ((50/100)*50):
            return self.building_color_50
        else:
            return self.building_color_100

class TownHall(Building):

    def __init__(self):
        Building.__init__(self)
        self.height = 4
        self.width = 3
        self.health = np.full((1), 150)
        self.x = 39
        self.y = 19

        
    def health_check(self):
        '''
        This function checks the health of the hut and returns the color of the building
        '''
        if self.health[0] <= ((20/100)*100):
            return self.building_color_20
        elif self.health[0] <= ((50/100)*100):
            return self.building_color_50
        else:
            return self.building_color_100