from ast import Str
from colorama import Fore, Style, Back
from src.input import Get, input_to
from src.king import King
from src.troops import Troops
from src.spell import Heal, Rage
from src.building import Hut, Cannon, TownHall
from src.walls import Walls
import numpy as np
import math
import time 
import os

class Village():

    def __init__(self):
        self.rows = 39
        self.cols = 78

        self.troops_spells_rows = 39
        self.troops_spells_cols = 26


        self.base_color = Back.LIGHTWHITE_EX+' '+Style.RESET_ALL
        self.border_color = Back.BLACK+' '+Style.RESET_ALL
        self.getch = Get()

        self.king = King(self.cols+self.troops_spells_cols - 11,7)
        self.troops = Troops(self.cols,self.cols+self.troops_spells_cols)

        self.rage = Rage(self.cols+self.troops_spells_cols - 11,19)
        self.rage_time = 0
        self.heal = Heal(self.cols+self.troops_spells_cols - 11,23)
        self.heal_time = 0

        self.th = TownHall()
        self.huts = Hut()
        self.cannons = Cannon()
        self.walls = Walls()

        self.start_time = time.time()
        self.current_time = time.time()
        self.time_elapsed = 0

        self.game_over = False
        

        self.render()

    def get_key(self):
        """Getting key from user."""
        key = input_to(self.getch)
        
        if(key == 'b' and self.king.status == 0):
            self.king.spawn()
        if(key == 'w' or 'a' or 's' or 'd'):
            if self.king.status == 1:
                self.king.move(key, self.walls, self.huts, self.cannons, self.th)
            else:
                pass
        if(key == ' '):
            if self.king.status == 1:
                self.king.attack(self.walls, self.huts, self.cannons, self.th)
        if(key == 'i' or 'j' or 'k'):
            if self.troops.count < 10:
                self.troops.spawn(key)
            else:
                pass
        if(key == 'r' and self.rage.status_rage == 0):
            self.rage.cast()
        if(key == 'h' and self.heal.status_heal == 0):
            self.heal.cast()
        return key

    def render(self):
        """Rendering Game Output."""
        os.system('clear')

        # render village
        if self.heal.status_heal == 2:
            self.village = [[self.heal.heal_color for i in range(self.cols+self.troops_spells_cols)] for j in range(self.rows)]
        elif self.rage.status_rage == 2:
            self.village = [[self.rage.rage_color for i in range(self.cols+self.troops_spells_cols)] for j in range(self.rows)]
        else:
            self.village = [[self.base_color for i in range(self.cols+self.troops_spells_cols)] for j in range(self.rows)]
        
        # render village border
        self.village = np.insert(self.village, 0, self.border_color, axis=0)
        self.village = np.insert(self.village, self.rows+1, self.border_color, axis=0)
        self.village = np.insert(self.village, 0, self.border_color, axis=1)
        self.village = np.insert(self.village, self.cols+1, self.border_color, axis=1)

        # render Town Hall
        for row in range(self.th.y,self.th.y+self.th.height):
            for col in range(self.th.x,self.th.x+self.th.width):
                self.village[row][col] = self.th.health_check()
        
        # render Huts
        for i in range(5):
            for row in range(self.huts.y[i],self.huts.y[i]+self.huts.height):
                for col in range(self.huts.x[i],self.huts.x[i]+self.huts.width):
                    self.village[row][col] = self.huts.health_check(i)
        
        # render Cannons
        for i in range(2):
            for row in range(self.cannons.y[i],self.cannons.y[i]+self.cannons.height):
                for col in range(self.cannons.x[i],self.cannons.x[i]+self.cannons.width):
                    self.village[row][col] = self.cannons.health_check(i)

        # render walls
        for i in range(114):
            self.village[self.walls.y[i]][self.walls.x[i]] = self.walls.health_check(i)


        # render Troops
        length = 1
        troop_spell_color = Back.LIGHTBLACK_EX+' '+Style.RESET_ALL

        for i in range(self.rows+2):
            for j in range(self.cols+2*length, self.cols+self.troops_spells_cols+2*length):
                self.village[i][j] = troop_spell_color

        troop = "----Troops----"
        troop_len = len(troop)
        troop_x = (self.cols+self.troops_spells_cols - troop_len - 4*length)
        troop_y = 3
        for i in range(troop_len):
            self.village[troop_y][troop_x+i] = Fore.YELLOW+troop[i]+Style.RESET_ALL

        # render King
        troop_king = "--King--"
        troop_king_len = len(troop_king)
        troop_king_x = (self.cols+self.troops_spells_cols - troop_king_len -7*length)
        troop_king_y = 5
        for i in range(troop_king_len):
            self.village[troop_king_y][troop_king_x+i] = Fore.YELLOW+troop_king[i]+Style.RESET_ALL

        king_health = "Health: "
        king_health_len = len(king_health)
        king_health_x = (self.cols+6)
        king_health_y = 7

        health_bar_len = 10
        king_health_length = int(self.king.king_health * health_bar_len / 100)

        if self.king.status == 0:
            self.village[self.king.y][self.king.x] = self.king.king_color
        elif self.king.status == 1:
            self.village[self.king.y][self.king.x] = self.king.king_color
            for i in range(king_health_len):
                self.village[king_health_y][king_health_x+i] = king_health[i]
            for i in range(health_bar_len):
                self.village[king_health_y][king_health_x+i+king_health_len] = Back.BLACK+' '+Style.RESET_ALL
            for i in range(king_health_length):
                self.village[king_health_y][king_health_x+i+king_health_len] = Back.RED+' '+Style.RESET_ALL

        self.king.king_color = Back.RED+' '+Style.RESET_ALL

        # render Barbarians
        troop_barb = "--Barb--"
        troop_barb_len = len(troop_barb)
        troop_barb_x = (self.cols+self.troops_spells_cols - troop_king_len -7*length)
        troop_barb_y = 9
        for i in range(troop_barb_len):
            self.village[troop_barb_y][troop_barb_x+i] = Fore.YELLOW+troop_barb[i]+Style.RESET_ALL        
        
        for counter in range(10):
            if self.troops.status[counter] == 0:
                self.village[self.troops.y[counter]][self.troops.x[counter]] = self.troops.troops_color
            if self.troops.status[counter] == 1:
                self.village[self.troops.y[counter]][self.troops.x[counter]] = self.troops.troops_color
        
        # render Spells
        spells = "----Spells----"
        spells_len = len(spells)
        spells_x = (self.cols+self.troops_spells_cols - spells_len - 4*length)
        spells_y = 15
        for i in range(spells_len):
            self.village[spells_y][spells_x+i] = Fore.YELLOW+spells[i]+Style.RESET_ALL

        # render Rage
        rage = "--Rage--"
        rage_len = len(rage)
        rage_x = (self.cols+self.troops_spells_cols - rage_len - 7*length)
        rage_y = 17
        for i in range(rage_len):
            self.village[rage_y][rage_x+i] = Fore.YELLOW+rage[i]+Style.RESET_ALL

        if self.rage.status_rage == 0:
            self.village[self.rage.rage_y][self.rage.rage_x] = self.rage.rage_color
        elif self.rage.status_rage == 1:
            self.rage.rage_timer = time.time()
            self.rage.status_rage = 2
        elif self.rage.status_rage == 2:
            if self.rage_time >= 5:
                self.rage.status_rage = 3


        # render Heal
        heal = "--Heal--"
        heal_len = len(heal)
        heal_x = (self.cols+self.troops_spells_cols - heal_len - 7*length)
        heal_y = 21
        for i in range(heal_len):
            self.village[heal_y][heal_x+i] = Fore.YELLOW+heal[i]+Style.RESET_ALL

        if self.heal.status_heal == 0:
            self.village[self.heal.heal_y][self.heal.heal_x] = self.heal.heal_color
        elif self.heal.status_heal == 1:
            self.heal.heal_timer = time.time()
            self.heal.status_heal = 2
        elif self.heal.status_heal == 2:
            if self.heal_time >= 5:
                self.heal.status_heal = 3

        if self.game_over == False:
            self.current_time = time.time()
            self.time_elapsed = math.floor(self.current_time - self.start_time)
            if self.heal.status_heal == 2:
                self.heal_time = math.floor(self.current_time - self.heal.heal_timer)
            if self.rage.status_rage == 2:
                self.rage_time = math.floor(self.current_time - self.rage.rage_timer)


        print('\n'.join([''.join(row) for row in self.village]))


