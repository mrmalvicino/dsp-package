"""
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