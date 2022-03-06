from colorama import Fore, Style, Back

class Spell():

    def __init__(self):
        self.rage_color = Back.MAGENTA+' '+Style.RESET_ALL
        self.status_rage = 0
        self.rage_timer = 0
        
        self.heal_color = Back.YELLOW+' '+Style.RESET_ALL
        self.status_heal = 0
        self.heal_timer = 0

class Rage(Spell):

    def __init__(self, x, y):
        Spell.__init__(self)
        self.rage_x = x
        self.rage_y = y

    def cast(self):
        self.status_rage = 1


class Heal(Spell):
    def __init__(self, x, y):
        Spell.__init__(self)
        self.heal_x = x
        self.heal_y = y

    def cast(self):
        self.status_heal = 1
