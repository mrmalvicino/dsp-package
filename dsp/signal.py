import numpy as np


class Signal:

    def __init__(self):
        self._fundamental_frequency = -1
        self._fundamental_amplitude = -1
        self._fundamental_phase = -1
        self._time_array = np.array([])
        self._frequency_array = np.array([])
        self._x_amplitude_array = np.array([])
        self._X_amplitude_array = np.array([])
        self._phase_array = np.array([])
        self._description = "N/A"

    @property
    def fundamental_frequency(self):
        return self._fundamental_frequency

    @fundamental_frequency.setter
    def fundamental_frequency(self, fundamental_frequency):
        self._fundamental_frequency = fundamental_frequency

    @property
    def fundamental_amplitude(self):
        return self._fundamental_amplitude

    @fundamental_amplitude.setter
    def fundamental_amplitude(self, fundamental_amplitude):
        self._fundamental_amplitude = fundamental_amplitude

    @property
    def fundamental_phase(self):
        return self._fundamental_phase

    @fundamental_phase.setter
    def fundamental_phase(self, fundamental_phase):
        self._fundamental_phase = fundamental_phase

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
    def x_amplitude_array(self):
        return self._x_amplitude_array

    @x_amplitude_array.setter
    def x_amplitude_array(self, x_amplitude_array):
        self._x_amplitude_array = x_amplitude_array

    @property
    def X_amplitude_array(self):
        return self._X_amplitude_array

    @X_amplitude_array.setter
    def X_amplitude_array(self, X_amplitude_array):
        self._X_amplitude_array = X_amplitude_array

    @property
    def phase_array(self):
        return self._phase_array

    @phase_array.setter
    def phase_array(self, phase_array):
        self._phase_array = phase_array

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description