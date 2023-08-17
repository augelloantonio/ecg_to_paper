import os
import numpy as np 
from math import ceil 
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import utils.ecg_filter as ecg_filter

def _ax_plot(ax, x, y, secs=10, lwidth=0.5, amplitude_ecg = 2.5, time_ticks = 0.2):
    ax.set_xticks(np.arange(0,secs,time_ticks))    
    ax.set_yticks(np.arange(-ceil(amplitude_ecg),ceil(amplitude_ecg),1.0))

    ax.minorticks_on()
    
    ax.xaxis.set_minor_locator(AutoMinorLocator(5))

    ax.set_ylim(-amplitude_ecg, amplitude_ecg)
    ax.set_xlim(0, secs)

    ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    ax.grid(which='minor', linestyle='-', linewidth='0.5', color=(1, 0.7, 0.7))

    ax.plot(x,y, linewidth=lwidth)

def plot_single_lead(ecg, save_fig_path, file_name, sample_rate=500, normalize_ecg=False, title = None, fig_width = 15, fig_height = 4, line_w = 1, ecg_amp = 5, timetick = 0.2):
    """
    Plot multi lead ECG chart.
    
    # Arguments
        ecg        : m x n ECG signal data, which m is number of leads and n is length of signal.
        sample_rate: Sample rate of the signal.
        title      : Title which will be shown on top off chart
        fig_width  : The width of the plot
        fig_height : The height of the plot
    """
    print(len(ecg))
    ecg_amp = int((len(ecg)/sample_rate)/2)

    if title == None:
        title = file_name[:len(file_name)-4]

    if normalize_ecg:
        ecg = ecg_filter.movingAverageMean(ecg, 25)
        
    plt.figure(figsize=(fig_width,fig_height))
    plt.suptitle(title)
    
    plt.subplots_adjust(
        hspace = 0, 
        wspace = 0.04,
        left   = 0.04,  # the left side of the subplots of the figure
        right  = 0.98,  # the right side of the subplots of the figure
        bottom = 0.2,   # the bottom of the subplots of the figure
        top    = 0.88
        )
    seconds = len(ecg)/sample_rate

    ax = plt.subplot(1, 1, 1)
    step = 1.0/sample_rate
    
    _ax_plot(ax,np.arange(0,len(ecg)*step,step),ecg, seconds, line_w, ecg_amp, timetick)
    
    if not os.path.exists(save_fig_path):
        os.makedirs(save_fig_path)

    plt.savefig(save_fig_path + "/" + title)