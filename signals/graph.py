import matplotlib.pyplot as plt
import numpy as np
import os
import sys

root_dir = os.path.dirname(__file__)
python_functions_path = os.path.realpath(os.path.join(root_dir, '..', 'python-functions'))
sys.path.insert(0, python_functions_path)

import python_functions as pyfun

def plot(x, y, **kwargs):
    plt.figure(figsize=(8,4))
    plt.plot(x,y, **kwargs)
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")

    return

def plot_LR(x, y, **kwargs):
    
    """
    Generates a plot using matplotlib.

    Parameters
    ----------

    x : NUMPY ARRAY
        Data for the horizontal axis.
    
    y : TUPLE OF NUMPY ARRAYS
        Data for the vertical axes. A two dimentions tuple is expected, containing the data for the left and right vertical axes in each component respectively.

    **kwargs : UNPACKED DICTIONARY
        Object orientated kwargs values for matplotlib.pyplot.plot() and matplotlib.pyplot.setp() methods.
        Bidimentional tuples are expected for the keys that involves the vertical axes.
        For example, the scale could be determined by defining the dictionary kwargs = {'xscale': 'linear', 'yscale': ('logit','log')} and using it into plot_LR(x, y, **kwargs).

    Returns
    -------

    none
    """

    # Store the **kwargs in a new dictionary:
    user_inputs = kwargs

    # Define possible **kwargs:
    kwargs = {
        'figsize': (10,5),
        'title': 'Plot',
        'xlabel': '',
        'ylabel': ('',''),
        'xscale': 'linear',
        'yscale': ('linear','linear'),
        'legend': ('',''),
        'xticks': 'default',
        'yticks': ('default','default'),
        'xticklabels': 'default',
        'yticklabels': ('default','default'),
        'xlim': 'default',
        'ylim': ('default','default'),
        'save': False,
        'save_folder': 'default'
    }

    # Overwrite the possible **kwargs with the actual inputs:
    for key, value in user_inputs.items():
        if key in kwargs:
            kwargs[key] = value
    
    # Split the plt.setp kwargs into 2 dictionaries:
    setpL = dict()
    setpR = dict()

    setpL_keys = ['yticks', 'yticklabels', 'ylim', 'xticks', 'xticklabels', 'xlim']
    setpR_keys = ['yticks', 'yticklabels', 'ylim']

    for key in setpL_keys:
        if len(kwargs[key]) == 2:
            if kwargs[key][0] != 'default':
                setpL.update({key: kwargs[key][0]})
        else:
            if kwargs[key] != 'default':
                setpL.update({key: kwargs[key]})

    for key in setpR_keys:
        if len(kwargs[key]) == 2:
            if kwargs[key][1] != 'default':
                setpR.update({key: kwargs[key][1]})

    # Generate plot:
    fig, (axisL) = plt.subplots(1,1, figsize=kwargs['figsize'])
    axisR = axisL.twinx()
    
    axisL.plot(x, y[0], color='blue')
    axisR.plot(x, y[1], color='red', linestyle='--')
    
    axisL.set_xlabel(kwargs['xlabel'])
    axisL.set_ylabel(kwargs['ylabel'][0])
    axisR.set_ylabel(kwargs['ylabel'][1])
    
    axisL.set_xscale(kwargs['xscale'])
    axisL.set_yscale(kwargs['yscale'][0])
    axisR.set_yscale(kwargs['yscale'][1])
    
    axisL.set_title(kwargs['title'])
    axisL.legend([kwargs['legend'][0]], loc='lower left')
    axisR.legend([kwargs['legend'][1]], loc='lower right')

    plt.setp(axisL, **setpL)
    plt.setp(axisR, **setpR)
    
    axisL.grid()
    plt.tight_layout()
    graph = plt.gcf()

    # Save plot:
    if kwargs['save'] == True:
        if kwargs['save_folder'] == 'default':
            kwargs['save_folder'] = os.path.dirname(__file__)
        title = kwargs['title']
        graph.savefig(os.path.join(kwargs['save_folder'], f'{title}'+'.png'))
    else:
        plt.show()

    return


def gen_ticks(n, N=20):
    
    """
    Generates a list of N ticks that are simetrically distributed along n and can be used in matplotlib.pyplot.setp() method.

    Parameters
    ----------

    n : LIST
        Array like data from where the ticks will be extracted.
    
    N : INTEGER
        Amount of ticks which are going to be extracted from the input data.

    Returns
    -------

    ticks : LIST
    """
    
    n = pyfun.make_list(n)
    ticks = []
    
    if n != []:    
        if len(n)%2 != 0:
            del n[-1] # Set n to even lenght
        
        while len(n)%N != 0:
            N = N - 1 # Set N to greatest common divisor
        
        ticks = [None]*N
        K = int(len(n)/N)
        
        for i in range(1, N+1, 1):
            ticks[i-1] = n[K*i-1]
    
    return ticks


def gen_ticks_oct():
    
    """
    Generates a list of ticks and anotherone of ticklabels that can both be used in matplotlib.pyplot.setp() method. The ticks are set to octaves, and defined according to UNE-EN 61260.

    Parameters
    ----------

    none

    Returns
    -------

    ticks : LIST

    ticklabels : LIST
    """
    
    ticks = []
    ticklabels = []
    
    for i in range(0, 10, 1):
            ticks.append(31.25*(2**i))
            if 31.25*(2**i) < 1000:
                ticklabels.append(str(int(31.25*(2**i))))
            else:
                ticklabels.append(str(int((31.25/1000)*(2**i)))+'k')
    
    return ticks, ticklabels


def plot_sin_list(tuples_list, **plot_kwargs):
    
    """
    Plots a list of sine waveforms in an interval determined by the average period of all the signals.

    Parameters
    ----------
    tuples_list : LIST OF TUPLES
        List of tuples containing each tuple the x-y axes data in the first two components.
        The third component of each tuple have to be a string carring the label of the respective signal, with the following format:
            'sin_N_freq_FHz' being N any natural number and F the frequency of the sinewave.
        The label of the sinewave with the average frequency must have the word 'ave' between brackets, have no spaces between characters and have the following format:
            'sin_N_freq_FHz(ave)' being N any natural number and F the frequency of the sinewave.
    
    **plot_kwargs : UNPACKED DICT
        Arguments for the matplotlib.plot() function.

    Returns
    -------
    
    None.

    """
    
    plt.grid()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    
    labels = []
    
    for i in range(0, len(tuples_list), 1):
        x = tuples_list[i][0]
        y = tuples_list[i][1]
        plt.plot(x,y, **plot_kwargs)
        labels.append(tuples_list[i][2])
        if 'ave' in tuples_list[i][2]:
            cut = len(tuples_list[i][2]) - 7
            freq_ave = float(tuples_list[i][2][11:cut])
    
    plt.xticks(np.linspace(0, 1/freq_ave, 5))
    plt.legend(labels, loc="upper right")

    return