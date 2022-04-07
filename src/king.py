from colorama import Fore, Style, Back
import numpy as np
import os
import math
from src.utlis import Utils

class King():
    
    def __init__(self, x, y, level):
        self.king_color = Back.RED+' '+Style.RESET_ALL
        self.king_light_color = Back.LIGHTRED_EX+' '+Style.RESET_ALL
        self.king_dead_color = Back.LIGHTBLACK_EX+' '+Style.RESET_ALL
        self.x = x
        self.y = y
        self.king_movement_speed = 1            # 1 blocks per command
        
        self.status = 0                         # status = 0 => not spawned
                                                # status = 1 => spawned
                                                # status = 2 => dead

        self.king_health = 100                  # health of the king

        self.king_attack_damage = 20            # damage per each attack

        self.leviathan_range = 4                # range of the leviathan    
        self.leviathan = False

        self.level = level

    def move(self, key, walls, huts, cannons,wizard, th, rage):
        """Moving king."""
        prev_y = self.y
        prev_x = self.x
        if rage == 2:
            obstacle = 0
            if key == 'w':
                self.y -= self.king_movement_speed // 2
            elif key == 'a':
                self.x -= self.king_movement_speed // 2
            elif key == 's':
                self.y += self.king_movement_speed // 2
            elif key == 'd':
                self.x += self.king_movement_speed // 2
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
                    self.y -= self.king_movement_speed
                elif key == 'a':
                    self.x -= self.king_movement_speed
                elif key == 's':
                    self.y += self.king_movement_speed
                elif key == 'd':
                    self.x += self.king_movement_speed
                else:
                    pass

                # retrace the path if there is a obstacle
                if walls.check_coordinates(self.y, self.x) > -1:
                    self.y = prev_y
                    self.x = prev_x
                    if rage == 2:
                        if key == 'w':
                            self.y -= self.king_movement_speed // 2
                        elif key == 'a':
                            self.x -= self.king_movement_speed // 2
                        elif key == 's':
                            self.y += self.king_movement_speed // 2
                        elif key == 'd':
                            self.x += self.king_movement_speed // 2
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
                            self.y -= self.king_movement_speed // 2
                        elif key == 'a':
                            self.x -= self.king_movement_speed // 2
                        elif key == 's':
                            self.y += self.king_movement_speed // 2
                        elif key == 'd':
                            self.x += self.king_movement_speed // 2
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
                            self.y -= self.king_movement_speed // 2
                        elif key == 'a':
                            self.x -= self.king_movement_speed // 2
                        elif key == 's':
                            self.y += self.king_movement_speed // 2
                        elif key == 'd':
                            self.x += self.king_movement_speed // 2
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
                            self.y -= self.king_movement_speed // 2
                        elif key == 'a':
                            self.x -= self.king_movement_speed // 2
                        elif key == 's':
                            self.y += self.king_movement_speed // 2
                        elif key == 'd':
                            self.x += self.king_movement_speed // 2
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
                            self.y -= self.king_movement_speed // 2
                        elif key == 'a':
                            self.x -= self.king_movement_speed // 2
                        elif key == 's':
                            self.y += self.king_movement_speed // 2
                        elif key == 'd':
                            self.x += self.king_movement_speed // 2
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
                            self.y -= self.king_movement_speed // 2
                        elif key == 'a':
                            self.x -= self.king_movement_speed // 2
                        elif key == 's':
                            self.y += self.king_movement_speed // 2
                        elif key == 'd':
                            self.x += self.king_movement_speed // 2
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
                self.y -= self.king_movement_speed
            elif key == 'a':
                self.x -= self.king_movement_speed
            elif key == 's':
                self.y += self.king_movement_speed
            elif key == 'd':
                self.x += self.king_movement_speed
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
        """Spawning king."""
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
        
    def attack(self, walls, huts, cannons, wizard, th):
        """Attacking."""
        self.king_color = Back.BLACK+' '+Style.RESET_ALL

        wall_l = walls.check_coordinates(self.y, self.x-1)
        wall_r = walls.check_coordinates(self.y, self.x+1)
        wall_u = walls.check_coordinates(self.y-1, self.x)
        wall_d = walls.check_coordinates(self.y+1, self.x)
        
        hut_l = huts.check_coordinates(self.y, self.x-1)
        hut_r = huts.check_coordinates(self.y, self.x+1)
        hut_u = huts.check_coordinates(self.y-1, self.x)
        hut_d = huts.check_coordinates(self.y+1, self.x)
        
        cannon_l = cannons.check_coordinates(self.y, self.x-1)
        cannon_r = cannons.check_coordinates(self.y, self.x+1)
        cannon_u = cannons.check_coordinates(self.y-1, self.x)
        cannon_d = cannons.check_coordinates(self.y+1, self.x)
        
        th_l = th.check_coordinates(self.y, self.x-1)
        th_r = th.check_coordinates(self.y, self.x+1)
        th_u = th.check_coordinates(self.y-1, self.x)
        th_d = th.check_coordinates(self.y+1, self.x)

        wizard_l = wizard.check_coordinates(self.y, self.x-1)
        wizard_r = wizard.check_coordinates(self.y, self.x+1)
        wizard_u = wizard.check_coordinates(self.y-1, self.x)
        wizard_d = wizard.check_coordinates(self.y+1, self.x)

        if wall_l != -1:
            walls.health_decrease(wall_l, self.king_attack_damage)
            os.system('afplay sounds/king_attack.wav &')
        elif wall_r != -1:
            walls.health_decrease(wall_r, self.king_attack_damage)
            os.system('afplay sounds/king_attack.wav &')
        elif wall_u != -1:
            walls.health_decrease(wall_u, self.king_attack_damage)
            os.system('afplay sounds/king_attack.wav &')
        elif wall_d != -1:
            walls.health_decrease(wall_d, self.king_attack_damage)
            os.system('afplay sounds/king_attack.wav &')
        elif hut_l != -1:
            huts.health_decrease(hut_l, self.king_attack_damage)
            os.system('afplay sounds/king_attack.wav &')
        elif hut_r != -1:
            huts.health_decrease(hut_r, self.king_attack_damage)
            os.system('afplay sounds/king_attack.wav &')
        elif hut_u != -1:
            huts.health_decrease(hut_u, self.king_attack_damage)
            os.system('afplay sounds/king_attack.wav &')
        elif hut_d != -1:
            huts.health_decrease(hut_d, self.king_attack_damage)
            os.system('afplay sounds/king_attack.wav &')
        elif cannon_l != -1:
            cannons.health_decrease(cannon_l, self.king_attack_damage)
            os.system('afplay sounds/king_attack.wav &')
        elif cannon_r != -1:
            cannons.health_decrease(cannon_r, self.king_attack_damage)
            os.system('afplay sounds/king_attack.wav &')
        elif cannon_u != -1:
            cannons.health_decrease(cannon_u, self.king_attack_damage)
            os.system('afplay sounds/king_attack.wav &')
        elif cannon_d != -1:
            cannons.health_decrease(cannon_d, self.king_attack_damage)
            os.system('afplay sounds/king_attack.wav &')
        elif wizard_l != -1:
            wizard.health_decrease(wizard_l, self.king_attack_damage)
            os.system('afplay sounds/king_attack.wav &')
        elif wizard_r != -1:
            wizard.health_decrease(wizard_r, self.king_attack_damage)
            os.system('afplay sounds/king_attack.wav &')
        elif wizard_u != -1:
            wizard.health_decrease(wizard_u, self.king_attack_damage)
            os.system('afplay sounds/king_attack.wav &')
        elif wizard_d != -1:
            wizard.health_decrease(wizard_d, self.king_attack_damage)
            os.system('afplay sounds/king_attack.wav &')
        elif th_l != -1 or th_r != -1 or th_u != -1 or th_d != -1:
            th.health_decrease(self.king_attack_damage)
            os.system('afplay sounds/king_attack.wav &')

    def attack_leviathan(self,walls,huts,cannons,wizard,th):
        """Attacking leviathan."""
        self.king_color = Back.BLACK+' '+Style.RESET_ALL

        wall_euclidian_distance = np.full(114, np.inf)
        for i in range(114):
            wall_euclidian_distance[i] = self.euclidean_distance(self.y, self.x, walls.y[i], walls.x[i])
        
        huts_euclidian_distance = np.full(5, np.inf)
        for i in range(5):
            huts_euclidian_distance[i] = self.euclidean_distance(self.y, self.x, huts.y[i], huts.x[i])
        
        cannons_euclidian_distance = np.full(self.level+1, np.inf)
        for i in range(self.level+1):
            cannons_euclidian_distance[i] = self.euclidean_distance_cannons(self.y, self.x, cannons.y[i], cannons.x[i])

        wizard_euclidian_distance = np.full(self.level+1, np.inf)
        for i in range(self.level+1):
            wizard_euclidian_distance[i] = self.euclidean_distance_cannons(self.y, self.x, wizard.y[i], wizard.x[i])

        th_euclidian_distance = 1000
        th_euclidian_distance = self.euclidean_distance_th(self.y, self.x, th.y, th.x)

        for i in range(114):
            if wall_euclidian_distance[i] <= self.leviathan_range:
                walls.health[i] = walls.health[i] - self.king_attack_damage
                os.system('afplay sounds/king_attack.wav &')
        
        for i in range(5):
            if huts_euclidian_distance[i] <= self.leviathan_range:
                huts.health[i] = huts.health[i] - self.king_attack_damage
                os.system('afplay sounds/king_attack.wav &')
        for i in range(self.level+1):
            if cannons_euclidian_distance[i] <= self.leviathan_range:
                cannons.health[i] = cannons.health[i] - self.king_attack_damage
                os.system('afplay sounds/king_attack.wav &')
        for i in range(self.level+1):
            if wizard_euclidian_distance[i] <= self.leviathan_range:
                wizard.health[i] = wizard.health[i] - self.king_attack_damage
                os.system('afplay sounds/king_attack.wav &')
        if th_euclidian_distance <= self.leviathan_range:
            th.health[0] = th.health[0] - self.king_attack_damage
            os.system('afplay sounds/king_attack.wav &')
        
    def health_check(self):
        """Checking health."""
        if self.king_health <= 0:
            self.status = 2
            return 
        

    def health_decrease(self, damage):
        """Decrease king's health"""
        self.king_health -= damage
        if self.king_health <= 0:
            self.status = 2

    def health_increase_heal(self):
        """Increase king's health"""
        self.king_health = 1.5 * self.king_health   # heal 150% times
        if self.king_health > 100:
            self.king_health = 100