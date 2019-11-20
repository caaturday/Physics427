'''
Cindy & Ryan
physics 427 advanced lab
Chaotic Rotor lab
October 19, 2019 
'''


import pyvisa
import time
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.animation as animation
import matplotlib as mpl
from astropy.table import Table, Column
from astropy.io import ascii


plt.close('all')

# setting plotting options
grid_style =   {     'alpha' : '0.75',
                 'linestyle' : ':' }
legend_style = {  'fontsize' : '10'} 
font_syle =    {      'size' : '14' }
mpl.rc(  'font', **font_syle)
mpl.rc(  'grid', **grid_style)
mpl.rc('legend', **legend_style)


rm = pyvisa.ResourceManager()
print(rm.list_resources())#Show location of devices
OSC = rm.open_resource('ASRL4::INSTR')#location of the device
print(OSC.query('*IDN?'))
OSC.write('*RST')

###############################################################################
#
#           data table, column function, arrays and plotting function
#
###############################################################################
numPoints = 5000 # number of data points

index = np.arange(0, numPoints)
chaosTable = Table([index], names='i')

# function adds new columns to chaos_table
def column(data, columnName):
    c = Column(data= data, name= columnName)
    chaosTable.add_column(c)

# making column names for each column in the table, JUST SAYING I, Cindy, made them manually! is there a better way I didn't think about?
timeColumn = np.array([['time1', 'time2', 'time3', 'time4'],
              ['time5', 'time6', 'time7', 'time8'],
              ['time9', 'time10', 'time11', 'time12'],
              ['time13', 'time14', 'time15', 'time16']])
# update, ryan made me make 2D arrays
angposColumn = np.array([['angpos1', 'angpos2', 'angpos3', 'angpos4'],
                ['angpos5', 'angpos6', 'angpos7', 'angpos8'],
                ['angpos9', 'angpos10', 'angpos11', 'angpos12'],
                ['angpos13', 'angpos14', 'angpos15', 'angpos16']])

angvelColumn = np.array([['angvel1', 'angvel2', 'angvel3', 'angvel4'],
                [ 'angvel5', 'angvel6', 'angvel7', 'angvel8'],
                ['angvel9', 'angvel10', 'angvel11', 'angvel12'],
                ['angvel13', 'angvel14', 'angvel15', 'angvel16']])

# ryan and I need an intern, com mon eric, use your chair power to get us an intern to make lables for our code
trialTitles = np.array([['Frequency: 0.25Hz     Amplitude: 2.5V', 'Frequency: 0.50Hz    Amplitude: 2.5V', 'Frequency: 0.75Hz    Amplitude: 2.5V', 'Frequency: 1.0Hz     Amplitude: 2.5V'],
                [ 'Frequency: 0.25Hz    Amplitude: 5.0V', 'Frequency: 0.50Hz    Amplitude: 5.0V', 'Frequency: 0.75Hz    Amplitude: 5.0V', 'Frequency: 1.0Hz     Amplitude: 5.0V'],
                ['Frequency: 0.25Hz     Amplitude: 7.5V', 'Frequency: 0.50Hz    Amplitude: 7.5V', 'Frequency: 0.75Hz    Amplitude: 7.5V', 'Frequency: 1.0Hz     Amplitude: 7.5V'],
                ['Frequency: 0.25Hz     Amplitude: 10.0V', 'Frequency: 0.50Hz   Amplitude: 10.0V', 'Frequency: 0.75Hz   Amplitude: 10.0V', 'Frequency: 1.0Hz    Amplitude: 10.0V']])

# frequency and amplitude 
FREQ_arr = np.array(['FREQ 0.25', 'FREQ 0.5', 'FREQ 0.75', 'FREQ 1.0'])
AMPL_arr = np.array(['AMPL 250', 'AMPL 500', 'AMPL 750', 'AMPL 1000'])


# function creates plots for every combination of frequency and amplitude
def plottingChaos(angpos, angvel, title):
    
    fig, ax = plt.subplots(1,1, figsize=(8,4))
    
    ax.scatter(angpos, angvel, color='#458B74', alpha=0.2, marker='o')
    
    ax.grid()
    ax.set_title(title)
    ax.set_ylabel('Angular Velocity (rad/s)')
    ax.set_xlabel('Angular Position (rad)')
    ax.set_ylim([-20, 20])
    ax.set_xlim([-np.pi, np.pi])

###############################################################################
#
#        collecting data
#
###############################################################################

def getValues():
    x = np.pi*float(OSC.query('POSN?'))/2048     # theta in degrees
    t = (float(OSC.query('TIME?')) - to)/1e6   # microseconds    
    return x, t

def amplitude(AMPL):
    OSC.write(AMPL)
    time.sleep(1)
    amp = float(OSC.query('AMPL?'))/100
    print('Amplitude: ', amp, 'V')

def frequency(FREQ):
    OSC.write(FREQ)
    time.sleep(1)
    freq = float(OSC.query('FREQ?'))
    print('Frequency: ', freq, 'Hz' )

time_arr = np.zeros([numPoints])
pos_arr = np.zeros([numPoints])
vel_arr = np.zeros([numPoints])

# recording data and appending columns to chaos table
for i in range(len(FREQ_arr)):
    print('-------------------------')
    print('Changing Frequency...')
    frequency(FREQ_arr[i])
    
    for j in range(len(AMPL_arr)):
        print('Changing Amplitude...')
        amplitude(AMPL_arr[j])
        OSC.write('COIL1')
        
        OSC.write('ZERO') #Reset inital position
        to = float(OSC.query('TIME?'))# initial time,will be subtracted from time measurments
        for k in range(0, numPoints):
            pos_arr[k],time_arr[k] = getValues()
            vel_arr[k] = (pos_arr[k] - pos_arr[k-1])/(time_arr[k] - time_arr[k-1])

        figureTitle = trialTitles[i,j]
        timeLable = timeColumn[i,j]
        angposLable = angposColumn[i,j]
        angvelLable = angvelColumn[i,j]        
        column(time_arr, timeLable)            
        column(pos_arr, angposLable)
        column(vel_arr, angvelLable)
        
        angpos = pos_arr
        angvel = vel_arr
        plottingChaos(angpos, angvel, figureTitle)
        
        print('Done recording this trial')
        print('-------------------------')
        time.sleep(2) #Allow oscillator to settle
        OSC.write('COIL0')

print(chaosTable)

#data_table = Table.read('chaosData.txt', format='ascii.commented_header',
#                        include_names=['angpos1','angvel1'])
#
# 
#
#pos_plot0, vel_plot0 = data_table['angpos1'][:5],data_table['angvel1'][:5]
#
#plottingChaos(pos_plot0, vel_plot0)     

###############################################################################
#
#        writing chaos table to a text file
#
###############################################################################
ascii.write(chaosTable, 'chaosData2.txt', format='commented_header', overwrite=True)


print('-----------')
print('All done :)')
OSC.write('COIL0')
OSC.close()
