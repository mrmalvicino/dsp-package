import numpy as np
from dsp.functions import to_list


class Ticks:

    def __init__(self):
        pass


    def sinewave_ticks(self, frequency):
        ticks_array = np.linspace(0, 1 / frequency, 5)

        return ticks_array


    def degrees_ticks(self, interval = 30):

        phase_deg_ticks = np.arange(-180, 180 + interval, interval)

        return phase_deg_ticks


    def octaves_ticks(self):
        octave_ticks = []

        for i in range(0, 10, 1):
            octave_ticks.append(31.25 * (2 ** i))

        return octave_ticks


    def octaves_labels(self):

        octave_labels = []

        for i in range(0, 10, 1):
            if 31.25 * (2 ** i) < 1000:
                octave_labels.append(str(int(31.25 * (2 ** i))))
            else:
                octave_labels.append(str(int((31.25 / 1000) * (2 ** i))) + 'k')

        return octave_labels


    def zero_to_max_ticks(self, array, interval = 1):

        zero_to_max_ticks = np.arange(0, np.max(array) + interval, interval)

        return zero_to_max_ticks


    def discrete_ticks(self, samples_array, amount_of_ticks = 20):

        samples_array = to_list(samples_array)
        discrete_ticks = []

        if samples_array != []:
            if len(samples_array) % 2 != 0:
                del samples_array[-1] # Set samples_array to even lenght

            while len(samples_array) % amount_of_ticks != 0:
                amount_of_ticks = amount_of_ticks - 1 # Set amount_of_ticks to greatest common divisor

            discrete_ticks = [None] * amount_of_ticks
            K = int(len(samples_array) / amount_of_ticks)

            for i in range(1, amount_of_ticks + 1, 1):
                discrete_ticks[i - 1] = samples_array[K * i - 1]

        return discrete_ticks