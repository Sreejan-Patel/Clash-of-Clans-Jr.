from colorama import Fore, Style, Back
from src.input import Get, input_to
from src.king import King
from src.troops import Troops
from src.spell import Heal, Rage
import numpy as np
import os

class Village():

    def __init__(self):
        self.rows = 39
        self.cols = 78

        self.troops_spells_rows = 39
        self.troops_spells_cols = 26


        self.village_color = Back.LIGHTCYAN_EX+' '+Style.RESET_ALL
        self.border_color = Back.BLACK+' '+Style.RESET_ALL
        self.village = np.zeros((self.rows, self.cols))
        self.getch = Get()
        self.king = King(self.cols+self.troops_spells_cols - 11,7)
        self.troops = Troops(self.cols,self.cols+self.troops_spells_cols)
        self.rage = Rage(self.cols+self.troops_spells_cols - 11,19)
        self.heal = Heal(self.cols+self.troops_spells_cols - 11,23)

        self.render()

    def get_key(self):
        """Getting key from user."""
        key = input_to(self.getch)
        
        if(key == 'b' and self.king.status == 0):
            self.king.spawn()
        if(key == 'w' or 'a' or 's' or 'd' or 'space' and self.king.status == 1):
            self.king.move(key)
        if(key == 'i' or 'j' or 'k' and self.troops.count < 10):
            self.troops.spawn(key)
        if(key == 'r' ):
            self.rage.cast()
        if(key == 'h' ):
            self.heal.cast()
        return key

    def render(self):
        """Rendering Game Output."""
        os.system('clear')

        # Drawing village
        self.village = [[self.village_color for i in range(self.cols+self.troops_spells_cols)] for j in range(self.rows)]
        
        # Drawing village border
        self.village = np.insert(self.village, 0, self.border_color, axis=0)
        self.village = np.insert(self.village, self.rows+1, self.border_color, axis=0)
        self.village = np.insert(self.village, 0, self.border_color, axis=1)
        self.village = np.insert(self.village, self.cols+1, self.border_color, axis=1)

        # Drawing Troops and King
        length = 1
        troop_spell_color = Back.BLACK+' '+Style.RESET_ALL

        for i in range(self.rows+1):
            for j in range(self.cols+2*length, self.cols+self.troops_spells_cols+2*length):
                self.village[i][j] = troop_spell_color

        troop = "----Troops----"
        troop_len = len(troop)
        troop_x = (self.cols+self.troops_spells_cols - troop_len - 4*length)
        troop_y = 3
        for i in range(troop_len):
            self.village[troop_y][troop_x+i] = Back.BLACK+Fore.YELLOW+troop[i]+Style.RESET_ALL

        troop_king = "--King--"
        troop_king_len = len(troop_king)
        troop_king_x = (self.cols+self.troops_spells_cols - troop_king_len -7*length)
        troop_king_y = 5
        for i in range(troop_king_len):
            self.village[troop_king_y][troop_king_x+i] = Back.BLACK+Fore.YELLOW+troop_king[i]+Style.RESET_ALL

        if self.king.status == 0:
            self.village[self.king.y][self.king.x] = self.king.king_color
        elif self.king.status == 1:
            self.village[self.king.y][self.king.x] = self.king.king_color

        troop_barb = "--Barb--"
        troop_barb_len = len(troop_barb)
        troop_barb_x = (self.cols+self.troops_spells_cols - troop_king_len -7*length)
        troop_barb_y = 9
        for i in range(troop_barb_len):
            self.village[troop_barb_y][troop_barb_x+i] = Back.BLACK+Fore.YELLOW+troop_barb[i]+Style.RESET_ALL        
        
        for counter in range(10):
            if self.troops.status[counter] == 0:
                self.village[self.troops.y[counter]][self.troops.x[counter]] = self.troops.troops_color
            if self.troops.status[counter] == 1:
                self.village[self.troops.y[counter]][self.troops.x[counter]] = self.troops.troops_color
        
        # Drawing Spells
        spells = "----Spells----"
        spells_len = len(spells)
        spells_x = (self.cols+self.troops_spells_cols - spells_len - 4*length)
        spells_y = 15
        for i in range(spells_len):
            self.village[spells_y][spells_x+i] = Back.BLACK+Fore.YELLOW+spells[i]+Style.RESET_ALL

        # Drawing Rage
        rage = "--Rage--"
        rage_len = len(rage)
        rage_x = (self.cols+self.troops_spells_cols - rage_len - 7*length)
        rage_y = 17
        for i in range(rage_len):
            self.village[rage_y][rage_x+i] = Back.BLACK+Fore.YELLOW+rage[i]+Style.RESET_ALL

        if self.rage.status_rage == 0:
            self.village[self.rage.rage_y][self.rage.rage_x] = self.rage.rage_color
        elif self.rage.status_rage == 1:
            self.rage.status_rage = 2
        elif self.rage.status_rage == 2:
            pass


        # Drawing Heal
        heal = "--Heal--"
        heal_len = len(heal)
        heal_x = (self.cols+self.troops_spells_cols - heal_len - 7*length)
        heal_y = 21
        for i in range(heal_len):
            self.village[heal_y][heal_x+i] = Back.BLACK+Fore.YELLOW+heal[i]+Style.RESET_ALL

        if self.heal.status_heal == 0:
            self.village[self.heal.heal_y][self.heal.heal_x] = self.heal.heal_color
        elif self.heal.status_heal == 1:
            self.heal.status_heal = 2
        elif self.heal.status_heal == 2:
            pass


        print('\n'.join([''.join(row) for row in self.village]))


