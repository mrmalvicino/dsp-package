import matplotlib.pyplot as plt
from dsp.signal import Signal
from dsp.ticks import Ticks
from dsp.functions import closest_to_average


class Grapher:

    def __init__(self, continuous_kwargs = None, discrete_kwargs = None):
        self._signal = Signal()
        self._ticks = Ticks()

        if continuous_kwargs is None:
            continuous_kwargs = {'color': 'black', 'linewidth': 2}

        self._continuous_kwargs = continuous_kwargs

        if discrete_kwargs is None:
            discrete_kwargs = {'alpha': 1, 'color': 'black', 'linestyle': '', 'linewidth': 1, 'marker': 'o'}

        self._discrete_kwargs = discrete_kwargs

    @property
    def signal(self):
        return self._signal

    @signal.setter
    def signal(self, signal):
        self._signal = signal

    @property
    def ticks(self):
        return self._ticks

    @ticks.setter
    def ticks(self, ticks):
        self._ticks = ticks

    @property
    def continuous_kwargs(self):
        return self._continuous_kwargs

    @continuous_kwargs.setter
    def continuous_kwargs(self, continuous_kwargs):
        self._continuous_kwargs = continuous_kwargs

    @property
    def discrete_kwargs(self):
        return self._discrete_kwargs

    @discrete_kwargs.setter
    def discrete_kwargs(self, discrete_kwargs):
        self._discrete_kwargs = discrete_kwargs


    def plot_signal(self, signal):
        fig, (ax1, ax2, ax3) = plt.subplots(nrows = 3, ncols = 1, figsize = (6, 6))

        ax1.plot(signal.time_array, signal.amplitude_array, ** self.continuous_kwargs)
        ax2.plot(signal.frequency_array, signal.X_magnitude_array, ** self.discrete_kwargs)
        ax3.plot(signal.frequency_array, signal.X_phase_array, ** self.discrete_kwargs)

        ax1.set_title('Waveform')
        ax2.set_title('Spectrum Amplitude')
        ax3.set_title('Spectrum Phase')

        ax1.set_xlabel('Time [s]')
        ax2.set_xlabel('Frequency [Hz]')
        ax3.set_xlabel('Frequency [Hz]')

        ax1.set_ylabel('x(t) Amplitude')
        ax2.set_ylabel('X(f) Amplitude')
        ax3.set_ylabel('Phase [deg]')

        ax1.set_xscale('linear')
        ax2.set_xscale('log')
        ax3.set_xscale('log')

        ax1.grid(True)
        ax2.grid(True)
        ax3.grid(True)

        ax1.set_xticks(self.ticks.sinewave_ticks(signal.fundamental_frequency))
        ax2.set_xticks(self.ticks.octaves_ticks())
        ax3.set_xticks(self.ticks.octaves_ticks())

        ax2.set_yticks(self.ticks.zero_to_max_ticks(signal.X_magnitude_array))
        ax3.set_yticks(self.ticks.degrees_ticks(90))

        ax2.set_xticklabels(self.ticks.octaves_labels())
        ax3.set_xticklabels(self.ticks.octaves_labels())

        ax1.legend([signal.description])
        ax2.legend([signal.description])
        ax3.legend([signal.description])

        plt.tight_layout()
        graph = plt.gcf()

        return graph

    def plot_waveforms(self, * signals):
        legends_list = []
        frequencies_list = []

        plt.figure(figsize = (6,2))
        plt.grid()

        for i in range(0, len(signals), 1):
            x_data = signals[i].time_array
            y_data = signals[i].amplitude_array
            plt.plot(x_data, y_data, ** self.continuous_kwargs)
            legends_list.append(signals[i].description)
            frequencies_list.append(signals[i].fundamental_frequency)

        min_freq = min(frequencies_list)
        plt.xticks(self.ticks.sinewave_ticks(min_freq))
        plt.legend(legends_list, loc = "upper right")
        graph = plt.gcf()

        return graph