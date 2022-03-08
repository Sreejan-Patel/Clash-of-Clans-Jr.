from operator import le
from random import random
from colorama import Fore, Style, Back
import numpy as np
import math
from src.utlis import Utils

class Troops():

    def __init__(self,start,end):
        self.troops_color = Back.BLUE+' '+Style.RESET_ALL
        self.x = np.zeros((10), type(int))
        self.y = np.zeros((10), type(int))
        self.status = np.zeros((10), type(int))
        self.health = np.full((10), 30)
        self.troop = np.arange(10)
        self.count = 0
        self.damage = 10
        self.movement_speed = 1

        self.move_x = np.full((10), -1)
        self.move_y = np.full((10), -1)

        self.entered = np.zeros((10), type(int))

        self.initialize(start,end)

    def initialize(self,start,end):
        """Initializing troops."""
        length = 2
        for i in range(10):
            if self.status[i] == 0:
                self.x[i] = start + i*length + 3*length
                self.y[i] = 11

    def spawn(self, key):
        """Spawning troops."""
        if self.count < 10:
            if key == 'i':
                self.x[self.count] = 7
                self.y[self.count] = 7
                self.status[self.count] = 1
                self.count += 1
            elif key == 'j':
                self.x[self.count] = 73
                self.y[self.count] = 11
                self.status[self.count] = 1
                self.count += 1
            elif key == 'k':
                self.x[self.count] = 32
                self.y[self.count] = 12
                self.status[self.count] = 1
                self.count += 1
            else:
                pass
    
 

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

    def check_obstacle(self,i,walls,huts,cannons,th,prev_y,prev_x):
        if walls.check_coordinates(self.y[i], self.x[i]) > -1:
            self.y[i] = prev_y
            self.x[i] = prev_x
            return 1
        elif huts.check_coordinates(self.y[i], self.x[i]) > -1:
            self.y[i] = prev_y
            self.x[i] = prev_x
            return 2
        elif cannons.check_coordinates(self.y[i], self.x[i]) > -1:
            self.y[i] = prev_y
            self.x[i] = prev_x
            return 3
        elif th.check_coordinates(self.y[i], self.x[i]) > -1:
            self.y[i] = prev_y
            self.x[i] = prev_x
            return 4
        elif Utils.check_border_coordinates(self.y[i], self.x[i]):
            self.y[i] = prev_y
            self.x[i] = prev_x
            return 5
        else:
            return 0
    
    
    def move_troops(self,i,rage,walls,huts,cannons,th,prev_y,prev_x,w,s,a,d,temp):
            if w == min(w,s,a,d):
                self.y[i] -= 1
                check = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                if temp == 1 and check == 1:
                    self.attack_wall(i,walls)
                elif check > 0:
                    if s == min(s,a,d):
                        self.y[i] += 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 > 0:
                            if a == min(a,d):
                                self.x[i] -= 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 > 0:
                                    self.x[i] += 1
                            else:
                                self.x[i] += 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 > 0:
                                    self.x[i] -= 1
                    elif a == min(s,a,d):
                        self.x[i] -= 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 > 0:
                            if d == min(s,d):
                                self.x[i] += 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 > 0:
                                    self.y[i] += 1
                            else:
                                self.y[i] += 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 > 0:
                                    self.x[i] += 1
                    elif d == min(s,a,d):
                        self.x[i] += 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 > 0:
                            if s == min(s,a):
                                self.y[i] += 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 > 0:
                                    self.x[i] -= 1
                            else:
                                self.x[i] -= 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 > 0:
                                    self.y[i] += 1
                    
            elif s == min(w,s,a,d):
                self.y[i] += 1
                check = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                if temp == 1 and check == 1:
                    self.attack_wall(i,walls)
                elif check > 0:
                    if w == min(w,a,d):
                        self.y[i] -= 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 > 0:
                            if a == min(a,d):
                                self.x[i] -= 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 > 0:
                                    self.x[i] += 1
                            else:
                                self.x[i] += 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 > 0:
                                    self.x[i] -= 1
                    elif a == min(w,a,d):
                        self.x[i] -= 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 > 0:
                            if d == min(s,d):
                                self.x[i] += 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 > 0:
                                    self.y[i] -= 1
                            else:
                                self.y[i] -= 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 > 0:
                                    self.x[i] += 1
                    elif d == min(w,a,d):
                        self.x[i] += 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 > 0:
                            if s == min(s,a):
                                self.y[i] -= 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 > 0:
                                    self.x[i] -= 1
                            else:
                                self.x[i] -= 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 > 0:
                                    self.y[i] -= 1
            elif a == min(w,s,a,d):
                self.x[i] -= 1
                check = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                if temp == 1 and check == 1:
                    self.attack_wall(i,walls)
                elif check > 0:
                    if s == min(s,w,d):
                        self.y[i] += 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 > 0:
                            if w == min(w,d):
                                self.y[i] -= 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 > 0:
                                    self.x[i] += 1
                            else:
                                self.x[i] += 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 > 0:
                                    self.y[i] -= 1
                    elif w == min(s,w,d):
                        self.y[i] -= 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 > 0:
                            if d == min(s,d):
                                self.x[i] += 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 > 0:
                                    self.y[i] += 1
                            else:
                                self.y[i] += 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 > 0:
                                    self.x[i] += 1
                    elif d == min(s,w,d):
                        self.x[i] += 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 > 0:
                            if s == min(s,a):
                                self.y[i] += 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 > 0:
                                    self.y[i] -= 1
                            else:
                                self.y[i] -= 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 > 0:
                                    self.y[i] += 1
            elif d == min(w,s,a,d):
                self.x[i] += 1
                check = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                if temp == 1 and check == 1:
                    self.attack_wall(i,walls)
                elif check > 0:
                    if s == min(s,a,w):
                        self.y[i] += 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 > 0:
                            if a == min(a,w):
                                self.x[i] -= 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 > 0:
                                    self.y[i] -= 1
                            else:
                                self.y[i] -= 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 > 0:
                                    self.x[i] -= 1
                    elif a == min(s,a,w):
                        self.x[i] -= 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 > 0:
                            if w == min(s,w):
                                self.y[i] -= 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 > 0:
                                    self.y[i] += 1
                            else:
                                self.y[i] += 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 > 0:
                                    self.y[i] -= 1
                    elif w == min(s,a,w):
                        self.y[i] -= 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 > 0:
                            if s == min(s,a):
                                self.y[i] += 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 > 0:
                                    self.x[i] -= 1
                            else:
                                self.x[i] -= 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 > 0:
                                    self.y[i] += 1
            else:
                pass

    def nearest_building(self,i,huts,cannons,th,game_over):
        at_least_one = 0
        huts_dist = np.full((5), 100)
        for j in range(5):
            if huts.status[j] == 1:
                at_least_one = 1
                huts_dist[j] = self.euclidean_distance(self.y[i],self.x[i],huts.y[j],huts.x[j])
                    
        th_dist = 100
        if th.status == 1:
            at_least_one = 1
            th_dist = self.euclidean_distance_th(self.y[i],self.x[i],th.y,th.x)
                    
        cannons_dist = np.full((2), 100)
        for j in range(2):
            if cannons.status[j] == 1:
                at_least_one = 1
                cannons_dist[j] = self.euclidean_distance_cannons(self.y[i],self.x[i],cannons.y[j],cannons.x[j])
        if at_least_one == 1:
            if np.amin(huts_dist) < np.amin(cannons_dist) and np.amin(huts_dist) < th_dist:
                self.move_x[i] = huts.x[np.argmin(huts_dist)]
                self.move_y[i] = huts.y[np.argmin(huts_dist)]
            elif np.amin(cannons_dist) < th_dist:
                self.move_x[i] = cannons.x[np.argmin(cannons_dist)]
                self.move_y[i] = cannons.y[np.argmin(cannons_dist)]
            else:
                self.move_x[i] = th.x
                self.move_y[i] = th.y 
        else:
            game_over = 1       
        
    def move(self,walls,huts,cannons,th,rage,game_over):
        """Moving troops."""
        for i in range(10):
            if self.status[i] == 1:
                # first check if the troop is in the same position as the nearest broken wall , if not move there
                is_wall = np.zeros((114), type(int))
                is_protected = True
                if self.entered[i] == 0:
                    for j in range(114):
                        if walls.health[j] <= 0:
                            is_wall[j] = 1
                            is_protected = False
                elif self.entered[i] == 1:
                    temp = 0
                    self.nearest_building(i,huts,cannons,th,game_over)
                    self.move_towards_nearest_building(i,rage,walls,huts,cannons,th,temp)
                        

                walls_dist = np.full((114), 100)
                for j in range(114):
                    walls_dist[j] = self.euclidean_distance(self.y[i], self.x[i], walls.y[j], walls.x[j])

                # if no wall is broken, move towards the nearest building
                if is_protected == True:
                    temp = 1
                    self.nearest_building(i,huts,cannons,th,game_over)
                    self.move_towards_nearest_building(i,rage,walls,huts,cannons,th,temp)
                elif is_protected == False and self.entered[i] == 0:
                    wall_dist_min = 100
                    for j in range(114):
                        if is_wall[j] == 1:
                            if walls_dist[j] < wall_dist_min:
                                wall_dist_min = walls_dist[j]
                                self.move_x[i] = walls.x[j]
                                self.move_y[i] = walls.y[j]
                    self.move_towards_wall_open(i,rage,self.move_y[i],self.move_x[i],walls,huts,cannons,th)

    def move_towards_wall_open(self,i,rage,y,x,walls,huts,cannons,th):
        """Move Towards Wall Open"""
        if self.y[i] == y  and self.x[i] == x and self.health[i] > 0:
            self.entered[i] = 1
        else:
            self.entered[i] = 0
            w = self.euclidean_distance(self.y[i]-1,self.x[i],y,x)
            s = self.euclidean_distance(self.y[i]+1,self.x[i],y,x)
            a = self.euclidean_distance(self.y[i],self.x[i]-1,y,x)
            d = self.euclidean_distance(self.y[i],self.x[i]+1,y,x)
            

            prev_x = self.x[i]
            prev_y = self.y[i]
            temp = 0
            self.move_troops(i,rage,walls,huts,cannons,th,prev_y,prev_x,w,s,a,d,temp)
    
    def move_towards_nearest_building(self,i,rage,walls,huts,cannons,th,temp):
        """Move Towards Nearest Building"""
        if ((self.y[i] == self.move_y[i]+1 and self.x[i] == self.move_x[i]) or (self.y[i] == self.move_y[i]-1 and self.x[i] == self.move_x[i])
        or (self.y[i] == self.move_y[i] and self.x[i] == self.move_x[i]+1) or (self.y[i] == self.move_y[i] and self.x[i] == self.move_x[i]-1))  and self.health[i] > 0:
            self.attack(i,rage,walls,huts,cannons,th)
        else:
            w = self.euclidean_distance(self.y[i]-1,self.x[i],self.move_y[i],self.move_x[i])
            s = self.euclidean_distance(self.y[i]+1,self.x[i],self.move_y[i],self.move_x[i])
            a = self.euclidean_distance(self.y[i],self.x[i]-1,self.move_y[i],self.move_x[i])
            d = self.euclidean_distance(self.y[i],self.x[i]+1,self.move_y[i],self.move_x[i])
            

            prev_x = self.x[i]
            prev_y = self.y[i]
            self.move_troops(i,rage,walls,huts,cannons,th,prev_y,prev_x,w,s,a,d,temp)

    def attack(self,i,rage,walls,huts,cannons,th):
        """Attacking."""
        
        hut_l = huts.check_coordinates(self.y[i], self.x[i]-1)
        hut_r = huts.check_coordinates(self.y[i], self.x[i]+1)
        hut_u = huts.check_coordinates(self.y[i]-1, self.x[i])
        hut_d = huts.check_coordinates(self.y[i]+1, self.x[i])
        
        cannon_l = cannons.check_coordinates(self.y[i], self.x[i]-1)
        cannon_r = cannons.check_coordinates(self.y[i], self.x[i]+1)
        cannon_u = cannons.check_coordinates(self.y[i]-1, self.x[i])
        cannon_d = cannons.check_coordinates(self.y[i]+1, self.x[i])
        
        th_l = th.check_coordinates(self.y[i], self.x[i]-1)
        th_r = th.check_coordinates(self.y[i], self.x[i]+1)
        th_u = th.check_coordinates(self.y[i]-1, self.x[i])
        th_d = th.check_coordinates(self.y[i]+1, self.x[i])


        if hut_l != -1:
            huts.health_decrease(hut_l, self.damage)
        elif hut_r != -1:
            huts.health_decrease(hut_r, self.damage)
        elif hut_u != -1:
            huts.health_decrease(hut_u, self.damage)
        elif hut_d != -1:
            huts.health_decrease(hut_d, self.damage)

        elif cannon_l != -1:
            cannons.health_decrease(cannon_l, self.damage)
        elif cannon_r != -1:
            cannons.health_decrease(cannon_r, self.damage)
        elif cannon_u != -1:
            cannons.health_decrease(cannon_u, self.damage)
        elif cannon_d != -1:
            cannons.health_decrease(cannon_d, self.damage)

        elif th_l != -1 or th_r != -1 or th_u != -1 or th_d != -1:
            th.health_decrease(self.damage)       

    def attack_wall(self,i,walls):
        """Attacking."""

        wall_l = walls.check_coordinates(self.y[i], self.x[i]-1)
        wall_r = walls.check_coordinates(self.y[i], self.x[i]+1)
        wall_u = walls.check_coordinates(self.y[i]-1, self.x[i])
        wall_d = walls.check_coordinates(self.y[i]+1, self.x[i])
            
        if wall_l != -1:
            walls.health_decrease(wall_l, self.damage)
        elif wall_r != -1:
            walls.health_decrease(wall_r, self.damage)
        elif wall_u != -1:
            walls.health_decrease(wall_u, self.damage)
        elif wall_d != -1:
            walls.health_decrease(wall_d, self.damage)
            




    



