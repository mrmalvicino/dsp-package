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
# fineleectricidad


def gen_sin_list(*frequencies, A=1, f_s = 44100, is_closed_interval = True):
    t = np.arange(0, 1/closest_to_average(frequencies) + int(is_closed_interval)/f_s , 1/f_s)

    output = []

    for i in range(0, len(frequencies), 1):
        omega_i = 2*np.pi*frequencies[i]
        y_i = A*np.sin(omega_i*t)

        if frequencies[i] == closest_to_average(frequencies):
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
    
    plt.xticks(np.linspace(0, 1 / freq_ave, 5))
    plt.legend(labels, loc = "upper right")

    return