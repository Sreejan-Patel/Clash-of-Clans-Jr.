from colorama import Fore, Style, Back
import numpy as np
import os
import math
from src.utlis import Utils

class Queen():
    
    def __init__(self, x, y):
        self.queen_color = Back.RED+' '+Style.RESET_ALL
        self.queen_light_color = Back.LIGHTRED_EX+' '+Style.RESET_ALL
        self.queen_dead_color = Back.LIGHTBLACK_EX+' '+Style.RESET_ALL
        self.x = x
        self.y = y
        self.queen_movement_speed = 1            # 1 blocks per command
        
        self.status = 0                         # status = 0 => not spawned
                                                # status = 1 => spawned
                                                # status = 2 => dead

        self.queen_health = 100                  # health of the king

        self.queen_attack_damage = 15            # damage per each attack

    def move(self, key, walls, huts, cannons, th, rage):
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
        
    def attack(self, walls, huts, cannons, th):
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

        elif th_l != -1 or th_r != -1 or th_u != -1 or th_d != -1:
            th.health_decrease(self.king_attack_damage)
            os.system('afplay sounds/king_attack.wav &')

    
        
        
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