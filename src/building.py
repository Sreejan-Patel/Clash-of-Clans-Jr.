from colorama import Fore , Back , Style
import numpy as np
import math
import time
import os

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
        self.status = np.full((5), 1)
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
        if self.health[i] <= 0:
            self.status[i] = 0

class Cannon(Building):
    
    def __init__(self,level):
        Building.__init__(self)
        self.height = 2
        self.width = 3
        self.health = np.full((5), 100)
        self.y = np.zeros((5), type(int))
        self.x = np.zeros((5), type(int))
        self.level = level
        self.initialize_cannons()
        self.damage = 10
        self.range = 6
        self.status = np.full((5), 1)
        self.cannon_attack = [-1,-1,-1,-1,-1]
        self.cannon_time = [time.time(),time.time(),time.time(),time.time(),time.time()]
        self.cannon_attacking = [0,0,0,0,0]
        self.cannon_ticks = [0,0,0,0,0]
        self.cannon_attack_barb = [0,0,0,0,0]
        self.cannon_attack_archer = [0,0,0,0,0]

        self.attack_status = np.full((5), 0)
        self.attack_color = Back.BLACK+' '+Style.RESET_ALL

    def initialize_cannons(self):
        '''
        This function initializes the cannons
        '''
        if(self.level == 1):
            self.y[0] = 17
            self.x[0] = 23

            self.y[1] = 17
            self.x[1] = 55
        elif(self.level == 2):
            self.y[0] = 17
            self.x[0] = 23

            self.y[1] = 17
            self.x[1] = 55

            self.y[2] = 25
            self.x[2] = 39
        elif(self.level == 3):
            self.y[0] = 17
            self.x[0] = 23

            self.y[1] = 17
            self.x[1] = 55

            self.y[2] = 25
            self.x[2] = 23

            self.y[3] = 25
            self.x[3] = 55

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
        for i in range(self.level+1):
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
        if self.health[i] <= 0:
            self.status[i] = 0

    def euclidean_distance(self, y1, x1, y2, x2):
        '''
        This function calculates the euclidean distance between two points (considering the middle y and x coordinates of the cannon)
        '''
        return math.sqrt((y1-(y2))**2 + (x1-(x2))**2)

    def cannon_attack_troops(self, hero, king, queen, barbarians, archers):
        '''
        This function attacks the troops of the enemy
        '''

        for i in range(self.level+1):
            if self.health[i] <= 0:
                continue
            self.attack_status[i] = 0
            if self.cannon_attacking[i] == 1:
                self.cannon_time[i] = time.time()
                self.cannon_attacking[i] = 2
            
            hero_dist = 0
            if hero == 1:
                hero_dist = self.euclidean_distance(king.y, king.x, self.y[i], self.x[i])
            elif hero == 2:
                hero_dist = self.euclidean_distance(queen.y, queen.x, self.y[i], self.x[i])
            else:
                hero_dist = 1000
            
            barb_dist = np.full((10),100)
            for j in range(10):
                if barbarians.status[j] == 1:
                    barb_dist[j] = barb_dist[j] = self.euclidean_distance(barbarians.y[j], barbarians.x[j], self.y[i], self.x[i])
                else:
                    barb_dist[j] = 1000

            arch_dist = np.full((5),100)
            for j in range(5):
                if archers.status[j] == 1:
                    arch_dist[j] = self.euclidean_distance(archers.y[j], archers.x[j], self.y[i], self.x[i])
                else:
                    arch_dist[j] = 1000
            
            if self.cannon_attack[i] == -1:

                if np.amin(barb_dist) < np.amin(arch_dist) and np.amin(barb_dist) < hero_dist:
                    if barbarians.status[np.argmin(barb_dist)] == 1:
                        self.cannon_time[i] = 0
                        self.cannon_attacking[i] = 1
                        self.cannon_attack[i] = np.argmin(barb_dist)
                        self.cannon_ticks[i] = 0
                        self.cannon_attack_barb[i] = 1
                    else:
                        self.cannon_time[i] = 0
                        self.cannon_attacking[i] = 0
                        self.cannon_attack[i] = -1
                        self.cannon_ticks[i] = 0
                        self.cannon_attack_barb[i] = 0
                elif np.amin(arch_dist) < hero_dist:
                    if archers.status[np.argmin(arch_dist)] == 1:
                        self.cannon_time[i] = 0
                        self.cannon_attacking[i] = 1
                        self.cannon_attack[i] = np.argmin(arch_dist)
                        self.cannon_ticks[i] = 0
                        self.cannon_attack_archer[i] = 1
                    else:
                        self.cannon_time[i] = 0
                        self.cannon_attacking[i] = 0
                        self.cannon_attack[i] = -1
                        self.cannon_ticks[i] = 0
                        self.cannon_attack_archer[i] = 0
                else:
                    if hero == 1:
                        if king.status == 1:
                            self.cannon_time[i] = 0
                            self.cannon_attacking[i] = 1
                            self.cannon_attack[i] = 69
                            self.cannon_ticks[i] = 0
                        else:
                            self.cannon_time[i] = 0
                            self.cannon_attacking[i] = 0
                            self.cannon_attack[i] = -1
                            self.cannon_ticks[i] = 0
                    elif hero == 2:
                        if queen.status == 1:
                            self.cannon_time[i] = 0
                            self.cannon_attacking[i] = 1
                            self.cannon_attack[i] = 69
                            self.cannon_ticks[i] = 0
                        else:
                            self.cannon_time[i] = 0
                            self.cannon_attacking[i] = 0
                            self.cannon_attack[i] = -1
                            self.cannon_ticks[i] = 0
            
            elif self.cannon_attack[i] == 69:
                if hero == 1:
                    if king.status == 1:
                        king_dist = self.euclidean_distance(king.y,king.x,self.y[i],self.x[i])
                        if king_dist <= self.range:
                                if math.floor(time.time() - self.cannon_time[i]) == self.cannon_ticks[i]:
                                    self.attack_status[i] = 1
                                    self.cannon_ticks[i] += 1
                                    king.king_health -= self.damage
                                    if king.king_health <= 0:
                                        os.system('afplay sounds/king_die.wav -t 1 &')
                                        king.status = 2
                                        self.cannon_attack[i] = -1
                                        self.cannon_attacking[i] = 0
                                        self.cannon_ticks[i] = 0
                                        self.cannon_time[i] = 0
                        else:
                            self.cannon_attack[i] = -1
                            self.cannon_attacking[i] = 0
                            self.cannon_ticks[i] = 0
                            self.cannon_time[i] = 0
                elif hero == 2:
                    if queen.status == 1:
                        queen_dist = self.euclidean_distance(queen.y,queen.x,self.y[i],self.x[i])
                        if queen_dist <= self.range:
                                if math.floor(time.time() - self.cannon_time[i]) == self.cannon_ticks[i]:
                                    self.attack_status[i] = 1
                                    self.cannon_ticks[i] += 1
                                    queen.queen_health -= self.damage
                                    if queen.queen_health <= 0:
                                        os.system('afplay sounds/queen_die.wav -t 1 &')
                                        queen.status = 2
                                        self.cannon_attack[i] = -1
                                        self.cannon_attacking[i] = 0
                                        self.cannon_ticks[i] = 0
                                        self.cannon_time[i] = 0
                        else:
                            self.cannon_attack[i] = -1
                            self.cannon_attacking[i] = 0
                            self.cannon_ticks[i] = 0
                            self.cannon_time[i] = 0

            else:
                if self.cannon_attack_barb[i] == 1:
                    for j in range(10):

                        if self.cannon_attack[i] == j:
                            if barbarians.status[j] == 1:
                                barb_dist[j] = self.euclidean_distance(barbarians.y[j],barbarians.x[j],self.y[i],self.x[i])
                                if barb_dist[j] <= self.range:
                                        if math.floor(time.time() - self.cannon_time[i]) == self.cannon_ticks[i]:
                                            self.attack_status[i] = 1
                                            self.cannon_ticks[i] +=1
                                            barbarians.health[j] -= self.damage
                                            if barbarians.health[j] <= 0:
                                                barbarians.status[j] = 2
                                                self.cannon_attack[i] = -1
                                                self.cannon_attacking[i] = 0
                                                self.cannon_ticks[i] = 0
                                                self.cannon_time[i] = 0
                                                self.cannon_attack_barb[i] = 0
                                else:
                                    self.cannon_attack[i] = -1
                                    self.cannon_attacking[i] = 0
                                    self.cannon_ticks[i] = 0
                                    self.cannon_time[i] = 0
                                    self.cannon_attack_barb[i] = 0
                        else:
                            continue
                elif self.cannon_attack_archer[i] == 1:
                    for j in range(10):
                        if self.cannon_attack[i] == j:
                            if archers.status[j] == 1:
                                arch_dist[j] = self.euclidean_distance(archers.y[j],archers.x[j],self.y[i],self.x[i])
                                if arch_dist[j] <= self.range:
                                        if math.floor(time.time() - self.cannon_time[i]) == self.cannon_ticks[i]:
                                            self.attack_status[i] = 1
                                            self.cannon_ticks[i] +=1
                                            archers.health[j] -= self.damage
                                            if archers.health[j] <= 0:
                                                archers.status[j] = 2
                                                self.cannon_attack[i] = -1
                                                self.cannon_attacking[i] = 0
                                                self.cannon_ticks[i] = 0
                                                self.cannon_time[i] = 0
                                                self.cannon_attack_archer[i] = 0
                                else:
                                    self.cannon_attack[i] = -1
                                    self.cannon_attacking[i] = 0
                                    self.cannon_ticks[i] = 0
                                    self.cannon_time[i] = 0
                                    self.cannon_attack_archer[i] = 0
                        else:
                            continue

class WizardTower(Building):

    def __init__(self,level):
        Building.__init__(self)
        self.height = 3
        self.width = 3
        self.health = np.full((5), 100)
        self.y = np.zeros((5), type(int))
        self.x = np.zeros((5), type(int))
        self.level = level
        self.initialize_wizard_tower()
        self.damage = 10
        self.range = 6
        self.aoe = 3
        self.status = np.full((5), 1)
        self.wizard_attack = [-1,-1,-1,-1,-1]
        self.wizard_time = [time.time(),time.time(),time.time(),time.time(),time.time()]
        self.wizard_attacking = [0,0,0,0,0]
        self.wizard_ticks = [0,0,0,0,0]
        self.wizard_attack_barb = [0,0,0,0,0]
        self.wizard_attack_archer = [0,0,0,0,0]
        self.wizard_attack_loon = [0,0,0,0,0]

        self.attack_status = np.full((5), 0)
        self.attack_color = Back.BLACK+' '+Style.RESET_ALL
    
    def initialize_wizard_tower(self):
        '''
        This function initializes the wizard towers
        '''
        if(self.level == 1):
            self.y[0] = 25
            self.x[0] = 23

            self.y[1] = 25
            self.x[1] = 55
        elif(self.level == 2):
            self.y[0] = 25
            self.x[0] = 23

            self.y[1] = 25
            self.x[1] = 55

            self.y[2] = 16
            self.x[2] = 39
        elif(self.level == 3):
            self.y[0] = 16
            self.x[0] = 39

            self.y[1] = 25
            self.x[1] = 39

            self.y[2] = 20
            self.x[2] = 31

            self.y[3] = 20
            self.x[3] = 47

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
        This function checks the coordinates of the wizard towers and returns if a wizard tower is present or not
        '''
        for i in range(self.level+1):
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
        if self.health[i] <= 0:
            self.status[i] = 0

    def euclidean_distance(self, y1, x1, y2, x2):
        '''
        This function calculates the euclidean distance between two points (considering the middle y and x coordinates of the wizard tower)
        '''
        return math.sqrt((y1-(y2+1))**2 + (x1-(x2+1))**2)

    def euclidean_distance_attack(self, y1, x1, y2, x2):
        '''
        This function calculates the euclidean distance between two points (considering the middle y and x coordinates of the wizard tower)
        '''
        return math.sqrt((y1-(y2))**2 + (x1-(x2))**2)    

    def wizard_attack_troops(self, hero, king, queen, barbarians, archers, loon):
        '''
        This function attacks the troops of the enemy
        '''

        for i in range(self.level+1):
            if self.health[i] <= 0:
                continue
            self.attack_status[i] = 0
            if self.wizard_attacking[i] == 1:
                self.wizard_time[i] = time.time()
                self.wizard_attacking[i] = 2
            
            hero_dist = 0
            if hero == 1:
                hero_dist = self.euclidean_distance(king.y, king.x, self.y[i], self.x[i])
            elif hero == 2:
                hero_dist = self.euclidean_distance(queen.y, queen.x, self.y[i], self.x[i])
            else:
                hero_dist = 1000
            
            barb_dist = np.full((10),100)
            for j in range(10):
                if barbarians.status[j] == 1:
                    barb_dist[j] = barb_dist[j] = self.euclidean_distance(barbarians.y[j], barbarians.x[j], self.y[i], self.x[i])
                else:
                    barb_dist[j] = 1000

            arch_dist = np.full((5),100)
            for j in range(5):
                if archers.status[j] == 1:
                    arch_dist[j] = self.euclidean_distance(archers.y[j], archers.x[j], self.y[i], self.x[i])
                else:
                    arch_dist[j] = 1000

            loon_dist = np.full((2),100)
            for j in range(2):
                if loon.status[j] == 1:
                    loon_dist[j] = self.euclidean_distance(loon.y[j], loon.x[j], self.y[i], self.x[i])
                else:
                    loon_dist[j] = 1000

            if self.wizard_attack[i] == -1:

                if np.amin(barb_dist) < np.amin(arch_dist) and np.amin(barb_dist) < np.amin(loon_dist) and np.amin(barb_dist) < hero_dist:
                    if barbarians.status[np.argmin(barb_dist)] == 1:
                        self.wizard_time[i] = 0
                        self.wizard_attacking[i] = 1
                        self.wizard_attack[i] = np.argmin(barb_dist)
                        self.wizard_ticks[i] = 0
                        self.wizard_attack_barb[i] = 1
                    else:
                        self.wizard_time[i] = 0
                        self.wizard_attacking[i] = 0
                        self.wizard_attack[i] = -1
                        self.wizard_ticks[i] = 0
                        self.wizard_attack_barb[i] = 0
                elif np.amin(arch_dist) < np.amin(loon_dist) and np.amin(arch_dist) < hero_dist:
                    if archers.status[np.argmin(arch_dist)] == 1:
                        self.wizard_time[i] = 0
                        self.wizard_attacking[i] = 1
                        self.wizard_attack[i] = np.argmin(arch_dist)
                        self.wizard_ticks[i] = 0
                        self.wizard_attack_archer[i] = 1
                    else:
                        self.wizard_time[i] = 0
                        self.wizard_attacking[i] = 0
                        self.wizard_attack[i] = -1
                        self.wizard_ticks[i] = 0
                        self.wizard_attack_archer[i] = 0
                elif np.amin(loon_dist) < hero_dist:
                    if loon.status[np.argmin(loon_dist)] == 1:
                        self.wizard_time[i] = 0
                        self.wizard_attacking[i] = 1
                        self.wizard_attack[i] = np.argmin(loon_dist)
                        self.wizard_ticks[i] = 0
                        self.wizard_attack_loon[i] = 1
                    else:
                        self.wizard_time[i] = 0
                        self.wizard_attacking[i] = 0
                        self.wizard_attack[i] = -1
                        self.wizard_ticks[i] = 0
                        self.wizard_attack_loon[i] = 0
                else:
                    if hero == 1:
                        if king.status == 1:
                            self.wizard_time[i] = 0
                            self.wizard_attacking[i] = 1
                            self.wizard_attack[i] = 69
                            self.wizard_ticks[i] = 0
                        else:
                            self.wizard_time[i] = 0
                            self.wizard_attacking[i] = 0
                            self.wizard_attack[i] = -1
                            self.wizard_ticks[i] = 0
                    elif hero == 2:
                        if queen.status == 1:
                            self.wizard_time[i] = 0
                            self.wizard_attacking[i] = 1
                            self.wizard_attack[i] = 69
                            self.wizard_ticks[i] = 0
                        else:
                            self.wizard_time[i] = 0
                            self.wizard_attacking[i] = 0
                            self.wizard_attack[i] = -1
                            self.wizard_ticks[i] = 0
            
            elif self.wizard_attack[i] == 69:
                if hero == 1:
                    if king.status == 1:
                        king_dist = self.euclidean_distance(king.y,king.x,self.y[i],self.x[i])
                        if king_dist <= self.range:
                                if math.floor(time.time() - self.wizard_time[i]) == self.wizard_ticks[i]:
                                    self.attack_status[i] = 1
                                    self.wizard_ticks[i] += 1
                                    king.king_health -= self.damage
                                    euclidean_distances_barb = np.full((10),100)
                                    for j in range(10):
                                        euclidean_distances_barb[j] = self.euclidean_distance_attack(barbarians.y[j], barbarians.x[j], king.y, king.x)
                                        if euclidean_distances_barb[j] <= self.aoe:
                                            barbarians.health[j] -= self.damage
                                            if barbarians.health[j] <= 0:
                                                barbarians.health[j] = 2
                                    
                                    euclidean_distances_arch = np.full((5),100)
                                    for j in range(5):
                                        euclidean_distances_arch[j] = self.euclidean_distance_attack(archers.y[j], archers.x[j], king.y, king.x)
                                        if euclidean_distances_arch[j] <= self.aoe:
                                            archers.health[j] -= self.damage
                                            if archers.health[j] <= 0:
                                                archers.health[j] = 2

                                    euclidean_distances_loons = np.full((2),100)
                                    for j in range(2):
                                        euclidean_distances_loons[j] = self.euclidean_distance_attack(loon.y[j], loon.x[j], king.y, king.x)
                                        if euclidean_distances_loons[j] <= self.aoe:
                                            loon.health[j] -= self.damage
                                            if loon.health[j] <= 0:
                                                loon.health[j] = 2

                                    if king.king_health <= 0:
                                        os.system('afplay sounds/king_die.wav -t 1 &')
                                        king.status = 2
                                        self.wizard_attack[i] = -1
                                        self.wizard_attacking[i] = 0
                                        self.wizard_ticks[i] = 0
                                        self.wizard_time[i] = 0
                        else:
                            self.wizard_attack[i] = -1
                            self.wizard_attacking[i] = 0
                            self.wizard_ticks[i] = 0
                            self.wizard_time[i] = 0
                elif hero == 2:
                    if queen.status == 1:
                        queen_dist = self.euclidean_distance(queen.y,queen.x,self.y[i],self.x[i])
                        if queen_dist <= self.range:
                                if math.floor(time.time() - self.wizard_time[i]) == self.wizard_ticks[i]:
                                    self.attack_status[i] = 1
                                    self.wizard_ticks[i] += 1
                                    queen.queen_health -= self.damage
                                    euclidean_distances_barb = np.full((10),100)
                                    for j in range(10):
                                        euclidean_distances_barb[j] = self.euclidean_distance_attack(barbarians.y[j], barbarians.x[j], king.y, king.x)
                                        if euclidean_distances_barb[j] <= self.aoe:
                                            barbarians.health[j] -= self.damage
                                            if barbarians.health[j] <= 0:
                                                barbarians.health[j] = 2
                                    
                                    euclidean_distances_arch = np.full((5),100)
                                    for j in range(5):
                                        euclidean_distances_arch[j] = self.euclidean_distance_attack(archers.y[j], archers.x[j], king.y, king.x)
                                        if euclidean_distances_arch[j] <= self.aoe:
                                            archers.health[j] -= self.damage
                                            if archers.health[j] <= 0:
                                                archers.health[j] = 2

                                    euclidean_distances_loons = np.full((2),100)
                                    for j in range(2):
                                        euclidean_distances_loons[j] = self.euclidean_distance_attack(loon.y[j], loon.x[j], king.y, king.x)
                                        if euclidean_distances_loons[j] <= self.aoe:
                                            loon.health[j] -= self.damage
                                            if loon.health[j] <= 0:
                                                loon.health[j] = 2
                                    if queen.queen_health <= 0:
                                        queen.status = 2
                                        self.wizard_attack[i] = -1
                                        self.wizard_attacking[i] = 0
                                        self.wizard_ticks[i] = 0
                                        self.wizard_time[i] = 0
                        else:
                            self.wizard_attack[i] = -1
                            self.wizard_attacking[i] = 0
                            self.wizard_ticks[i] = 0
                            self.wizard_time[i] = 0

            else:
                if self.wizard_attack_barb[i] == 1:
                    for j in range(10):

                        if self.wizard_attack[i] == j:
                            if barbarians.status[j] == 1:
                                barb_dist[j] = self.euclidean_distance(barbarians.y[j],barbarians.x[j],self.y[i],self.x[i])
                                if barb_dist[j] <= self.range:
                                        if math.floor(time.time() - self.wizard_time[i]) == self.wizard_ticks[i]:
                                            self.attack_status[i] = 1
                                            self.wizard_ticks[i] +=1
                                            barbarians.health[j] -= self.damage
                                            euclidean_distances_barb = np.full((10),100)
                                            for k in range(10):
                                                if k != j:
                                                    euclidean_distances_barb[k] = self.euclidean_distance_attack(barbarians.y[k], barbarians.x[k], barbarians.y[j], barbarians.x[j])
                                                    if euclidean_distances_barb[k] <= self.aoe:
                                                        barbarians.health[k] -= self.damage
                                                        if barbarians.health[k] <= 0:
                                                            barbarians.health[k] = 2
                                                else:
                                                    pass
                                            
                                            euclidean_distances_arch = np.full((5),100)
                                            for k in range(5):
                                                euclidean_distances_arch[k] = self.euclidean_distance_attack(archers.y[k], archers.x[k], barbarians.y[j], barbarians.x[j])
                                                if euclidean_distances_arch[k] <= self.aoe:
                                                    archers.health[k] -= self.damage
                                                    if archers.health[k] <= 0:
                                                        archers.health[k] = 2
                                                
                                            euclidean_distances_loons = np.full((2),100)
                                            for k in range(2):
                                                euclidean_distances_loons[k] = self.euclidean_distance_attack(loon.y[k], loon.x[k], barbarians.y[j], barbarians.x[j])
                                                if euclidean_distances_loons[k] <= self.aoe:
                                                    loon.health[k] -= self.damage
                                                    if loon.health[k] <= 0:
                                                        loon.health[k] = 2

                                            hero_distance = 1000
                                            if hero == 1:
                                                if king.status == 1:
                                                    hero_distance = self.euclidean_distance_attack(king.y,king.x,barbarians.y[j],barbarians.x[j])
                                                    if hero_distance <= self.aoe:
                                                        king.king_health -= self.damage
                                                        if king.king_health <= 0:
                                                            os.system('afplay sounds/king_die.wav -t 1 &')
                                                            king.status = 2

                                            elif hero == 2:
                                                if queen.status == 1:
                                                    hero_distance = self.euclidean_distance_attack(queen.y,queen.x,barbarians.y[j],barbarians.x[j])
                                                    if hero_distance <= self.aoe:
                                                        queen.queen_health -= self.damage
                                                        if queen.queen_health <= 0:
                                                            queen.status = 2

                                            if barbarians.health[j] <= 0:
                                                barbarians.status[j] = 2
                                                self.wizard_attack[i] = -1
                                                self.wizard_attacking[i] = 0
                                                self.wizard_ticks[i] = 0
                                                self.wizard_time[i] = 0
                                                self.wizard_attack_barb[i] = 0
                                else:
                                    self.wizard_attack[i] = -1
                                    self.wizard_attacking[i] = 0
                                    self.wizard_ticks[i] = 0
                                    self.wizard_time[i] = 0
                                    self.wizard_attack_barb[i] = 0
                        else:
                            continue
                
                elif self.wizard_attack_archer[i] == 1:
                    for j in range(5):

                        if self.wizard_attack[i] == j:
                            if archers.status[j] == 1:
                                arch_dist[j] = self.euclidean_distance(archers.y[j],archers.x[j],self.y[i],self.x[i])
                                if arch_dist[j] <= self.range:
                                        if math.floor(time.time() - self.wizard_time[i]) == self.wizard_ticks[i]:
                                            self.attack_status[i] = 1
                                            self.wizard_ticks[i] +=1
                                            archers.health[j] -= self.damage
                                            euclidean_distances_arch = np.full((5),100)
                                            for k in range(5):
                                                if k != j:
                                                    euclidean_distances_arch[k] = self.euclidean_distance_attack(archers.y[k], archers.x[k], archers.y[j], archers.x[j])
                                                    if euclidean_distances_arch[k] <= self.aoe:
                                                        archers.health[k] -= self.damage
                                                        if archers.health[k] <= 0:
                                                            archers.health[k] = 2
                                                else:
                                                    pass
                                            
                                            euclidean_distances_barb = np.full((10),100)
                                            for k in range(10):
                                                euclidean_distances_barb[k] = self.euclidean_distance_attack(barbarians.y[k], barbarians.x[k], archers.y[j], archers.x[j])
                                                if euclidean_distances_barb[k] <= self.aoe:
                                                    barbarians.health[k] -= self.damage
                                                    if barbarians.health[k] <= 0:
                                                        barbarians.health[k] = 2
                                                
                                            euclidean_distances_loons = np.full((2),100)
                                            for k in range(2):
                                                euclidean_distances_loons[k] = self.euclidean_distance_attack(loon.y[k], loon.x[k], archers.y[j], archers.x[j])
                                                if euclidean_distances_loons[k] <= self.aoe:
                                                    loon.health[k] -= self.damage
                                                    if loon.health[k] <= 0:
                                                        loon.health[k] = 2
                                            
                                            hero_distance = 1000
                                            if hero == 1:
                                                if king.status == 1:
                                                    hero_distance = self.euclidean_distance_attack(king.y,king.x,barbarians.y[j],barbarians.x[j])
                                                    if hero_distance <= self.aoe:
                                                        king.king_health -= self.damage
                                                        if king.king_health <= 0:
                                                            os.system('afplay sounds/king_die.wav -t 1 &')
                                                            king.status = 2

                                            elif hero == 2:
                                                if queen.status == 1:
                                                    hero_distance = self.euclidean_distance_attack(queen.y,queen.x,barbarians.y[j],barbarians.x[j])
                                                    if hero_distance <= self.aoe:
                                                        queen.queen_health -= self.damage
                                                        if queen.queen_health <= 0:
                                                            queen.status = 2

                                            if archers.health[j] <= 0:
                                                archers.status[j] = 2
                                                self.wizard_attack[i] = -1
                                                self.wizard_attacking[i] = 0
                                                self.wizard_ticks[i] = 0
                                                self.wizard_time[i] = 0
                                                self.wizard_attack_archer[i] = 0
                                else:
                                    self.wizard_attack[i] = -1
                                    self.wizard_attacking[i] = 0
                                    self.wizard_ticks[i] = 0
                                    self.wizard_time[i] = 0
                                    self.wizard_attack_archer[i] = 0
                        else:
                            continue

                elif self.wizard_attack_loon[i] == 1:
                    for j in range(2):

                        if self.wizard_attack[i] == j:
                            if loon.status[j] == 1:
                                loon_dist[j] = self.euclidean_distance(loon.y[j],loon.x[j],self.y[i],self.x[i])
                                if loon_dist[j] <= self.range:
                                        if math.floor(time.time() - self.wizard_time[i]) == self.wizard_ticks[i]:
                                            self.attack_status[i] = 1
                                            self.wizard_ticks[i] +=1
                                            loon.health[j] -= self.damage
                                            euclidean_distances_loons = np.full((2),100)
                                            for k in range(2):
                                                if k != j:
                                                    euclidean_distances_loons[k] = self.euclidean_distance_attack(loon.y[k], loon.x[k], loon.y[j], loon.x[j])
                                                    if euclidean_distances_loons[k] <= self.aoe:
                                                        loon.health[k] -= self.damage
                                                        if loon.health[k] <= 0:
                                                            loon.health[k] = 2
                                                else:
                                                    pass
                                            
                                            euclidean_distances_barb = np.full((10),100)
                                            for k in range(10):
                                                euclidean_distances_barb[k] = self.euclidean_distance_attack(barbarians.y[k], barbarians.x[k], loon.y[j], loon.x[j])
                                                if euclidean_distances_barb[k] <= self.aoe:
                                                    barbarians.health[k] -= self.damage
                                                    if barbarians.health[k] <= 0:
                                                        barbarians.health[k] = 2
                                            
                                            euclidean_distances_arch = np.full((5),100)
                                            for k in range(5):
                                                euclidean_distances_arch[k] = self.euclidean_distance_attack(archers.y[k], archers.x[k], loon.y[j], loon.x[j])
                                                if euclidean_distances_arch[k] <= self.aoe:
                                                    archers.health[k] -= self.damage
                                                    if archers.health[k] <= 0:
                                                        archers.health[k] = 2

                                            hero_distance = 1000
                                            if hero == 1:
                                                if king.status == 1:
                                                    hero_distance = self.euclidean_distance_attack(king.y,king.x,loon.y[j],loon.x[j])
                                                    if hero_distance <= self.aoe:
                                                        king.king_health -= self.damage
                                                        if king.king_health <= 0:
                                                            os.system('afplay sounds/king_die.wav -t 1 &')
                                                            king.status = 2

                                            elif hero == 2:
                                                if queen.status == 1:
                                                    hero_distance = self.euclidean_distance_attack(queen.y,queen.x,loon.y[j],loon.x[j])
                                                    if hero_distance <= self.aoe:
                                                        queen.queen_health -= self.damage
                                                        if queen.queen_health <= 0:
                                                            queen.status = 2

                                            if loon.health[j] <= 0:
                                                loon.status[j] = 2
                                                self.wizard_attack[i] = -1
                                                self.wizard_attacking[i] = 0
                                                self.wizard_ticks[i] = 0
                                                self.wizard_time[i] = 0
                                                self.wizard_attack_loon[i] = 0
                                else:
                                    self.wizard_attack[i] = -1
                                    self.wizard_attacking[i] = 0
                                    self.wizard_ticks[i] = 0
                                    self.wizard_time[i] = 0
                                    self.wizard_attack_loon[i] = 0
                        else:
                            continue

class TownHall(Building):

    def __init__(self):
        Building.__init__(self)
        self.height = 4
        self.width = 3
        self.health = np.full((1), 150)
        self.x = 39
        self.y = 20
        self.status = 1

        
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
                if self.y+i == y and self.x+j == x and self.health[0] > 0:
                    return 1

        return -1

    def health_decrease(self, damage):
        '''
        This function decreases the health of the TownHall by damage
        '''
        self.health[0] -= damage
        if self.health[0] <= 0:
            self.status = 0