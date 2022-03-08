import time
from colorama import Fore, Style, Back
import numpy as np
import math
from src.utlis import Utils

class Troops():

    def __init__(self,start,end):
        self.troops_color = Back.BLUE+' '+Style.RESET_ALL
        self.troops_color_low_health = Back.LIGHTBLUE_EX+' '+Style.RESET_ALL
        self.x = np.zeros((10), type(int))
        self.y = np.zeros((10), type(int))
        self.status = np.zeros((10), type(int))
        self.health = np.full((10), 30)
        self.count = 0
        self.damage = 10
        self.movement_speed = 1
        self.timer = np.full((10), 0)
        self.time_ticks = np.full((10), -1)

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

    def health_increase_heal(self,i):
        """Increase troops's health"""
        self.health[i] = 1.5 * self.health[i]   # heal 150% times
        if self.health[i] > 30:
            self.health[i] = 30

    def health_check(self, i):
        '''
        This function checks the health of the hut and returns the color of the building
        '''
        if self.health[i] <= ((50/100)*30):
            return self.troops_color_low_health
        else:
            return self.troops_color

    def spawn(self, key):
        """Spawning troops."""
        if self.count < 10:
            if key == 'i':
                self.x[self.count] = 7
                self.y[self.count] = 7
                self.status[self.count] = 1
                self.timer[self.count] = time.time()
                self.time_ticks[self.count] = 0
                self.count += 1
            elif key == 'j':
                self.x[self.count] = 73
                self.y[self.count] = 11
                self.status[self.count] = 1
                self.timer[self.count] = time.time()
                self.time_ticks[self.count] = 0
                self.count += 1
            elif key == 'k':
                self.x[self.count] = 32
                self.y[self.count] = 12
                self.status[self.count] = 1
                self.timer[self.count] = time.time()
                self.time_ticks[self.count] = 0
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
    
    
    def move_troops(self,i,walls,huts,cannons,th,prev_y,prev_x,w,s,a,d,ne,nw,se,sw,temp):
            movement = [w,s,a,d,ne,nw,se,sw]
            movement.sort()

            for j in range(len(movement)):
                if movement[j] == w:
                    self.y[i] -= self.movement_speed
                    check = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                    if check == 1 and temp == 1:
                        self.attack_wall(i,walls)
                        break
                    elif check > 0:
                        continue
                    else:
                        break
                elif movement[j] == s:
                    self.y[i] += self.movement_speed
                    check = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                    if check == 1 and temp == 1:
                        self.attack_wall(i,walls)
                        break
                    elif check > 0:
                        continue
                    else:
                        break
                elif movement[j] == a:
                    self.x[i] -= self.movement_speed
                    check = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                    if check == 1 and temp == 1:
                        self.attack_wall(i,walls)
                        break
                    elif check > 0:
                        continue
                    else:
                        break
                elif movement[j] == d:
                    self.x[i] += self.movement_speed
                    check = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                    if check == 1 and temp == 1:
                        self.attack_wall(i,walls)
                        break
                    elif check > 0:
                        continue
                    else:
                        break
                elif movement[j] == ne:
                    self.y[i] -= self.movement_speed
                    self.x[i] += self.movement_speed
                    check = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                    if check == 1 and temp == 1:
                        self.attack_wall(i,walls)
                        break
                    elif check > 0:
                        continue
                    else:
                        break
                elif movement[j] == nw:
                    self.y[i] -= self.movement_speed
                    self.x[i] -= self.movement_speed
                    check = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                    if check == 1 and temp == 1:
                        self.attack_wall(i,walls)
                        break
                    elif check > 0:
                        continue
                    else: 
                        break
                elif movement[j] == se:
                    self.y[i] += self.movement_speed
                    self.x[i] += self.movement_speed
                    check = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                    if check == 1 and temp == 1:
                        self.attack_wall(i,walls)
                        break
                    elif check > 0:
                        continue
                    else: 
                        break
                elif movement[j] == sw:
                    self.y[i] += self.movement_speed
                    self.x[i] -= self.movement_speed
                    check = self.check_obstacle(i,walls,huts,cannons,th,prev_y,prev_x)
                    if check == 1 and temp == 1:
                        self.attack_wall(i,walls)
                        break
                    elif check > 0:
                        continue
                    else: 
                        break
                else:
                    pass

    def nearest_building(self,i,huts,cannons,th):
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
            pass    
        
    def move(self,walls,huts,cannons,th):
        """Moving troops."""
        for i in range(10):
            if self.status[i] == 1:
                if math.floor(time.time() - self.timer[i]) == self.time_ticks[i]:
                    self.time_ticks[i] += 1
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
                        self.nearest_building(i,huts,cannons,th)
                        self.move_towards_nearest_building(i,walls,huts,cannons,th,temp)
                            

                    walls_dist = np.full((114), 100)
                    for j in range(114):
                        walls_dist[j] = self.euclidean_distance(self.y[i], self.x[i], walls.y[j], walls.x[j])

                    # if no wall is broken, move towards the nearest building
                    if is_protected == True:
                        temp = 1
                        self.nearest_building(i,huts,cannons,th)
                        self.move_towards_nearest_building(i,walls,huts,cannons,th,temp)
                    elif is_protected == False and self.entered[i] == 0:
                        wall_dist_min = 100
                        for j in range(114):
                            if is_wall[j] == 1:
                                if walls_dist[j] < wall_dist_min:
                                    wall_dist_min = walls_dist[j]
                                    self.move_x[i] = walls.x[j]
                                    self.move_y[i] = walls.y[j]
                        self.move_towards_wall_open(i,self.move_y[i],self.move_x[i],walls,huts,cannons,th)

    def move_towards_wall_open(self,i,y,x,walls,huts,cannons,th):
        """Move Towards Wall Open"""
        if self.y[i] == y  and self.x[i] == x and self.health[i] > 0:
            self.entered[i] = 1
        else:
            self.entered[i] = 0
            w = self.euclidean_distance(self.y[i]-1,self.x[i],y,x)
            s = self.euclidean_distance(self.y[i]+1,self.x[i],y,x)
            a = self.euclidean_distance(self.y[i],self.x[i]-1,y,x)
            d = self.euclidean_distance(self.y[i],self.x[i]+1,y,x)
            ne = self.euclidean_distance(self.y[i]-1,self.x[i]+1,y,x)
            nw = self.euclidean_distance(self.y[i]-1,self.x[i]-1,y,x)
            se = self.euclidean_distance(self.y[i]+1,self.x[i]+1,y,x)
            sw = self.euclidean_distance(self.y[i]+1,self.x[i]-1,y,x)
            

            prev_x = self.x[i]
            prev_y = self.y[i]
            temp = 0
            self.move_troops(i,walls,huts,cannons,th,prev_y,prev_x,w,s,a,d,ne,nw,se,sw,temp)
    
    def move_towards_nearest_building(self,i,walls,huts,cannons,th,temp):
        """Move Towards Nearest Building"""
        if ((self.y[i] == self.move_y[i]+1 and self.x[i] == self.move_x[i]) or (self.y[i] == self.move_y[i]-1 and self.x[i] == self.move_x[i])
        or (self.y[i] == self.move_y[i] and self.x[i] == self.move_x[i]+1) or (self.y[i] == self.move_y[i] and self.x[i] == self.move_x[i]-1)
        or (self.y[i] == self.move_y[i]+1 and self.x[i] == self.move_x[i]+1) or (self.y[i] == self.move_y[i]-1 and self.x[i] == self.move_x[i]-1)
        or (self.y[i] == self.move_y[i]-1 and self.x[i] == self.move_x[i]+1) or (self.y[i] == self.move_y[i]+1 and self.x[i] == self.move_x[i]-1)) and self.health[i] > 0:
            self.attack(i,huts,cannons,th)
        else:
            w = self.euclidean_distance(self.y[i]-1,self.x[i],self.move_y[i],self.move_x[i])
            s = self.euclidean_distance(self.y[i]+1,self.x[i],self.move_y[i],self.move_x[i])
            a = self.euclidean_distance(self.y[i],self.x[i]-1,self.move_y[i],self.move_x[i])
            d = self.euclidean_distance(self.y[i],self.x[i]+1,self.move_y[i],self.move_x[i])
            ne = self.euclidean_distance(self.y[i]-1,self.x[i]+1,self.move_y[i],self.move_x[i])
            nw = self.euclidean_distance(self.y[i]-1,self.x[i]-1,self.move_y[i],self.move_x[i])
            se = self.euclidean_distance(self.y[i]+1,self.x[i]+1,self.move_y[i],self.move_x[i])
            sw = self.euclidean_distance(self.y[i]+1,self.x[i]-1,self.move_y[i],self.move_x[i])
            

            prev_x = self.x[i]
            prev_y = self.y[i]
            self.move_troops(i,walls,huts,cannons,th,prev_y,prev_x,w,s,a,d,ne,nw,se,sw,temp)

    def attack(self,i,huts,cannons,th):
        """Attacking."""
        
        hut_l = huts.check_coordinates(self.y[i], self.x[i]-1)
        hut_r = huts.check_coordinates(self.y[i], self.x[i]+1)
        hut_u = huts.check_coordinates(self.y[i]-1, self.x[i])
        hut_d = huts.check_coordinates(self.y[i]+1, self.x[i])
        hut_ne = huts.check_coordinates(self.y[i]-1, self.x[i]+1)
        hut_nw = huts.check_coordinates(self.y[i]-1, self.x[i]-1)
        hut_se = huts.check_coordinates(self.y[i]+1, self.x[i]+1)
        hut_sw = huts.check_coordinates(self.y[i]+1, self.x[i]-1)
        
        cannon_l = cannons.check_coordinates(self.y[i], self.x[i]-1)
        cannon_r = cannons.check_coordinates(self.y[i], self.x[i]+1)
        cannon_u = cannons.check_coordinates(self.y[i]-1, self.x[i])
        cannon_d = cannons.check_coordinates(self.y[i]+1, self.x[i])
        cannon_ne = cannons.check_coordinates(self.y[i]-1, self.x[i]+1)
        cannon_nw = cannons.check_coordinates(self.y[i]-1, self.x[i]-1)
        cannon_se = cannons.check_coordinates(self.y[i]+1, self.x[i]+1)
        cannon_sw = cannons.check_coordinates(self.y[i]+1, self.x[i]-1)
        
        th_l = th.check_coordinates(self.y[i], self.x[i]-1)
        th_r = th.check_coordinates(self.y[i], self.x[i]+1)
        th_u = th.check_coordinates(self.y[i]-1, self.x[i])
        th_d = th.check_coordinates(self.y[i]+1, self.x[i])
        th_ne = th.check_coordinates(self.y[i]-1, self.x[i]+1)
        th_nw = th.check_coordinates(self.y[i]-1, self.x[i]-1)
        th_se = th.check_coordinates(self.y[i]+1, self.x[i]+1)
        th_sw = th.check_coordinates(self.y[i]+1, self.x[i]-1)


        if hut_l != -1:
            huts.health_decrease(hut_l, self.damage)
        elif hut_r != -1:
            huts.health_decrease(hut_r, self.damage)
        elif hut_u != -1:
            huts.health_decrease(hut_u, self.damage)
        elif hut_d != -1:
            huts.health_decrease(hut_d, self.damage)
        elif hut_ne != -1:
            huts.health_decrease(hut_ne, self.damage)
        elif hut_nw != -1:
            huts.health_decrease(hut_nw, self.damage)
        elif hut_se != -1:
            huts.health_decrease(hut_se, self.damage)
        elif hut_sw != -1:
            huts.health_decrease(hut_sw, self.damage)

        elif cannon_l != -1:
            cannons.health_decrease(cannon_l, self.damage)
        elif cannon_r != -1:
            cannons.health_decrease(cannon_r, self.damage)
        elif cannon_u != -1:
            cannons.health_decrease(cannon_u, self.damage)
        elif cannon_d != -1:
            cannons.health_decrease(cannon_d, self.damage)
        elif cannon_ne != -1:
            cannons.health_decrease(cannon_ne, self.damage)
        elif cannon_nw != -1:
            cannons.health_decrease(cannon_nw, self.damage)
        elif cannon_se != -1:
            cannons.health_decrease(cannon_se, self.damage)
        elif cannon_sw != -1:
            cannons.health_decrease(cannon_sw, self.damage)

        elif th_l != -1 or th_r != -1 or th_u != -1 or th_d != -1 or th_ne != -1 or th_nw != -1 or th_se != -1 or th_sw != -1:
            th.health_decrease(self.damage)       

    def attack_wall(self,i,walls):
        """Attacking."""

        wall_l = walls.check_coordinates(self.y[i], self.x[i]-1)
        wall_r = walls.check_coordinates(self.y[i], self.x[i]+1)
        wall_u = walls.check_coordinates(self.y[i]-1, self.x[i])
        wall_d = walls.check_coordinates(self.y[i]+1, self.x[i])
        wall_ne = walls.check_coordinates(self.y[i]-1, self.x[i]+1)
        wall_nw = walls.check_coordinates(self.y[i]-1, self.x[i]-1)
        wall_se = walls.check_coordinates(self.y[i]+1, self.x[i]+1)
        wall_sw = walls.check_coordinates(self.y[i]+1, self.x[i]-1)
            
        if wall_l != -1:
            walls.health_decrease(wall_l, self.damage)
        elif wall_r != -1:
            walls.health_decrease(wall_r, self.damage)
        elif wall_u != -1:
            walls.health_decrease(wall_u, self.damage)
        elif wall_d != -1:
            walls.health_decrease(wall_d, self.damage)
        elif wall_ne != -1:
            walls.health_decrease(wall_ne, self.damage)
        elif wall_nw != -1:
            walls.health_decrease(wall_nw, self.damage)
        elif wall_se != -1:
            walls.health_decrease(wall_se, self.damage)
        elif wall_sw != -1:
            walls.health_decrease(wall_sw, self.damage)
        
            




    



