from matplotlib import pyplot as plt
import numpy as np
import os
import sys

root_dir = os.path.dirname(__file__)
python_functions_path = os.path.realpath(os.path.join(root_dir, '..', '..', 'python-functions'))
sys.path.insert(0, python_functions_path)
matplotlib_functions_path = os.path.realpath(os.path.join(root_dir, '..', '..', 'matplotlib-functions'))
sys.path.insert(0, matplotlib_functions_path)

import python_functions as pyfun
import matplotlib_functions as matplt


def gen_discrete_signals(signal_name, n_start=-10, n_end=10, n_0=10, on=5, off=15, m=5, mu=0, sigma=1, isClosedInterval = True, **kwargs):
    
    """
    Generates a custom discrete signal and optionally saves the plot and arrays involved.
    
    Parameters
    ----------
    
    signal_name : STR
        Name of the signal which is going to be generated. E.g., unitImpulse, unitStep, sqPulse, triangPulse, rnd.
    
    n_start : INT, optional
        Starting sample. The default is -10.
    
    n_end : INT, optional
        Ending sample. The default is 10.
    
    n_0 : INT, optional
        Sample at which the unitImpulse is and at which the unitStep begins. The default is 10.
    
    on : INT, optional
        Sample at which the sqPulse goes from 0 to 1. The default is 5.
    
    off : INT, optional
        Sample at which the sqPulse goes from 1 to 0. The default is 15.
    
    m : INT, optional
        Half of the triangPulse base lenght. The default is 5.
    
    mu : INT, optional
        Mean or expected value. The default is 0.
    
    sigma : FLOAT, optional
        Standard deviation. The default is 1.
    
    isClosedInterval : BOOL, optional
        Determines whether the bound of the samples interval belongs to it or not. The default is True.
    
    **kwargs : UNPACKED DICT
        Optional saving parameters.
    
        save_plot : BOOL
            Determines whether the plot is saved to a .png file.
            
        save_array : BOOL
            Determines whether the sample and amplitude arrays are saved to .npy files.

    Raises
    ------
    
    ValueError
        The parameter n_start must be less than n_end by definition.
    
    ValueError
        The parameter n_0 does not belong to the interval [n_start,n_end].
    
    ValueError
        Duty Cycle can not be greater than 100%.
    
    ValueError
        The parameter m must be greater than 0 and less than (n_end-n_start)/2.
    
    ValueError
        Invalid input.

    Returns
    -------
    
    None.

    """
    
    
    # Defines samples interval
    
    if not n_start < n_end:
        raise ValueError('The parameter n_start must be less than n_end by definition.')
    
    n = np.arange(n_start, n_end + int(isClosedInterval), 1)
    
    
    # Defines signal waveform
    
    if signal_name == 'unitImpulse':
        
        if n_0 > len(n):
            raise ValueError('The parameter n_0 does not belong to the interval [n_start,n_end].')
        
        x = np.zeros(len(n))
        x[n_0] = 1    
    
    elif signal_name == 'unitStep':
        
        if n_0 > len(n):
            raise ValueError('The parameter n_0 does not belong to the interval [n_start,n_end].')
        
        x = np.concatenate((np.zeros(n_0), np.ones(len(n)-n_0)), axis=0)
    
    elif signal_name == 'sqPulse':
        
        dutyCycle = (off-on)*100/len(n)
        
        if dutyCycle > 100:
            raise ValueError('Duty Cycle can not be greater than 100%.')
        
        x = np.concatenate((np.zeros(on), np.ones(off-on), np.zeros(len(n)-off)), axis=0)
    
    elif signal_name == 'triangPulse':
        if m <= 0 or m > len(n)/2:
            raise ValueError('The parameter m must be greater than 0 and less than (n_end-n_start)/2.')
        
        x = np.zeros(len(n))
        
        for i in range(-m, m, 1):
            n_i = int((n_end-n_start)/2 + i)
            x[n_i] = 1-abs(i*(1/m))
    
    elif signal_name == 'rnd':
        x = np.random.normal(mu, sigma, len(n))
    
    else:
        raise ValueError('Invalid input.')
    
    
    # Plot
    
    plot_kwargs = {'alpha': 1, 'color': 'black', 'linestyle': '', 'linewidth': 1, 'marker': 'o'}
    
    plt.figure(figsize=(8,4))
    plt.plot(n,x, **plot_kwargs)
    plt.grid()
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    
    if len(n) < 21:
        plt.xticks(n)
    else:
        plt.xticks(matplt.gen_ticks(n, N=21))
    
    graph = plt.gcf()
    
    
    # Kwargs
    
    for key, value in kwargs.items():
        
        if key == 'save_plot' and value == True:
            save(graph, file_dir=os.path.join(root_dir, 'images'), file_name=signal_name+'Plot')
        
        if key == 'save_array' and value == True:
            save(n, file_dir=os.path.join(root_dir, 'files'), file_name=signal_name+'Array_n')
            save(x, file_dir=os.path.join(root_dir, 'files'), file_name=signal_name+'Array_x')
    
    return


def gen_sin_list(*frequencies, A=1, f_s = 44100, isClosedInterval = True):
    
    """
    Generates a sine wave for each input frequency.

    Parameters
    ----------
    
    *frequencies : UNPACKED TUPLE OF FLOATS
        Unpacked tuple containing the frequency values of the sine waves which are going to be generated.
    
    A : FLOAT, optional
        Amplitude of all the sine waves which are going to be generated. The default is 1.
    
    f_s : FLOAT, optional
        Sampling frequency rate. The default is 44100.
        
    isClosedInterval : BOOL, optional
        Determines whether the bound of the samples interval belongs to it or not. The default is True.

    Returns
    -------
    
    output : LIST OF TUPLES
        For each sine wave generated, the function returns a list of one tuple for every signal.
        Each tuple has three components that contains the time vector, the amplitude vector and a label respectively.
        Thus, the output for n signals generated would be:
        [ (time_1, amplitude_1, label_1) , (time_2, amplitude_2, label_2) , ... , (time_n, amplitude_n, label_n) ]
        Where time_i and amplitude_i are numpy arrays which holds the signal data and label_i is a string with descriptive porposes, being i a natural number between 1 and n.
        The average frequency is specified between brackets in its' label.

    """
    
    t = np.arange(0, 1/pyfun.closest_to_average(frequencies) + int(isClosedInterval)/f_s , 1/f_s)
    
    output = []
    
    for i in range(0, len(frequencies), 1):
        omega_i = 2*np.pi*frequencies[i]
        y_i = A*np.sin(omega_i*t)
        if frequencies[i] == pyfun.closest_to_average(frequencies):
            label = f'sin_{i+1}_freq_{frequencies[i]}Hz(ave)'
        else:
            label= f'sin_{i+1}_freq_{frequencies[i]}Hz'
        signal_i = (t , y_i , label)
        output.append(signal_i)
    
    return output


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

def generateTimeArray(wave_frequency, amount_of_periods = 1, sampling_rate = 44100):
    wave_period = 1 / wave_frequency
    interval_lenght = amount_of_periods * wave_period
    step = 1 / sampling_rate
    time_array = np.arange(0, interval_lenght, step)

    return time_array

def generateSine(time_array, wave_frequency, phase_deg = 0, wave_amplitude = 1):
    omega = 2 * np.pi * wave_frequency
    phase_rad = phase_deg * (np.pi / 180)
    sine_array = wave_amplitude * np.sin(omega * time_array + phase_rad)

    return sine_array