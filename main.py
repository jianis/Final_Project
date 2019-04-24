import numpy as np
from numpy.linalg import cholesky
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import truncnorm
from scipy.stats import norm
from random import uniform
import threading as thd
import time
import datetime

def create_MMR(KDA,time,win_perc):
    pass

def create_player():
    #ID, MMR, WaitingTime
    Size = 10000
    mu = 1120
    sigma = 425
    lower = 0
    upper = 5000
    # np.random.seed(0)
    s  = np.random.normal(mu, sigma, Size)
    plt.hist(s, 30, normed=True)
    plt.show()

    return s


def create_match_pool(player_list, range):
    start = time.time()
    # waiting_time_list = [0 for n in range(500)]
    match_list = []

    for i in range(0,9999):
        if player_list[i]:
            for j in range(i+1,10000):
                if player_list[j]:
                    if player_list[j] > player_list[i] - range and player_list[j] < player_list[i] + range:
                        match_list.append([player_list[i],player_list[j]])
                        player_list[i] = None
                        player_list[j] = None
                        break
                    else:
                        continue
                else:
                    continue
        else:
            continue
    end = time.time()
    print (end - start)
    return match_list

def compare_MMR(match_list, range):
    compare_list = []
    # Use some statistic ways to compute the comparison. Not just find the difference.
    for i in range(0,len(match_list)):
        if abs(match_list[i][0] - match_list[i][1]) > 0.7*range:
            compare_list.append(0)
        else:
            compare_list.append(1)
    return compare_list

def compute_win_lose(enemy_list):
    new_MMR = []
    # for j in range(0,len(match_list)):

    Ea = 1/(1+10**(enemy_list[0]-enemy_list[1]/400))
    Eb = 1 -Ea
    # Create random (1,100). If this number < Ea, A will win.
    number = 1
    if number < Ea:
        win_or_lose_A = 1
        win_or_lose_B = 0 #A win
    else:
        win_or_lose_A = 0
        win_or_lose_B = 1 #A lose
    # return win_or_lose
    new_MMR.append(enemy_list[0] + 16*(win_or_lose_A-Ea))
    new_MMR.append(enemy_list[1] + 16*(win_or_lose_B-Eb))
    return new_MMR

def compute_waiting_time():
    pass

def main_simulation(player):
    pass

if __name__ == "__main__":
    list = create_player()

    match_list = create_match_pool(list)
    print(match_list)