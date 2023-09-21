import numpy as np


class Signal:
    """
    Represents a signal.
    """

    def __init__(self, description = 'sin1kHz', waveform = "sinewave", fundamental_frequency = 1000, time_array = None, frequency_array = None, amplitude_array = None, phase_array = None):
        """
        Constructs a Signal object.
        """

        self._description = description
        self._waveform = waveform
        self._fundamental_frequency = fundamental_frequency
        self._time_array = time_array
        self._frequency_array = frequency_array
        self._amplitude_array = amplitude_array
        self._phase_array = phase_array

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def waveform(self):
        return self._waveform

    @waveform.setter
    def waveform(self, waveform):
        self._waveform = waveform

    @property
    def fundamental_frequency(self):
        return self._fundamental_frequency

    @fundamental_frequency.setter
    def fundamental_frequency(self, fundamental_frequency):
        self._fundamental_frequency = fundamental_frequency

    @property
    def time_array(self):
        return self._time_array

    @time_array.setter
    def time_array(self, time_array):
        self._time_array = time_array

    @property
    def frequency_array(self):
        return self._frequency_array

    @frequency_array.setter
    def frequency_array(self, frequency_array):
        self._frequency_array = frequency_array

    @property
    def amplitude_array(self):
        return self._amplitude_array

    @amplitude_array.setter
    def amplitude_array(self, amplitude_array):
        self._amplitude_array = amplitude_array

    @property
    def phase_array(self):
        return self._phase_array

    @phase_array.setter
    def phase_array(self, phase_array):
        self._phase_array = phase_array