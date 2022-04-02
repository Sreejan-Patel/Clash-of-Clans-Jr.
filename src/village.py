from colorama import Fore, Style, Back
from src.input import Get, input_to
from src.king import King
from src.queen import Queen
from src.troops import Archers, Barbarians, Loons
from src.spell import Heal, Rage
from src.building import Hut, Cannon, TownHall, WizardTower
from src.walls import Walls
import numpy as np
import math
import time 
import os

class Village():

    def __init__(self,level):
        self.level = level

        self.rows = 39
        self.cols = 78

        self.troops_spells_rows = 39
        self.troops_spells_cols = 26


        self.base_color = Back.LIGHTWHITE_EX+' '+Style.RESET_ALL
        self.border_color = Back.BLACK+' '+Style.RESET_ALL
        self.getch = Get()

        self.hero = 0
        self.king = King(self.cols+self.troops_spells_cols - 11,7)
        self.queen = Queen(self.cols+self.troops_spells_cols - 11,7)

        self.barbarians = Barbarians(self.cols,self.cols+self.troops_spells_cols)
        self.archers = Archers(self.cols,self.cols+self.troops_spells_cols)
        self.loons = Loons(self.cols,self.cols+self.troops_spells_cols)

        self.rage = Rage(self.cols+self.troops_spells_cols - 11,25)
        self.rage_time = 0
        self.rage_color = Back.LIGHTMAGENTA_EX+' '+Style.RESET_ALL
        self.heal = Heal(self.cols+self.troops_spells_cols - 11,29)
        self.heal_time = 0
        self.heal_color = Back.LIGHTYELLOW_EX+' '+Style.RESET_ALL

        self.th = TownHall()
        self.huts = Hut()
        self.cannons = Cannon(level)
        self.walls = Walls()
        self.wizard_tower = WizardTower(level)

        self.start_time = time.time()
        self.current_time = time.time()
        self.time_elapsed = 0

        self.game_result = 0
        self.replay_number = 0
        
        self.initialize_replay()

        self.render()

    def get_key(self):
        """Getting key from user."""
        key = input_to(self.getch)
        
        if self.hero == 0:
            if(key == 'b' and self.king.status == 0):
                self.king.spawn()
                self.hero = 1
            if(key == 'q' and self.queen.status == 0):
                self.queen.spawn()
                self.hero = 2
        if(key == 'w' or 'a' or 's' or 'd'):
            if self.king.status == 1:
                self.king.move(key, self.walls, self.huts, self.cannons, self.th, self.rage.status_rage)
            elif self.queen.status == 1:
                if key == 'w':
                    self.queen.queen_dir = 1
                elif key == 'a':
                    self.queen.queen_dir = 2
                elif key == 's':
                    self.queen.queen_dir = 3
                elif key == 'd':
                    self.queen.queen_dir = 4
                self.queen.move(key, self.walls, self.huts, self.cannons, self.th, self.rage.status_rage)
            else:
                pass
        if(key == ' '):
            if self.king.status == 1:
                self.king.attack(self.walls, self.huts, self.cannons, self.th)
            elif self.queen.status == 1:
                attack_y = 0
                attack_x = 0
                if self.queen.queen_dir == 1:
                    attack_y = self.queen.y - 8
                    attack_x = self.queen.x
                    self.queen.attack(self.walls, self.huts, self.cannons, self.th, attack_y, attack_x)
                elif self.queen.queen_dir == 2:
                    attack_y = self.queen.y
                    attack_x = self.queen.x - 8
                    self.queen.attack(self.walls, self.huts, self.cannons, self.th, attack_y, attack_x)
                elif self.queen.queen_dir == 3:
                    attack_y = self.queen.y + 8
                    attack_x = self.queen.x
                    self.queen.attack(self.walls, self.huts, self.cannons, self.th, attack_y, attack_x)
                elif self.queen.queen_dir == 4:
                    attack_y = self.queen.y
                    attack_x = self.queen.x + 8 
                    self.queen.attack(self.walls, self.huts, self.cannons, self.th, attack_y, attack_x)
        
        
        if(key == 'i' or 'j' or 'k'):
            if self.barbarians.count < 10:
                self.barbarians.spawn(key)
            else:
                pass
        if(key == 'm' or 'n' or 'o'):
            if self.archers.count < 5:
                self.archers.spawn(key)
            else:
                pass
        if(key == 'x' or 'y' or 'z'):
            if self.loons.count < 3:
                self.loons.spawn(key)
            else:
                pass        
        
        
                
        if(key == 'r' and self.rage.status_rage == 0):
            self.rage.cast()
        if(key == 'h' and self.heal.status_heal == 0):
            self.heal.cast()
        if(key == 'l'):
            if self.king.status == 1:
                self.king.attack_leviathan(self.walls, self.huts, self.cannons, self.th)
        if(key == 'e'):
            if self.queen.status == 1:
                if self.queen.attack_eagle == 0:
                    self.queen.attack_eagle = 1
                    self.queen.eagle_timer = time.time()
                    self.queen.eagle_attack_x = self.queen.x
                    self.queen.eagle_attack_y = self.queen.y

                
        return key

    def initialize_replay(self):
        """Initialize replay."""
        fname = 'replay_'+str(self.replay_number)+'.txt'
        fpath = './replays/'+fname
        while os.path.exists(fpath):
            self.replay_number += 1
            fname = 'replay_'+str(self.replay_number)+'.txt'
            fpath = './replays/'+fname

    

    def render(self):
        """Rendering Game Output."""
        os.system('clear')

        # render village
        if self.heal.status_heal == 2:
            self.village = [[self.heal_color for i in range(self.cols+self.troops_spells_cols)] for j in range(self.rows)]
        elif self.rage.status_rage == 2:
            self.village = [[self.rage_color for i in range(self.cols+self.troops_spells_cols)] for j in range(self.rows)]
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

        # render walls
        for i in range(114):
            self.village[self.walls.y[i]][self.walls.x[i]] = self.walls.health_check(i)

        # render barbarians
        length = 1
        troop_spell_color = Back.LIGHTBLACK_EX+' '+Style.RESET_ALL

        for i in range(self.rows+2):
            for j in range(self.cols+2*length, self.cols+self.troops_spells_cols+2*length):
                self.village[i][j] = troop_spell_color

        # render clash of clans
        clash = "Clash of Clans Jr."
        clash_len = len(clash)
        clash_x = (self.cols+6)
        clash_y = 1
        for i in range(clash_len):
            self.village[clash_y][clash_x+i] = Fore.GREEN+clash[i]+Style.RESET_ALL

        troop = "----Troops----"
        troop_len = len(troop)
        troop_x = (self.cols+self.troops_spells_cols - troop_len - 4*length)
        troop_y = 3
        for i in range(troop_len):
            self.village[troop_y][troop_x+i] = Fore.YELLOW+troop[i]+Style.RESET_ALL

        if self.hero == 0:
            hero = "--Hero--"
            hero_len = len(hero)
            hero_x = (self.cols+self.troops_spells_cols - hero_len - 7*length)
            hero_y = 5
            for i in range(hero_len):
                self.village[hero_y][hero_x+i] = Fore.YELLOW+hero[i]+Style.RESET_ALL

        if self.king.status == 1:
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

            king_dead = "!!Dead!!"
            king_dead_len = len(king_dead)
            king_dead_x = (self.cols+self.troops_spells_cols - troop_king_len -7*length)
            king_dead_y = 7


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
            elif self.king.status == 2:
                for i in range(king_dead_len):
                    self.village[king_dead_y][king_dead_x+i] = Fore.RED+king_dead[i]+Style.RESET_ALL
            

            self.king.king_color = Back.RED+' '+Style.RESET_ALL
        
        if self.queen.status == 1:
            # render Queen
            troop_queen = "--Queen--"
            troop_queen_len = len(troop_queen)
            troop_queen_x = (self.cols+self.troops_spells_cols - troop_queen_len -7*length)
            troop_queen_y = 5
            for i in range(troop_queen_len):
                self.village[troop_queen_y][troop_queen_x+i] = Fore.YELLOW+troop_queen[i]+Style.RESET_ALL

            queen_health = "Health: "
            queen_health_len = len(queen_health)
            queen_health_x = (self.cols+6)
            queen_health_y = 7

            health_bar_len = 10
            queen_health_length = int(self.queen.queen_health * health_bar_len / 100)

            queen_dead = "!!Dead!!"
            queen_dead_len = len(queen_dead)
            queen_dead_x = (self.cols+self.troops_spells_cols - troop_queen_len -7*length)
            queen_dead_y = 7


            if self.queen.status == 0:
                self.village[self.queen.y][self.queen.x] = self.queen.queen_color
            elif self.queen.status == 1:
                self.village[self.queen.y][self.queen.x] = self.queen.queen_color
                for i in range(queen_health_len):
                    self.village[queen_health_y][queen_health_x+i] = queen_health[i]
                for i in range(health_bar_len):
                    self.village[queen_health_y][queen_health_x+i+queen_health_len] = Back.BLACK+' '+Style.RESET_ALL
                for i in range(queen_health_length):
                    self.village[queen_health_y][queen_health_x+i+queen_health_len] = Back.RED+' '+Style.RESET_ALL
            elif self.queen.status == 2:
                for i in range(queen_dead_len):
                    self.village[queen_dead_y][queen_dead_x+i] = Fore.RED+queen_dead[i]+Style.RESET_ALL
            
            self.queen.queen_color = Back.RED+' '+Style.RESET_ALL

        # Barbarians Attack
        self.barbarians.move(self.walls, self.huts, self.cannons, self.th)

        # render Barbarians
        troop_barb = "--Barb--"
        troop_barb_len = len(troop_barb)
        troop_barb_x = (self.cols+self.troops_spells_cols - troop_barb_len -7*length)
        troop_barb_y = 9
        for i in range(troop_barb_len):

            self.village[troop_barb_y][troop_barb_x+i] = Fore.YELLOW+troop_barb[i]+Style.RESET_ALL  

              
        
        for counter in range(10):
            if self.barbarians.status[counter] == 0:
                self.village[self.barbarians.y[counter]][self.barbarians.x[counter]] = self.barbarians.barbarians_color
            if self.barbarians.status[counter] == 1:
                if self.barbarians.attack_status[counter] == 0:
                    self.village[self.barbarians.y[counter]][self.barbarians.x[counter]] = self.barbarians.health_check(counter)
                elif self.barbarians.attack_status[counter] == 1:
                    self.village[self.barbarians.y[counter]][self.barbarians.x[counter]] = self.barbarians.attack_color

        # render Archers
        troop_archer = "--Archer--"
        troop_archer_len = len(troop_archer)
        troop_archer_x = (self.cols+self.troops_spells_cols - troop_barb_len -8*length)
        troop_archer_y = 13
        for i in range(troop_archer_len):
            self.village[troop_archer_y][troop_archer_x+i] = Fore.YELLOW+troop_archer[i]+Style.RESET_ALL

        for counter in range(5):
            if self.archers.status[counter] == 0:
                self.village[self.archers.y[counter]][self.archers.x[counter]] = self.archers.archers_color
            if self.archers.status[counter] == 1:
                if self.archers.attack_status[counter] == 0:
                    self.village[self.archers.y[counter]][self.archers.x[counter]] = self.archers.health_check(counter)
                elif self.archers.attack_status[counter] == 1:
                    self.village[self.archers.y[counter]][self.archers.x[counter]] = self.archers.attack_color
        
        # render Loons
        troop_loon = "--Loon--"
        troop_loon_len = len(troop_loon)
        troop_loon_x = (self.cols+self.troops_spells_cols - troop_loon_len -7*length)
        troop_loon_y = 17
        for i in range(troop_loon_len):
            self.village[troop_loon_y][troop_loon_x+i] = Fore.YELLOW+troop_loon[i]+Style.RESET_ALL

        for counter in range(3):
            if self.loons.status[counter] == 0:
                self.village[self.loons.y[counter]][self.loons.x[counter]] = self.loons.loons_color
            if self.loons.status[counter] == 1:
                if self.loons.attack_status[counter] == 0:
                    self.village[self.loons.y[counter]][self.loons.x[counter]] = self.loons.health_check(counter)
                elif self.loons.attack_status[counter] == 1:
                    self.village[self.loons.y[counter]][self.loons.x[counter]] = self.loons.attack_color



        # Cannon attack
        self.cannons.cannon_attack_troops(self.hero, self.king, self.queen, self.barbarians)
                    
        # render Cannons
        for i in range(self.level + 1):
            for row in range(self.cannons.y[i],self.cannons.y[i]+self.cannons.height):
                for col in range(self.cannons.x[i],self.cannons.x[i]+self.cannons.width):
                    if self.cannons.attack_status[i] == 1:
                        if self.cannons.health[i] > 0:
                            os.system('afplay sounds/cannon_attack.wav &')
                            self.village[row][col] = self.cannons.attack_color
                        else:
                            self.village[row][col] = self.cannons.building_color_dead
                    else:
                        self.village[row][col] = self.cannons.health_check(i)
        
        # render Wizard Towers
        for i in range(self.level + 1):
            for row in range(self.wizard_tower.y[i],self.wizard_tower.y[i]+self.wizard_tower.height):
                for col in range(self.wizard_tower.x[i],self.wizard_tower.x[i]+self.wizard_tower.width):
                    self.village[row][col] = self.wizard_tower.health_check(i)


        # render Spells
        spells = "----Spells----"
        spells_len = len(spells)
        spells_x = (self.cols+self.troops_spells_cols - spells_len - 4*length)
        spells_y = 21
        for i in range(spells_len):
            self.village[spells_y][spells_x+i] = Fore.YELLOW+spells[i]+Style.RESET_ALL

        # render Rage
        rage = "--Rage--"
        rage_len = len(rage)
        rage_x = (self.cols+self.troops_spells_cols - rage_len - 7*length)
        rage_y = 23
        for i in range(rage_len):
            self.village[rage_y][rage_x+i] = Fore.YELLOW+rage[i]+Style.RESET_ALL

        if self.rage.status_rage == 0:
            self.village[self.rage.rage_y][self.rage.rage_x] = self.rage_color
        elif self.rage.status_rage == 1:
            self.rage.rage_timer = time.time()
            if self.king.status == 1:
                self.king.king_attack_damage = self.king.king_attack_damage * 2
                self.king.king_movement_speed = self.king.king_movement_speed * 2
            self.barbarians.damage = self.barbarians.damage * 2
            self.barbarians.time_to_move = 0.5
            os.system('afplay sounds/rage.wav -t 5 &')
            self.rage.status_rage = 2
        elif self.rage.status_rage == 2:
            if self.rage_time >= 4:
                self.rage.status_rage = 3
                if self.king.status == 1 or self.king.king_movement_speed == 2:
                    self.king.king_attack_damage = self.king.king_attack_damage // 2
                    self.king.king_movement_speed = self.king.king_movement_speed // 2
                self.barbarians.time_to_move = 1
                self.barbarians.damage = self.barbarians.damage // 2



        # render Heal
        heal = "--Heal--"
        heal_len = len(heal)
        heal_x = (self.cols+self.troops_spells_cols - heal_len - 7*length)
        heal_y = 27
        for i in range(heal_len):
            self.village[heal_y][heal_x+i] = Fore.YELLOW+heal[i]+Style.RESET_ALL

        if self.heal.status_heal == 0:
            self.village[self.heal.heal_y][self.heal.heal_x] = self.heal_color
        elif self.heal.status_heal == 1:
            self.heal.heal_timer = time.time()
            if self.king.status == 1:
                self.king.health_increase_heal()
            for counter in range(10):
                if self.barbarians.status[counter] == 1:
                    self.barbarians.health_increase_heal(counter)
            os.system('afplay sounds/heal.wav -t 1 &')
            self.heal.status_heal = 2
        elif self.heal.status_heal == 2:
            if self.heal_time >= 1:
                self.heal.status_heal = 3

        # render timer
        timer = "-----Time-----"
        timer_len = len(timer)
        timer_x = (self.cols+self.troops_spells_cols - timer_len - 4*length)
        timer_y = 31
        for i in range(timer_len):
            self.village[timer_y][timer_x+i] = Fore.YELLOW+timer[i]+Style.RESET_ALL

        time_elapsed_len = len(str(self.time_elapsed))
        time_elapsed_y = 33
        time_elapsed_x = self.cols+self.troops_spells_cols - 11
        for i in range(time_elapsed_len):
            self.village[time_elapsed_y][time_elapsed_x+i] = Fore.CYAN+str(self.time_elapsed)[i]+Style.RESET_ALL


        # check for game ending
        check_loss = 0
        for counter in range(10):
            if self.barbarians.status[counter] == 2:
                check_loss += 1
        if self.king.status == 2:
            check_loss += 1
        
        check_victory = 0
        for counter in range(2):
            if self.cannons.health[counter] <= 0:
                check_victory += 1
        for counter in range(5):
            if self.huts.health[counter] <= 0:
                check_victory += 1
        if self.th.health <= 0:
            check_victory += 1

        if check_loss == 11 and check_victory < 8:
            self.game_result = 2
        elif check_victory == 8:
            self.game_result = 1

        if self.game_result == 0:
            self.current_time = time.time()
            self.time_elapsed = math.floor(self.current_time - self.start_time)
            if self.heal.status_heal == 2:
                self.heal_time = math.floor(self.current_time - self.heal.heal_timer)
            if self.rage.status_rage == 2:
                self.rage_time = math.floor(self.current_time - self.rage.rage_timer)
            if self.queen.attack_eagle == 1:
                if self.current_time - self.queen.eagle_timer >= 1:
                    attack_y = 0
                    attack_x = 0
                    if self.queen.queen_dir == 1:
                        attack_y = self.queen.eagle_attack_y - 16
                        attack_x = self.queen.eagle_attack_x
                        self.queen.attack(self.walls, self.huts, self.cannons, self.th, attack_y, attack_x)
                    elif self.queen.queen_dir == 2:
                        attack_y = self.queen.eagle_attack_y
                        attack_x = self.queen.eagle_attack_x - 16
                        self.queen.attack(self.walls, self.huts, self.cannons, self.th, attack_y, attack_x)
                    elif self.queen.queen_dir == 3:
                        attack_y = self.queen.eagle_attack_y + 16
                        attack_x = self.queen.eagle_attack_x
                        self.queen.attack(self.walls, self.huts, self.cannons, self.th, attack_y, attack_x)
                    elif self.queen.queen_dir == 4:
                        attack_y = self.queen.eagle_attack_y
                        attack_x = self.queen.eagle_attack_x + 16 
                        self.queen.attack(self.walls, self.huts, self.cannons, self.th, attack_y, attack_x)
                    self.queen.attack_eagle = 0
                    self.queen.eagle_timer = 0
                    self.queen.eagle_attack_x = 0
                    self.queen.eagle_attack_y = 0

                    
        elif self.game_result == 1:
            game_over_screen_height = 16
            game_over_screen_width = 43
            self.game_over_screen = [[self.border_color for i in range(game_over_screen_width)] for j in range(game_over_screen_height)]

            Clash_of_clans = "Clash of clans Jr."
            Clash_of_clans_len = len(Clash_of_clans)
            clash_offset = 13
            for j in range(Clash_of_clans_len):
                self.game_over_screen[1][clash_offset+j] = Fore.GREEN+Clash_of_clans[j]+Style.RESET_ALL

            game_over = "Victory!"
            game_over_offset = 18
            for j in range(0, len(game_over)):
                self.game_over_screen[3][game_over_offset+j] =  Fore.YELLOW+game_over[j]+Style.RESET_ALL

            time_taken = "Time Taken: {} seconds".format(self.time_elapsed)
            time_taken_offset = 11
            for j in range(0, len(time_taken)):
                self.game_over_screen[5][time_taken_offset+j] = Fore.YELLOW+time_taken[j]+Style.RESET_ALL

            for row in range(0, game_over_screen_height):
                for col in range(0, game_over_screen_width):
                    self.village[14+row][19+col] = self.game_over_screen[row][col]
        elif self.game_result == 2:
            game_over_screen_height = 16
            game_over_screen_width = 43
            self.game_over_screen = [[self.border_color for i in range(game_over_screen_width)] for j in range(game_over_screen_height)]

            Clash_of_clans = "Clash of clans Jr."
            Clash_of_clans_len = len(Clash_of_clans)
            clash_offset = 13
            for j in range(Clash_of_clans_len):
                self.game_over_screen[1][clash_offset+j] = Fore.GREEN+Clash_of_clans[j]+Style.RESET_ALL

            game_over = "You Lose!"
            game_over_offset = 18
            for j in range(0, len(game_over)):
                self.game_over_screen[3][game_over_offset+j] =  Fore.YELLOW+game_over[j]+Style.RESET_ALL

            time_taken = "Time Taken: {} seconds".format(self.time_elapsed)
            time_taken_offset = 11
            for j in range(0, len(time_taken)):
                self.game_over_screen[5][time_taken_offset+j] = Fore.YELLOW+time_taken[j]+Style.RESET_ALL

            for row in range(0, game_over_screen_height):
                for col in range(0, game_over_screen_width):
                    self.village[14+row][19+col] = self.game_over_screen[row][col]

        # replay storing
        file_path = "./replays/replay_"+str(self.replay_number)+".txt"
        with open(file_path, "a") as f:
            f.write('\n'.join([''.join(row) for row in self.village]))
            f.write('\n')


        print('\n'.join([''.join(row) for row in self.village]))


