import numpy as np


class Signal:
    """
    Represents a signal.
    """

    def __init__(self, description = '', period = 0, time_array = None, frequency_array = None, amplitude_array = None, phase_array = None):
        """
        Constructs a Signal object with default settings.
        """

        self._description = description
        self._period = period
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
    def period(self):
        return self._period

    @period.setter
    def period(self, period):
        self._period = period

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