from colorama import Fore, Style, Back
import numpy as np

class King():
    
    def __init__(self, x, y):
        self.king_color = Back.RED+' '+Style.RESET_ALL
        self.x = x
        self.y = y
        self.status = 0

    def move(self, key):
        """Moving king."""
        if key == 'w':
            self.y -= 1
        elif key == 'a':
            self.x -= 1
        elif key == 's':
            self.y += 1
        elif key == 'd':
            self.x += 1
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

