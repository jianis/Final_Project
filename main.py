import numpy as np
from numpy.linalg import cholesky
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import truncnorm
from scipy.stats import norm
from random import uniform
import threading as thd
import time

def create_MMR(KDA,time,win_perc):

    pass

def create_player():
    #分数范围: 0-5000, 正态分布
    #ID, MMR, WaitingTime
    Size = 1000
    mu = 2500
    sigma = 833
    lower = 0
    upper = 5000
    # np.random.seed(0)
    # instantiate an object X using the above four parameters,
    X = truncnorm((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
    # generate 1000 sample data
    samples = X.rvs(300)
    # compute the PDF of the sample data
    pdf_probs = truncnorm.pdf(samples, (lower - mu) / sigma, (upper - mu) / sigma, mu, sigma)
    # compute the CDF of the sample data
    cdf_probs = truncnorm.cdf(samples, (lower - mu) / sigma, (upper - mu) / sigma, mu, sigma)
    # make a histogram for the samples
    s  = np.random.normal(mu, sigma, Size )
    # plt.hist(samples, bins=50, normed=True, alpha=0.3, label='histogram')
    plt.hist(s, 30, normed=True)
    plt.show()

    return s


def create_match_pool(player_list):
    # waiting_time_list = [0 for n in range(500)]
    match_list = []

    for i in range(0,499):
        if player_list[i]:

            for j in range(i+1,500):
                if player_list[j]:
                    if player_list[j] > player_list[i] - 100 and player_list[j] < player_list[i]+100:
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
    return match_list

def compute_ELO():
    pass

def match(match_list):
    for i in range(len(match_list)):
        if match_list[i][0] < match_list[i][1]:
            pass
    pass

def main_simulation(player,):
    pass

if __name__ == "__main__":
    list = create_player()

    match_list = create_match_pool(list)
    print(match_list)