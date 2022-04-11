from colorama import Fore, Style, Back
import numpy as np
import os
import math
from src.utils import Utils

class Queen():
    
    def __init__(self, x, y, level):
        self.queen_color = Back.RED+' '+Style.RESET_ALL
        self.queen_light_color = Back.LIGHTRED_EX+' '+Style.RESET_ALL
        self.queen_dead_color = Back.LIGHTBLACK_EX+' '+Style.RESET_ALL
        self.x = x
        self.y = y
        self.queen_movement_speed = 1            # 1 blocks per command
        self.queen_dir = 1
        
        self.status = 0                         # status = 0 => not spawned
                                                # status = 1 => spawned
                                                # status = 2 => dead

        self.queen_health = 100                  # health of the king

        self.queen_attack_damage = 15            # damage per each attack

        self.queen_attack_range = 5              # range of the attack
        self.queen_eagle_attack_range = 9       # range of the eagle attack
        
        self.attack_eagle = False                # if the queen is with eagle artillery
        self.eagle_timer = 0
        self.eagle_attack_x = 0
        self.eagle_attack_y = 0

        self.level = level

    def move(self, key, walls, huts, cannons, wizard, th, rage):
        """Moving Queen."""
        prev_y = self.y
        prev_x = self.x
        if rage == 2:
            obstacle = 0
            if key == 'w':
                self.y -= self.queen_movement_speed // 2
            elif key == 'a':
                self.x -= self.queen_movement_speed // 2
            elif key == 's':
                self.y += self.queen_movement_speed // 2
            elif key == 'd':
                self.x += self.queen_movement_speed // 2
            else:
                pass

            if walls.check_coordinates(self.y, self.x) > -1:
                self.y = prev_y
                self.x = prev_x
                obstacle = 1
            elif huts.check_coordinates(self.y, self.x) > -1:
                self.y = prev_y
                self.x = prev_x
                obstacle = 1
            elif cannons.check_coordinates(self.y, self.x) > -1:
                self.y = prev_y
                self.x = prev_x
                obstacle = 1
            elif th.check_coordinates(self.y, self.x) > -1:
                self.y = prev_y
                self.x = prev_x
                obstacle = 1
            elif wizard.check_coordinates(self.y, self.x) > -1:
                self.y = prev_y
                self.x = prev_x
                obstacle = 1
            else:
                obstacle = 2
                self.y = prev_y
                self.x = prev_x

            if obstacle == 2:
                if key == 'w':
                    self.y -= self.queen_movement_speed
                elif key == 'a':
                    self.x -= self.queen_movement_speed
                elif key == 's':
                    self.y += self.queen_movement_speed
                elif key == 'd':
                    self.x += self.queen_movement_speed
                else:
                    pass

                # retrace the path if there is a obstacle
                if walls.check_coordinates(self.y, self.x) > -1:
                    self.y = prev_y
                    self.x = prev_x
                    if rage == 2:
                        if key == 'w':
                            self.y -= self.queen_movement_speed // 2
                        elif key == 'a':
                            self.x -= self.queen_movement_speed // 2
                        elif key == 's':
                            self.y += self.queen_movement_speed // 2
                        elif key == 'd':
                            self.x += self.queen_movement_speed // 2
                        else:
                            pass

                        # retrace the path if there is a obstacle
                        if walls.check_coordinates(self.y, self.x) > -1:
                            self.y = prev_y
                            self.x = prev_x

                elif huts.check_coordinates(self.y, self.x) > -1:
                    self.y = prev_y
                    self.x = prev_x
                    if rage == 2:
                        if key == 'w':
                            self.y -= self.queen_movement_speed // 2
                        elif key == 'a':
                            self.x -= self.queen_movement_speed // 2
                        elif key == 's':
                            self.y += self.queen_movement_speed // 2
                        elif key == 'd':
                            self.x += self.queen_movement_speed // 2
                        else:
                            pass

                        # retrace the path if there is a obstacle
                        if huts.check_coordinates(self.y, self.x) > -1:
                            self.y = prev_y
                            self.x = prev_x
                elif cannons.check_coordinates(self.y, self.x) > -1:
                    self.y = prev_y
                    self.x = prev_x
                    if rage == 2:
                        if key == 'w':
                            self.y -= self.queen_movement_speed // 2
                        elif key == 'a':
                            self.x -= self.queen_movement_speed // 2
                        elif key == 's':
                            self.y += self.queen_movement_speed // 2
                        elif key == 'd':
                            self.x += self.queen_movement_speed // 2
                        else:
                            pass

                        # retrace the path if there is a obstacle
                        if cannons.check_coordinates(self.y, self.x) > -1:
                            self.y = prev_y
                            self.x = prev_x
                elif wizard.check_coordinates(self.y, self.x) > -1:
                    self.y = prev_y
                    self.x = prev_x
                    if rage == 2:
                        if key == 'w':
                            self.y -= self.queen_movement_speed // 2
                        elif key == 'a':
                            self.x -= self.queen_movement_speed // 2
                        elif key == 's':
                            self.y += self.queen_movement_speed // 2
                        elif key == 'd':
                            self.x += self.queen_movement_speed // 2
                        else:
                            pass

                        # retrace the path if there is a obstacle
                        if wizard.check_coordinates(self.y, self.x) > -1:
                            self.y = prev_y
                            self.x = prev_x
                elif th.check_coordinates(self.y, self.x) > -1:
                    self.y = prev_y
                    self.x = prev_x
                    if rage == 2:
                        if key == 'w':
                            self.y -= self.queen_movement_speed // 2
                        elif key == 'a':
                            self.x -= self.queen_movement_speed // 2
                        elif key == 's':
                            self.y += self.queen_movement_speed // 2
                        elif key == 'd':
                            self.x += self.queen_movement_speed // 2
                        else:
                            pass

                        # retrace the path if there is a obstacle
                        if th.check_coordinates(self.y, self.x) > -1:
                            self.y = prev_y
                            self.x = prev_x
                elif Utils.check_border_coordinates(self.y, self.x):
                    self.y = prev_y
                    self.x = prev_x
                    if rage == 2:
                        if key == 'w':
                            self.y -= self.queen_movement_speed // 2
                        elif key == 'a':
                            self.x -= self.queen_movement_speed // 2
                        elif key == 's':
                            self.y += self.queen_movement_speed // 2
                        elif key == 'd':
                            self.x += self.queen_movement_speed // 2
                        else:
                            pass

                        # retrace the path if there is a obstacle
                        if Utils.check_border_coordinates(self.y, self.x):
                            self.y = prev_y
                            self.x = prev_x
                else:
                    pass
            else:
                return
        else:
            if key == 'w':
                self.y -= self.queen_movement_speed
            elif key == 'a':
                self.x -= self.queen_movement_speed
            elif key == 's':
                self.y += self.queen_movement_speed
            elif key == 'd':
                self.x += self.queen_movement_speed
            else:
                pass

            if walls.check_coordinates(self.y, self.x) > -1:
                self.y = prev_y
                self.x = prev_x
            elif huts.check_coordinates(self.y, self.x) > -1:
                self.y = prev_y
                self.x = prev_x
            elif cannons.check_coordinates(self.y, self.x) > -1:
                self.y = prev_y
                self.x = prev_x
            elif th.check_coordinates(self.y, self.x) > -1:
                self.y = prev_y
                self.x = prev_x
            elif wizard.check_coordinates(self.y, self.x) > -1:
                self.y = prev_y
                self.x = prev_x
            else:
                pass

    
        

    def spawn(self):
        """Spawning Queen."""
        self.status = 1
        self.x = 5
        self.y = 5
    
    def euclidean_distance_th(self, y1, x1, y2, x2):
        '''
        This function calculates the euclidean distance between two points (considering the middle y and x coordinates of the th)
        '''
        return math.sqrt((y1-(y2+1))**2 + (x1-(x2+1))**2)

    def euclidean_distance_cannons(self, y1, x1, y2, x2):
        '''
        This function calculates the euclidean distance between two points (considering the middle y and x coordinates of the cannons)
        '''
        return math.sqrt((y1-(y2+1))**2 + (x1-(x2+1))**2)
    
    def euclidean_distance(self, y1, x1, y2, x2):
        '''
        This function calculates the euclidean distance between two points 
        '''
        return math.sqrt((y1-y2)**2 + (x1-x2)**2)
        
    def attack(self, walls, huts, cannons, wizard, th, attack_y, attack_x):
        """Attacking."""
        if self.attack_eagle == 0:
            self.queen_color = Back.BLACK+' '+Style.RESET_ALL

        wall_euclidian_distance = np.full(114, np.inf)
        for i in range(114):
            wall_euclidian_distance[i] = self.euclidean_distance(attack_y, attack_x, walls.y[i], walls.x[i])
        
        huts_euclidian_distance = np.full(5, np.inf)
        for i in range(5):
            huts_euclidian_distance[i] = self.euclidean_distance(attack_y, attack_x, huts.y[i], huts.x[i])
        
        cannons_euclidian_distance = np.full(self.level+1, np.inf)
        for i in range(self.level+1):
            cannons_euclidian_distance[i] = self.euclidean_distance_cannons(attack_y, attack_x, cannons.y[i], cannons.x[i])

        wizard_euclidian_distance = np.full(self.level+1, np.inf)
        for i in range(self.level+1):
            wizard_euclidian_distance[i] = self.euclidean_distance(attack_y, attack_x, wizard.y[i], wizard.x[i])

        th_euclidian_distance = 1000
        th_euclidian_distance = self.euclidean_distance_th(attack_y, attack_x, th.y, th.x)

        if self.attack_eagle == 0:
            for i in range(114):
                if wall_euclidian_distance[i] <= self.queen_attack_range:
                    walls.health[i] = walls.health[i] - self.queen_attack_damage
            
            for i in range(5):
                if huts_euclidian_distance[i] <= self.queen_attack_range:
                    huts.health[i] = huts.health[i] - self.queen_attack_damage
            
            for i in range(self.level+1):
                if cannons_euclidian_distance[i] <= self.queen_attack_range:
                    cannons.health[i] = cannons.health[i] - self.queen_attack_damage
            
            for i in range(self.level+1):
                if wizard_euclidian_distance[i] <= self.queen_attack_range:
                    wizard.health[i] = wizard.health[i] - self.queen_attack_damage
            
            if th_euclidian_distance <= self.queen_attack_range:
                th.health[0] = th.health[0] - self.queen_attack_damage
        else:
            for i in range(114):
                if wall_euclidian_distance[i] <= self.queen_eagle_attack_range:
                    walls.health[i] = walls.health[i] - self.queen_attack_damage
            
            for i in range(5):
                if huts_euclidian_distance[i] <= self.queen_eagle_attack_range:
                    huts.health[i] = huts.health[i] - self.queen_attack_damage
            
            for i in range(self.level+1):
                if cannons_euclidian_distance[i] <= self.queen_eagle_attack_range:
                    cannons.health[i] = cannons.health[i] - self.queen_attack_damage
            
            for i in range(self.level+1):
                if wizard_euclidian_distance[i] <= self.queen_eagle_attack_range:
                    wizard.health[i] = wizard.health[i] - self.queen_attack_damage

            if th_euclidian_distance <= self.queen_eagle_attack_range:
                th.health[0] = th.health[0] - self.queen_attack_damage

        

    
        
        
    def health_check(self):
        """Checking health."""
        if self.queen_health <= 0:
            self.status = 2
            return 
        

    def health_decrease(self, damage):
        """Decrease queen's health"""
        self.queen_health -= damage
        if self.queen_health <= 0:
            self.status = 2

    def health_increase_heal(self):
        """Increase queen's health"""
        self.queen_health = 1.5 * self.queen_health   # heal 150% times
        if self.queen_health > 100:
            self.queen_health = 100