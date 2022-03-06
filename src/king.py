from colorama import Fore, Style, Back
import numpy as np
from src.building import TownHall, Hut, Cannon
from src.walls import Walls
from src.utlis import Utils

class King():
    
    def __init__(self, x, y):
        self.king_color = Back.RED+' '+Style.RESET_ALL
        self.x = x
        self.y = y
        self.king_movement_speed = 1            # 1 blocks per command
        
        self.status = 0                         # status = 0 => not spawned
                                                # status = 1 => spawned
                                                # status = 2 => dead

        self.king_health = 100                  # health of the king

        self.king_attack_damage = 20            # damage per each attack



    def move(self, key, walls, huts, cannons, th):
        """Moving king."""
        prev_y = self.y
        prev_x = self.x
        if key == 'w':
            self.y -= self.king_movement_speed
        elif key == 'a':
            self.x -= self.king_movement_speed
        elif key == 's':
            self.y += self.king_movement_speed
        elif key == 'd':
            self.x += self.king_movement_speed
        elif key == 'space':
            self.attack()
        else:
            pass

        # retrace the path if there is a obstacle
        if walls.check_coordinates(self.y, self.x):
            self.y = prev_y
            self.x = prev_x
        elif huts.check_coordinates(self.y, self.x):
            self.y = prev_y
            self.x = prev_x
        elif cannons.check_coordinates(self.y, self.x):
            self.y = prev_y
            self.x = prev_x
        elif th.check_coordinates(self.y, self.x):
            self.y = prev_y
            self.x = prev_x
        elif Utils.check_border_coordinates(self.y, self.x):
            self.y = prev_y
            self.x = prev_x
        

        

    def spawn(self):
        """Spawning king."""
        self.status = 1
        self.x = 5
        self.y = 5
        
    def attack(self):
        """Attacking."""
        pass

    def health_decrease(self, damage):
        """Decrease king's health"""
        self.king_health -= damage
        if self.king_health <= 0:
            self.status = 2