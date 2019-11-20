'''
Cindy & Ryan
physics 427 advanced lab
Chaotic Rotor lab
October 20, 2019 
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from astropy.table import Table
#from toomanytimes import plottingChaos

plt.close('all')

grid_style =   {     'alpha' : '0.75',
                 'linestyle' : ':' }
legend_style = {  'fontsize' : '10'} 
font_syle =    {      'size' : '14' }
mpl.rc(  'font', **font_syle)
mpl.rc(  'grid', **grid_style)
mpl.rc('legend', **legend_style)

# reading data from txt file
data_table = Table.read('chaosData.txt', format='ascii.commented_header')
trialTitles = np.array([['Frequency: 0.25Hz     Amplitude: 2.5V', 'Frequency: 0.25Hz    Amplitude: 5.0V', 
                         'Frequency: 0.25Hz     Amplitude: 7.5V','Frequency: 0.25Hz     Amplitude: 10.0V'],
                        ['Frequency: 0.50Hz    Amplitude: 2.5V',  'Frequency: 0.50Hz    Amplitude: 5.0V',
                         'Frequency: 0.50Hz    Amplitude: 7.5V', 'Frequency: 0.50Hz   Amplitude: 10.0V'],
                        ['Frequency: 0.75Hz    Amplitude: 2.5V', 'Frequency: 0.75Hz    Amplitude: 5.0V',
                         'Frequency: 0.75Hz    Amplitude: 7.5V', 'Frequency: 0.75Hz   Amplitude: 10.0V'], 
                        ['Frequency: 1.0Hz     Amplitude: 2.5V','Frequency: 1.0Hz     Amplitude: 5.0V',
                         'Frequency: 1.0Hz     Amplitude: 7.5V', 'Frequency: 1.0Hz    Amplitude: 10.0V']])
                     

###############################################################################
#
#        poincare plot function
#
###############################################################################
def time(T, angpos, angvel):
    numPoints = 5000
    numPoinPoints = numPoints//T
        
    pos_poin = np.zeros(numPoinPoints)
    vel_poin = np.zeros(numPoinPoints)
    


    for i in range(numPoinPoints):
        pos_poin[i] = angpos[i*T]
        vel_poin[i] = angvel[i*T]
        
    return pos_poin, vel_poin


def poinCare(T, angpos1, angvel1, angpos2, angvel2, angpos3, angvel3, angpos4, angvel4, title, period, savefig,
             xlim00 = [-np.pi, np.pi], xlim10 = [-np.pi, np.pi], xlim01 = [-np.pi, np.pi], xlim11 = [-np.pi, np.pi],
             ylim00 = None, ylim10 = None, ylim01 = None, ylim11 = None, 
             ):        
    fig, axs = plt.subplots(2, 2, figsize=(9, 3))
    fig.subplots_adjust(hspace = 0.5)        
    
    pos_poin1, vel_poin1 = time(T, angpos1, angvel1)
    axs[0, 0].scatter(angpos1, angvel1, color='#458B74', alpha= 0.2, marker='.')
    axs[0, 0].scatter(pos_poin1, vel_poin1, color='black', alpha=1, marker='*')
    axs[0, 0].grid()
    axs[0, 0].set_xlabel('Angular Position (rad)')
    axs[0, 0].set_ylabel('Angular Velocity (rad/s)')
    axs[0, 0].set_xlim(xlim00)
    axs[0, 0].set_ylim(ylim00)
    axs[0, 0].set_title(title[0])
    fig.savefig(savefig)
    
    pos_poin2, vel_poin2 = time(T, angpos2, angvel2)
    axs[1, 0].scatter(angpos2, angvel2, color='#458B74', alpha= 0.2, marker='.')
    axs[1, 0].scatter(pos_poin2, vel_poin2, color='black', alpha=1, marker='*')
    axs[1, 0].grid()
    axs[1, 0].set_xlabel('Angular Position (rad)')
    axs[1, 0].set_ylabel('Angular Velocity (rad/s)')
    axs[1, 0].set_xlim(xlim10)
    axs[1, 0].set_ylim(ylim10)
    axs[1, 0].set_title(title[1])
    fig.savefig(savefig)
    pos_poin3, vel_poin3 = time(T, angpos3, angvel3)
    axs[0, 1].scatter(angpos3, angvel3, color='#458B74', alpha= 0.2, marker='.')
    axs[0, 1].scatter(pos_poin3, vel_poin3, color='black', alpha=1, marker='*')
    axs[0, 1].set_ylim([-8, 8])
    axs[0, 1].grid()
    axs[0, 1].set_xlabel('Angular Position (rad)')
    axs[0, 1].set_ylabel('Angular Velocity (rad/s)')
    axs[0, 1].set_xlim(xlim01)
    axs[0, 1].set_ylim(ylim01)
    axs[0, 1].set_title(title[2])
    fig.savefig(savefig)

    pos_poin4, vel_poin4 = time(T, angpos4, angvel4)  
    axs[1, 1].scatter(angpos4, angvel4, color='#458B74', alpha= 0.2, marker='.')
    axs[1, 1].scatter(pos_poin4, vel_poin4, color='black', alpha=1, marker='*')
    axs[1, 1].set_ylim([-15, 15])
    axs[1, 1].grid()
    axs[1, 1].set_xlabel('Angular Position (rad)')
    axs[1, 1].set_ylabel('Angular Velocity (rad/s)')
    axs[1, 1].set_xlim(xlim11)
    axs[1, 1].set_ylim(ylim11)
    axs[1, 1].set_title(title[3])
    fig.savefig(savefig)

    fig.suptitle(period)

def forRyan(T, time1, angpos1, angvel1, title):
    numPoints = 5000
    numPoinPoints = numPoints//T
    
    time_poin = np.zeros(numPoinPoints)
    pos_poin = np.zeros(numPoinPoints)
    vel_poin = np.zeros(numPoinPoints)
    


    for i in range(numPoinPoints):
        time_poin[i] = time1[i*T]
        pos_poin[i] = angpos1[i*T]
        vel_poin[i] = angvel1[i*T]
        
        
    fig, ax = plt.subplots(1, 1, figsize=(9, 3))
    
    ax.scatter(angpos1, angvel1, color='#458B74', alpha= 0.2, marker='o')
    ax.scatter(pos_poin, vel_poin, color='black', alpha=1, marker='*')
    ax.set_ylim([-20, 20])
    ax.grid()
    ax.set_title('$T = 200s$')
    ax.set_xlabel('Angular Position (rad)')
    ax.set_ylabel('Angular Velocity (rad/s)')
    ax.set_xlim([-np.pi, np.pi])
    fig.savefig(T)


    fig.suptitle('Example of Period Tripling \n Amplitude: 5.0V   Frequency: 1.00Hz')

#-------------------------------- trials 1 - 4
T = 400 #seconds 
title = trialTitles[0]

p1, p2, p3, p4 = data_table['angpos1'], data_table['angpos2'], data_table['angpos3'], data_table['angpos4']
v1, v2, v3, v4 = data_table['angvel1'], data_table['angvel2'], data_table['angvel3'], data_table['angvel4']

#poinCare(T, p1, v1, p2, v2, p3, v3, p4, v4, 
#         title = title, period = '$T = 400s$', 
#         savefig= '400.png')

#-------------------------------- trials 5-8
T = 200 #seconds 
title = trialTitles[1]

p5, p6, p7, p8 = data_table['angpos5'], data_table['angpos6'], data_table['angpos7'], data_table['angpos8']
v5, v6, v7, v8 = data_table['angvel5'], data_table['angvel6'], data_table['angvel7'], data_table['angvel8']

#poinCare(T, p5, v5, p6, v6, p7, v7, p8, v8, 
#         title = title, period = '$T = 200s$',
#         ylim00 = [-8, 8], ylim10 = [-10, 10],
#         savefig= '200.png')

#-------------------------------- trials 9- 12
T = 133 #seconds 
title = trialTitles[2]
p9, p10, p11, p12 = data_table['angpos9'], data_table['angpos10'], data_table['angpos11'], data_table['angpos12']
v9, v10, v11, v12 = data_table['angvel9'], data_table['angvel10'], data_table['angvel11'], data_table['angvel12']

#poinCare(T, p9, v9, p10, v10, p11, v11, p12, v12, 
#         title = title, period = '$T = 133s$',
#         ylim00 = [-10, 10], ylim10 = [-10, 10],
#         savefig= '133.png')

#-------------------------------- trials 13, 16
T = 100 #seconds 
title = trialTitles[3]

p13, p14, p15, p16 = data_table['angpos13'], data_table['angpos14'], data_table['angpos15'], data_table['angpos16']
v13, v14, v15, v16 = data_table['angvel13'], data_table['angvel14'], data_table['angvel15'], data_table['angvel16']

#poinCare(T, p13, v13, p14, v14, p15, v15, p16, v16, 
#         title = title, period = '$T = 133s$',
#          ylim10 = [-15, 15],
#          savefig= '100.png')

#-------------------------------- for ryan
t8, p8, v8 = data_table['time8'], data_table['angpos8'], data_table['angvel8']
T = 200
forRyan(T, t8, p8, v8, title= 'trial 8')
