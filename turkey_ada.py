#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 12:05:47 2022

@author: shamdoran
"""

import numpy as np
import matplotlib.pyplot as plt

## If you have a continuous cost (costA) and you reduce this (costB) and stake the savings in ADA, what is your return over a specified time horizon? 

## Adjustable parameters:
costA = 64.90 #monthly in USD (the more expensive option must be costA)
costB = 33.33 #monthly in USD
time_horizon = 20 # in years
final_ADA_prices = [1.5,5,10] # in USD. add as many as you want, separated by a comma
starting_ADA_price = 1.36 #in USD
inflation = .03 #annual percentage as a proportion in USD, i.e., 3% = .03
staking_return = .05 #annual percentage as a proportion in ADA, i.e., 5% = .05
cost_fee = .02 #cost of aquiring ADA, percentage as a proportion in USD, i.e., 2% = .02
##

time_horizon_in_days = time_horizon*365
font = {'family' : 'helvetica',
        'weight' : 'normal',
        'size'   : 20}

plt.figure(figsize = (10, 8),dpi=300)
plt.rc('font', **font)
for fa in final_ADA_prices:
    
    investment_over_time = np.zeros(time_horizon_in_days)
    ADA_daily_unit_growth = (fa - starting_ADA_price) / time_horizon_in_days
    ADA_bank = 0
    time_since_last_invest = 0 #in days
    time_since_last_reward = 0 #in days
    ADA_price = starting_ADA_price
    costA_inf = costA
    costB_inf = costB
    
    for day in np.arange(0,time_horizon_in_days):
        
        time_since_last_invest = time_since_last_invest + 1
        time_since_last_reward = time_since_last_reward + 1
        ADA_price = ADA_price + ADA_daily_unit_growth
        
        if time_since_last_reward==4:
            time_since_last_reward=0
            ADA_bank = ADA_bank*(1+(staking_return/73))
            
        if time_since_last_invest==30:
            costA_inf=costA_inf*(1+(inflation/12))
            costB_inf=costB_inf*(1+(inflation/12))
            time_since_last_invest=0
            to_be_invested_USD = costA_inf - costB_inf
            to_be_invested_ADA = (to_be_invested_USD*(1-cost_fee)) / ADA_price
            ADA_bank = ADA_bank + to_be_invested_ADA
        
        investment_over_time[day] = ADA_bank*ADA_price
        
    plt.plot(np.arange(0,time_horizon_in_days),investment_over_time)
    plt.text(time_horizon_in_days,investment_over_time[-1]+2000,'If ADA hits $'+str(fa))
    plt.text(time_horizon_in_days,investment_over_time[-1]-2000,'$'+str(np.round(investment_over_time[-1])))
    plt.xlabel('days since you start roasting your own turkey')
    plt.ylabel('investment yield (in USD)')

import matplotlib as mpl
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
plt.show()
plt.savefig('turkey_ada.png')
        
        
        
        
        
        
