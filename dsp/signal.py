import numpy as np


class Signal:

    def __init__(self):
        self._fundamental_frequency = -1
        self._fundamental_amplitude = -1
        self._fundamental_phase = -1
        self._time_array = np.array([])
        self._amplitude_array = np.array([])
        self._frequency_array = np.array([])
        self._X_magnitude_array = np.array([])
        self._X_phase_array = np.array([])
        self._description = "N/A"


#######################
## GETTERS & SETTERS ##
#######################


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
    def amplitude_array(self):
        return self._amplitude_array

    @amplitude_array.setter
    def amplitude_array(self, amplitude_array):
        self._amplitude_array = amplitude_array

    @property
    def frequency_array(self):
        return self._frequency_array

    @frequency_array.setter
    def frequency_array(self, frequency_array):
        self._frequency_array = frequency_array

    @property
    def X_magnitude_array(self):
        return self._X_magnitude_array

    @X_magnitude_array.setter
    def X_magnitude_array(self, X_magnitude_array):
        self._X_magnitude_array = X_magnitude_array

    @property
    def X_phase_array(self):
        return self._X_phase_array

    @X_phase_array.setter
    def X_phase_array(self, X_phase_array):
        self._X_phase_array = X_phase_array

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description


#############
## METHODS ##
#############


    def copy_from(self, origin):
        self.fundamental_frequency = origin.fundamental_frequency
        self.fundamental_amplitude = origin.fundamental_amplitude
        self.fundamental_phase = origin.fundamental_phase
        self.time_array = origin.time_array                             # Used for waveform: t
        self.amplitude_array = origin.amplitude_array                   # Used for waveform: x(t)
        self.frequency_array = origin.frequency_array                   # Used for spectrum: f
        self.X_magnitude_array = origin.X_magnitude_array               # Used for spectrum: X(f)
        self.X_phase_array = origin.X_phase_array                       # Used for spectrum: Q(f)
        self.description = origin.description

        return


    def load_spectrum(self, path):
        """
        Loads a signal from a NumPy binary file.

        Args:
            path (string) The file path to the NumPy binary file containing the signal data. The path should include the file name with the .npy extension.

        Returns:
            None.
        """

        signal = np.load(path)

        self.frequency_array = signal[0,:]
        self.X_magnitude_array = signal[1,:]
        self.X_phase_array = signal[2,:]

        return


    def extend(self, new_duration):
        """
        Increase the signal's domain by extending the time array and generating a new amplitude_array.

        Args:
            new_duration (float): The desired duration in seconds for the new time domain.

        Returns:
            None.
        """

        if new_duration != 1 / self.fundamental_frequency:
            samples_before = len(self.time_array)
            samples_after = int(new_duration * len(self.time_array) / self.time_array[-1])
            samples_increment = samples_after - samples_before

            for i in range(0, samples_increment, 1):
                steps_lenght = self.time_array[1]
                time_increment = self.time_array[-1] + steps_lenght
                self.time_array = np.append(self.time_array, time_increment)
                self.amplitude_array = np.append(self.amplitude_array, self.amplitude_array[i+1])

        return