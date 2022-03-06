from colorama import Fore , Back , Style
import numpy as np

class Building():

    def __init__(self):
        self.building_color_100 = Back.LIGHTGREEN_EX+' '+Style.RESET_ALL                # color of the building when the health is in the range of 50 - 100%
        self.building_color_50  = Back.LIGHTYELLOW_EX+' '+Style.RESET_ALL               # color of the building when the health is in the range of 20 - 50%
        self.building_color_20  = Back.LIGHTRED_EX+' '+Style.RESET_ALL    
        self.building_color_dead = Back.LIGHTBLACK_EX+' '+Style.RESET_ALL              # color of the building when the health is in the range of 0 - 20%


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
        if self.health[i] <= 0:
            return self.building_color_dead
        elif self.health[i] <= ((20/100)*30):
            return self.building_color_20
        elif self.health[i] <= ((50/100)*30):
            return self.building_color_50
        else:
            return self.building_color_100

    def check_coordinates(self, y, x):
        '''
        This function checks the coordinates of the huts and returns if a hut is present or not
        '''
        for i in range(5):
            if self.y[i] == y and self.x[i] == x and self.health[i] > 0:
                return i

        return -1
    
    def health_decrease(self, i, damage):
        '''
        This function decreases the health of the hut by damage
        '''
        self.health[i] -= damage

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
        if self.health[i] <= 0:
            return self.building_color_dead
        elif self.health[i] <= ((20/100)*100):
            return self.building_color_20
        elif self.health[i] <= ((50/100)*100):
            return self.building_color_50
        else:
            return self.building_color_100

    def check_coordinates(self, y, x):
        '''
        This function checks the coordinates of the cannons and returns if a cannon is present or not
        '''
        for i in range(2):
            for j in range (self.height):
                for k in range (self.width):
                    if self.y[i]+j == y and self.x[i]+k == x and self.health[i] > 0:
                        return i
        return -1

    def health_decrease(self, i, damage):
        '''
        This function decreases the health of the cannon by damage
        '''
        self.health[i] -= damage
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
        This function checks the health of the Townhall and returns the color of the building
        '''
        if self.health[0] <= 0:
            return self.building_color_dead
        elif self.health[0] <= ((20/100)*150):
            return self.building_color_20
        elif self.health[0] <= ((50/100)*150):
            return self.building_color_50
        else:
            return self.building_color_100

    def check_coordinates(self, y, x):
        '''
        This function checks the coordinates of the TownHall and returns if TownHall is present or not
        '''
        for i in range (self.height):
            for j in range (self.width):
                if self.y+i == y and self.x+j == x and self.health > 0:
                    return 1

        return -1

    def health_decrease(self, damage):
        '''
        This function decreases the health of the TownHall by damage
        '''
        self.health -= damage
