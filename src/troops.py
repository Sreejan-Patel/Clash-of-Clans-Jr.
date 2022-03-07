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
    
    def euclidean_distance_huts(self, y1, x1, y2, x2):
        '''
        This function calculates the euclidean distance between two points (considering the middle y and x coordinates of the huts)
        '''
        return math.sqrt((y1-y2)**2 + (x1-x2)**2)

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
    
    def euclidean_distance_walls(self, y1, x1, y2, x2):
        '''
        This function calculates the euclidean distance between two points (considering the middle y and x coordinates of the walls)
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
            return 1
        elif cannons.check_coordinates(self.y[i], self.x[i]) > -1:
            self.y[i] = prev_y
            self.x[i] = prev_x
            return 1
        elif th.check_coordinates(self.y[i], self.x[i]) > -1:
            self.y[i] = prev_y
            self.x[i] = prev_x
            return 1
        elif Utils.check_border_coordinates(self.y[i], self.x[i]):
            self.y[i] = prev_y
            self.x[i] = prev_x
            return 1
        else:
            return 0

        
    def move(self,walls,huts,cannons,th,rage,heal):
        """Moving troops."""
        for i in range(10):
            if self.status[i] == 1:
                is_wall = np.zeros((114), type(int))
                is_protected = False
                if self.entered[i] == 0:
                    for j in range(114):
                        if walls.health[j] <= 0:
                            is_wall[j] = 1
                            is_protected = False
                        

                walls_dist = np.full((114), 100)
                for j in range(114):
                    walls_dist[j] = self.euclidean_distance_walls(self.y[i], self.x[i], walls.y[j], walls.x[j])
                if is_protected == True:
                    huts_dist = np.full((5), 100)
                    for j in range(5):
                        if huts.status[j] == 1:
                            huts_dist[j] = self.euclidean_distance_huts(self.y[i],self.x[i],huts.y[j],huts.x[j])
                    
                    th_dist = 100
                    if th.status == 1:
                        th_dist = self.euclidean_distance_th(self.y[i],self.x[i],th.y,th.x)
                    
                    cannons_dist = np.full((2), 100)
                    for j in range(2):
                        if cannons.status[j] == 1:
                            cannons_dist[j] = self.euclidean_distance_cannons(self.y[i],self.x[i],cannons.y[j],cannons.x[j])

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
                    wall_dist_min = 100
                    for j in range(114):
                        if is_wall[j] == 1:
                            if walls_dist[j] < wall_dist_min:
                                wall_dist_min = walls_dist[j]
                                self.move_x[i] = walls.x[j]
                                self.move_y[i] = walls.y[j]
                    self.move_towards_wall_open(i,rage,self.move_y[i],self.move_x[i],walls,huts,cannons,th)

    def move_towards_wall_open(self,i,rage,y,x,walls,huts,cannons,th):
        """Attacking troops."""
        if self.y[i] == y  and self.x[i] == x and self.health[i] > 0:
            self.entered[i] = 1
        else:
            self.entered[i] = 0
            w = self.euclidean_distance_walls(self.y[i]-1,self.x[i],y,x)
            s = self.euclidean_distance_walls(self.y[i]+1,self.x[i],y,x)
            a = self.euclidean_distance_walls(self.y[i],self.x[i]-1,y,x)
            d = self.euclidean_distance_walls(self.y[i],self.x[i]+1,y,x)
            

            prev_x = self.x[i]
            prev_y = self.y[i]

            if w == min(w,s,a,d):
                self.y[i] -= 1
                check = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                if check == 1:
                    if s == min(s,a,d):
                        self.y[i] += 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 == 1:
                            if a == min(a,d):
                                self.x[i] -= 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 == 1:
                                    self.x[i] += 1
                            else:
                                self.x[i] += 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 == 1:
                                    self.x[i] -= 1
                    elif a == min(s,a,d):
                        self.x[i] -= 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 == 1:
                            if d == min(s,d):
                                self.x[i] += 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 == 1:
                                    self.y[i] += 1
                            else:
                                self.y[i] += 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 == 1:
                                    self.x[i] += 1
                    elif d == min(s,a,d):
                        self.x[i] += 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 == 1:
                            if s == min(s,a):
                                self.y[i] += 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 == 1:
                                    self.x[i] -= 1
                            else:
                                self.x[i] -= 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 == 1:
                                    self.y[i] += 1
                    
            elif s == min(w,s,a,d):
                self.y[i] += 1
                check = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                if check == 1:
                    if w == min(w,a,d):
                        self.y[i] -= 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 == 1:
                            if a == min(a,d):
                                self.x[i] -= 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 == 1:
                                    self.x[i] += 1
                            else:
                                self.x[i] += 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 == 1:
                                    self.x[i] -= 1
                    elif a == min(w,a,d):
                        self.x[i] -= 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 == 1:
                            if d == min(s,d):
                                self.x[i] += 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 == 1:
                                    self.y[i] -= 1
                            else:
                                self.y[i] -= 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 == 1:
                                    self.x[i] += 1
                    elif d == min(w,a,d):
                        self.x[i] += 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 == 1:
                            if s == min(s,a):
                                self.y[i] -= 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 == 1:
                                    self.x[i] -= 1
                            else:
                                self.x[i] -= 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 == 1:
                                    self.y[i] -= 1
            elif a == min(w,s,a,d):
                self.x[i] -= 1
                check = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                if check == 1:
                    if s == min(s,w,d):
                        self.y[i] += 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 == 1:
                            if w == min(w,d):
                                self.y[i] -= 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 == 1:
                                    self.x[i] += 1
                            else:
                                self.x[i] += 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 == 1:
                                    self.y[i] -= 1
                    elif w == min(s,w,d):
                        self.y[i] -= 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 == 1:
                            if d == min(s,d):
                                self.x[i] += 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 == 1:
                                    self.y[i] += 1
                            else:
                                self.y[i] += 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 == 1:
                                    self.x[i] += 1
                    elif d == min(s,w,d):
                        self.x[i] += 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 == 1:
                            if s == min(s,a):
                                self.y[i] += 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 == 1:
                                    self.y[i] -= 1
                            else:
                                self.y[i] -= 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 == 1:
                                    self.y[i] += 1
            elif d == min(w,s,a,d):
                self.x[i] += 1
                check = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                if check == 1:
                    if s == min(s,a,w):
                        self.y[i] += 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 == 1:
                            if a == min(a,w):
                                self.x[i] -= 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 == 1:
                                    self.y[i] -= 1
                            else:
                                self.y[i] -= 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 == 1:
                                    self.x[i] -= 1
                    elif a == min(s,a,w):
                        self.x[i] -= 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 == 1:
                            if w == min(s,w):
                                self.y[i] -= 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 == 1:
                                    self.y[i] += 1
                            else:
                                self.y[i] += 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 == 1:
                                    self.y[i] -= 1
                    elif w == min(s,a,w):
                        self.y[i] -= 1
                        check2 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                        if check2 == 1:
                            if s == min(s,a):
                                self.y[i] += 1
                                check3 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check3 == 1:
                                    self.x[i] -= 1
                            else:
                                self.x[i] -= 1
                                check4 = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                                if check4 == 1:
                                    self.y[i] += 1
            else:
                pass
            
                
            




    



