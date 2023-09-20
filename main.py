import os
import sys

root_dir = os.getcwd()
new_path = os.path.realpath(os.path.join(root_dir, 'signals'))
sys.path.insert(0, new_path)

#################################
## Generator and Graph classes ##
#################################

# Imports

from functions import *

from generator import Generator
generator = Generator()

from graph import Graph
graph = Graph()

# Square pulse

is_closed_interval = True
starting_sample = 0
ending_sample = 25
turn_on = 5
turn_off = 10

samples_array = generator.samples_array(starting_sample, ending_sample, is_closed_interval)
discrete_signal = generator.square_pulse(samples_array, turn_on, turn_off)

square_pulse_graph = graph.plot_multiple_overlaids(samples_array, [discrete_signal], ['Square pulse'], True)

# Sinewaves with parameters

time_array = generator.arange_time_array(wave_frequency = 200, is_closed_interval = True)

sine_array_1 = generator.sinewave(time_array, wave_frequency = 200)
sine_array_2 = generator.sinewave(time_array, wave_frequency = 2000, wave_amplitude = 0.5)
sine_array_3 = generator.sinewave(time_array, wave_frequency = 500, phase_deg = 90)

y_data_list = [sine_array_1, sine_array_2, sine_array_3]
y_legends_list = ['200 Hz', '2k Hz', '500 Hz']

sinewave_graph = graph.plot_multiple_overlaids(time_array, y_data_list, y_legends_list)

# List of sinewaves

list_of_tuples = generator.sinewaves_list(200, 2000, 500)
sinewaves_list_graph = graph.sinewaves_list(list_of_tuples)

# Save arrays and graph

save_plot(sinewave_graph, file_dir = os.path.join(root_dir, 'output'), file_name = 'sinewaves_plot')
save_array(samples_array, file_dir = os.path.join(root_dir, 'output'), file_name = 'sq_samples')
save_array(discrete_signal, file_dir = os.path.join(root_dir, 'output'), file_name = 'sq_amplitude')