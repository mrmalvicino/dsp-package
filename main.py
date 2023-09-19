"""
# electricidad

from matplotlib import pyplot as plt
import numpy as np
import os
import sys

root_dir = os.getcwd()
gen_signals_path = os.path.realpath(os.path.join(root_dir, 'functions'))
sys.path.insert(0, gen_signals_path)
import gen_signals as gensig

wave_frequency = 50
amount_of_periods = 1
sampling_rate = 44100

time_array = gensig.generateTimeArray(wave_frequency, amount_of_periods, sampling_rate)

voltage_phase = 0
voltage_amplitude = 1

voltage_signal = gensig.generateSine(time_array, wave_frequency, phase_deg = voltage_phase, wave_amplitude = voltage_amplitude)

current_phase = 90
current_amplitude = 0.3

current_signal = gensig.generateSine(time_array, wave_frequency, phase_deg = current_phase, wave_amplitude = current_amplitude)

plt.figure(figsize=(8,4))
plt.plot(time_array, voltage_signal, label = "Voltage", color = "blue", linestyle = "-")
plt.plot(time_array, current_signal, label = "Current", color = "red", linestyle = "-")
plt.plot(time_array, voltage_signal * current_signal, label = "Power", color = "green", linestyle = "--")
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.legend()



"""

def plot_dual_axis(x, y, **kwargs):
    """
    Generates a plot using matplotlib.

    Args:
        x (numpy.ndarray) Data for the horizontal axis.
        y (tuple of numpy.ndarray) Data for the vertical axes. A two dimentions tuple is expected, containing the data for the left and right vertical axes in each component respectively.
        **kwargs (unpacked dictionary) Object orientated kwargs values for matplotlib.pyplot.plot() and matplotlib.pyplot.setp() methods. Bidimentional tuples are expected for the keys that involves the vertical axes. For example, the scale could be determined by defining the dictionary kwargs = {'xscale': 'linear', 'yscale': ('logit','log')} and using it into plot_dual_axis(x, y, **kwargs).

    Returns:
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


def save(param, **kwargs):
    
    """
    Saves a given numpy array or matplotlib plot.
    
    Parameters
    ----------
    
    param : FIGURE OR ARRAY
        Object that is going to be saved.
    
    **kwargs : UNPACKED DICTIONARY
    
        **save_kwargs : UNPACKED DICTIONARY
            Kwargs for internal use.
    
            file_dir : STRING
                Path of the directory where the file is going to be saved.
    
            file_name : STRING
                Name of the file which is going to be saved.
    
            ask_for_confirmation : BOOLEAN
                Determines whether the script should ask for user input confirmation.
    
        **savefig_kwargs : UNPACKED DICTIONARY
            Kwargs for the savefig() method.
    
            bbox_inches : STRING
    
            dpi : INTEGER
    
            transparent : BOOLEAN
    
    Raises
    ------
    
    ValueError
        Invalid input.
    
    Returns
    -------
    
    None.

    """
    
    save_kwargs = {'file_dir': os.path.dirname(__file__), 'file_name': 'saved_by_' + os.getlogin(), 'ask_for_confirmation': False}
    
    for key, value in kwargs.items():
        if key in save_kwargs and value != save_kwargs[key]:
            save_kwargs[key] = value
    
    if save_kwargs['ask_for_confirmation'] == True:
        save = 'ask'
    else:
        save = 'y'

    while save != 'y' and save != 'n':
        save = input('Do you really want to save? [y/n] ')
    
    if save == 'y':
        if type(param) == plt.Figure:
            savefig_kwargs = {'bbox_inches': 'tight', 'dpi': 300, 'transparent': False}
            
            for key, value in kwargs.items():
                if key in savefig_kwargs and value != savefig_kwargs[key]:
                    savefig_kwargs[key] = value
            
            param.savefig(os.path.join(save_kwargs['file_dir'], save_kwargs['file_name'] + '.png'), **savefig_kwargs)
        
        elif type(param) == np.ndarray:
            np.save(os.path.join(save_kwargs['file_dir'], save_kwargs['file_name']), param)
        
        else:
            raise ValueError(f'{type(param)} input not supported.')
    
    return