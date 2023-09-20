import numpy as np
from functions import closest_to_average

class Generator:
    """
    Provides methods for generating signals using Numpy library.
    """


    def __init__(self):
        """
        Constructs an Aliasing object with default settings.
        """
        pass


    def samples_array(self, starting_sample = -10, ending_sample = 10, is_closed_interval = True):
        """
        Generates an array of samples to use as the domain of a discrete signal.

        Args:
            starting_sample (int, optional) Starting sample. The default is -10.
            ending_sample (int, optional) Ending sample. The default is 10.
            is_closed_interval (bool, optional) Determines whether the bound of the samples interval belongs to it or not. The default is True.

        Returns:
            (numpy.ndarray) Array with the samples.
        """

        if ending_sample <= starting_sample:
            raise ValueError('The parameter starting_sample must be less than ending_sample by definition.')

        samples_array = np.arange(starting_sample, ending_sample + int(is_closed_interval), 1)

        return samples_array


    def arange_time_array(self, wave_frequency = 200, sampling_rate = 320000, is_closed_interval = True):
        """
        Generates an array of time samples that represent one period of a given wave.

        Args:
            wave_frequency (int, optional) The frequency of the waveform in hertz (default is 1k Hz).
            sampling_rate (int, optional) The sampling rate in samples per second (default is 44100 samples per second).
            is_closed_interval (bool, optional) Determines whether the bound of the samples interval belongs to it or not. The default is True.

        Returns:
            time_array (numpy.ndarray) An array containing sampling time values.
        """

        wave_period = 1 / wave_frequency
        step = 1 / sampling_rate
        last_sample = int(is_closed_interval) * step
        time_array = np.arange(0, wave_period + last_sample, step)

        return time_array


    def linspace_time_array(self, wave_frequency = 200, sampling_rate = 320000, is_closed_interval = True):
        """
        Generates an array of time samples that represent one period of a given wave.

        Args:
            wave_frequency (int, optional) The frequency of the waveform in hertz (default is 1k Hz).
            sampling_rate (int, optional) The sampling rate in samples per second (default is 44100 samples per second).
            is_closed_interval (bool, optional) Determines whether the bound of the samples interval belongs to it or not. The default is True.

        Returns:
            time_array (numpy.ndarray) An array containing sampling time values.
        """

        wave_period = 1 / wave_frequency
        time_array = np.linspace(0, wave_period, int(sampling_rate / wave_frequency), endpoint = is_closed_interval)

        return time_array


    def unit_impulse(self, samples_array, starting_sample = -10, ending_sample = 10, impulse_sample = 10):
        """
        Generates a discrete unit impulse.

        Args:
            samples_array (numpy.ndarray) Array with domain samples.
            starting_sample (int, optional) Starting sample. The default is -10.
            ending_sample (int, optional) Ending sample. The default is 10.
            impulse_sample (int, optional) Sample at which the unit impulse is. The default is 10.

        Returns:
            (numpy.ndarray) Array with an unit impulse.
        """

        if impulse_sample > len(samples_array):
            raise ValueError('The parameter impulse_sample does not belong to the interval [starting_sample,ending_sample].')

        signal = np.zeros(len(samples_array))
        signal[impulse_sample] = 1

        return signal


    def unit_step(self, samples_array, starting_sample = -10, ending_sample = 10, step_sample = 10):
        """
        Generates a discrete unit step.

        Args:
            samples_array (numpy.ndarray) Array with domain samples.
            starting_sample (int, optional) Starting sample. The default is -10.
            ending_sample (int, optional) Ending sample. The default is 10.
            step_sample (int, optional) Sample at which the unit step begins. The default is 10.

        Returns:
            (numpy.ndarray) Array with an unit step.
        """

        if len(samples_array) < step_sample:
            raise ValueError('The parameter step_sample does not belong to the interval [starting_sample,ending_sample].')

        signal = np.concatenate((np.zeros(step_sample), np.ones(len(samples_array) - step_sample)), axis = 0)

        return signal


    def square_pulse(self, samples_array, turn_on = 5, turn_off = 15):
        """
        Generates a discrete square pulse.

        Args:
            samples_array (numpy.ndarray) Array with domain samples.
            turn_on (int, optional) Sample at which the square pulse goes from 0 to 1. The default is 5.
            turn_off (int, optional) Sample at which the square pulse goes from 1 to 0. The default is 15.

        Returns:
            (numpy.ndarray) Array with a square pulse.
        """

        duty_cycle = (turn_off - turn_on) * 100 / len(samples_array)

        if 100 < duty_cycle:
            raise ValueError('Duty Cycle can not be greater than 100%.')

        signal = np.concatenate((np.zeros(turn_on), np.ones(turn_off - turn_on), np.zeros(len(samples_array) - turn_off)), axis = 0)

        return signal


    def triangular_pulse(self, samples_array, starting_sample = -10, ending_sample = 10, half_base = 5):
        """
        Generates a discrete triangular pulse.

        Args:
            samples_array (numpy.ndarray) Array with domain samples.
            starting_sample (int, optional) Starting sample. The default is -10.
            ending_sample (int, optional) Ending sample. The default is 10.
            half_base (int, optional) Half of the triangPulse base lenght. The default is 5.

        Returns:
            (numpy.ndarray) Array with a triangular pulse.
        """

        if half_base <= 0 or half_base > len(samples_array) / 2:
            raise ValueError('The parameter half_base must be greater than 0 and less than (ending_sample - starting_sample) / 2.')

        signal = np.zeros(len(samples_array))

        for i in range(- half_base, half_base, 1):
            sample_i = int((ending_sample - starting_sample) / 2 + i)
            signal[sample_i] = 1 - abs(i * (1 / half_base))

        return signal


    def random_signal(self, samples_array, mu_expectation = 0, sigma_deviation = 1):
        """
        Generates a random discrete signal.

        Args:
            samples_array (numpy.ndarray) Array with domain samples.
            mu_expectation (int, optional) Mean or expected value. The default is 0.
            sigma_deviation (float, optional) Standard deviation. The default is 1.

        Returns:
            (numpy.ndarray) Array with a random signal.
        """

        signal = np.random.normal(mu_expectation, sigma_deviation, len(samples_array))

        return signal

    def sinewave(self, time_array, wave_frequency, phase_deg = 0, wave_amplitude = 1):
        """
        Generates a sinewave.

        Args:
            time_array (numpy.ndarray) Array of time values.
            wave_frequency (float) Frequency of the sine wave (Hz).
            phase_deg (float, optional) Phase angle in degrees. Default is 0 degrees.
            wave_amplitude (float, optional) Amplitude of the sine wave. Default is 1.

        Returns:
            (numpy.ndarray) Array containing the generated sine wave.
        """
 
        omega = 2 * np.pi * wave_frequency
        phase_rad = phase_deg * (np.pi / 180)
        sine_array = wave_amplitude * np.sin(omega * time_array + phase_rad)

        return sine_array


    def sinewaves_list(self, *frequencies, sampling_rate = 320000, is_closed_interval = True):
        """
        Generates a list of sine waves with different frequencies.

        Args:
            *frequencies (float) Frequencies (in Hertz) of the sine waves.
            sampling_rate (int, optional) The sampling rate in samples per second (default is 320000 samples per second).
            is_closed_interval (bool, optional) Determines whether the bound of the samples interval belongs to it or not. The default is True.

        Returns:
            sinewaves_list (list) A list of tuples, where each tuple contains the time values, the corresponding sine wave signal, and a legend.
        """

        ave_frequency = closest_to_average(frequencies)
        time_array = self.arange_time_array(ave_frequency, sampling_rate, is_closed_interval)
        sinewaves_list = []

        for i in range(0, len(frequencies), 1):
            sinewave_i = self.sinewave(time_array, frequencies[i])

            if frequencies[i] == ave_frequency:
                legend_i = f'sin_{frequencies[i]}_Hz_ave'
            else:
                legend_i = f'sin_{frequencies[i]}_Hz'

            signal_i = (time_array , sinewave_i , legend_i)
            sinewaves_list.append(signal_i)

        return sinewaves_list