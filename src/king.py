from colorama import Fore, Style, Back
import numpy as np

class King():
    
    def __init__(self, x, y):
        self.king_color = Back.RED+' '+Style.RESET_ALL
        self.x = x
        self.y = y
        self.king_movement_speed = 2            # 2 blocks per command
        
        self.status = 0                         # status = 0 => not spawned
                                                # status = 1 => spawned
                                                # status = 2 => dead

        self.king_health = 100                  # health of the king

        self.king_attack_damage = 10            # damage per each attack



    def move(self, key):
        """Moving king."""
        if key == 'w':
            self.y -= 1*self.king_movement_speed
        elif key == 'a':
            self.x -= 1*self.king_movement_speed
        elif key == 's':
            self.y += 1*self.king_movement_speed
        elif key == 'd':
            self.x += 1*self.king_movement_speed
        elif key == 'space':
            self.attack()
        else:
            pass

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
        
