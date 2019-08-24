# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import math
import matplotlib.pyplot as plt
import numpy as np

def rand_walk(n):
    """return the coordinate of x, y after random walks of n steps"""
    available_steps = [(0,1),(0,-1),(1,0),(-1,0)]
    x, y = 0, 0
    
    for i in range(n):
        (dx, dy) = random.choice(available_steps)
        x += dx
        y += dy
        
    return x, y

def distance(x,y):
    return abs(x) + abs(y)

def cart_distance(x,y):
    return math.sqrt(x**2 + y**2)

if __name__ == '__main__':
    # messages for stdout
    dis_msg = 'average distance from home is {:.2f} for {} steps'
    call_msg = '{:.2f} % of walks needs a ride home'
    
    # some parameters for this simulation
    MCsteps = 100000
    taxi_call = 5
    
    
    for i in range(29,31):
        tot_dis = 0
        num_calls = 0
        conf = np.zeros((2,MCsteps))
        
        for j in range(MCsteps):
            x, y = rand_walk(i)
            conf[0,j] = x
            conf[1,j] = y
            d = distance(x, y)
            tot_dis += d
            if d > taxi_call:
                num_calls += 1
                
        tot_dis /= MCsteps
        num_calls /= MCsteps
        print( dis_msg.format(tot_dis, i) )
        print( call_msg.format(num_calls*100))
        
        plt.scatter(conf[0], conf[1])
        plt.grid(True)
        
        plt.show()
        plt.close()
        
        plt.hist2d(conf[0], conf[1])
        plt.grid(True)
        plt.show()
        plt.close