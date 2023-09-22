import matplotlib.pyplot as plt
from dsp.signal import Signal
from dsp.ticks import Ticks
from dsp.functions import to_list


class Grapher:

    def __init__(self, discrete_kwargs = None):
        self._signal = Signal()
        self._ticks = Ticks()

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
    def discrete_kwargs(self):
        return self._discrete_kwargs

    @discrete_kwargs.setter
    def discrete_kwargs(self, discrete_kwargs):
        self._discrete_kwargs = discrete_kwargs


    def plot_signal(self, signal):
        fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(6, 6))

        ax1.plot(signal.time_array, signal.x_amplitude_array)
        ax2.plot(signal.frequency_array, signal.X_amplitude_array, ** self.discrete_kwargs)
        ax3.plot(signal.frequency_array, signal.phase_array, ** self.discrete_kwargs)

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
        ax3.set_yticks(self.ticks.degrees_ticks(90))

        ax2.set_xticklabels(self.ticks.octaves_labels())
        ax3.set_xticklabels(self.ticks.octaves_labels())

        ax1.legend([signal.description])
        ax2.legend([signal.description])
        ax3.legend([signal.description])

        plt.tight_layout()
        graph = plt.gcf()

        return graph


    def plot_multiple_overlaids(self, x_data, y_data_list, y_legends_list, is_discrete = False, **kwargs):
        """
        Generates a single graph of multiple signals one over each other.

        Args:
            x_data (numpy.ndarray) Horizontal axis data.
            y_data_list (list of numpy arrays) Data of each signal per component.
            y_legends_list (list of strings) Legend of each signal per component.
            is_discrete (bool, optional) Determines plotting styles depending on the horizontal domain. Default is False.
            **kwargs (unpacked dict) Arguments for the matplotlib.plot() function.

        Returns:
            (matplotlib figure) Graph.
        """

        if len(y_data_list) != len(y_legends_list):
            raise ValueError('There are not as many signals as legends.')

        plt.figure(figsize=(10,5))
        plt.grid()

        if is_discrete == True:
            plt.xlabel("Samples [n]")
            kwargs = self._discrete_kwargs
            plt.xticks(self.generate_ticks(x_data, 21))
        else:
            plt.xlabel("Time [s]")

        plt.ylabel("Amplitude")

        for i in range(0, len(y_data_list), 1):
            y_data = y_data_list[i]
            plt.plot(x_data, y_data, **kwargs)

        plt.legend(y_legends_list, loc = "upper right")
        graph = plt.gcf()

        return graph


    def plot_dual_axis(self, x, y, **kwargs):
        """
        Generates a plot using matplotlib.

        Args:
            x (numpy.ndarray) Data for the horizontal axis.
            y (tuple of numpy.ndarray) Data for the vertical axes. A two dimentions tuple is expected, containing the data for the left and right vertical axes in each component respectively.
            **kwargs (unpacked dict) Object orientated kwargs values for matplotlib.pyplot.plot() and matplotlib.pyplot.setp() methods. Bidimentional tuples are expected for the keys that involves the vertical axes. For example, the scale could be determined by defining the dictionary kwargs = {'xscale': 'linear', 'yscale': ('logit','log')} and using it into plot_dual_axis(x, y, **kwargs).

        Returns:
            (matplotlib figure) Graph.
        """

        # Store the **kwargs in a new dictionary:
        user_inputs = kwargs

        # Define possible **kwargs:
        kwargs = {
            'figsize': (10,5),
            'title': 'Plot',
            'xlabel': '',
            'ylabel': ('',''),
            'xscale': 'linear',
            'yscale': ('linear','linear'),
            'legend': ('',''),
            'xticks': 'default',
            'yticks': ('default','default'),
            'xticklabels': 'default',
            'yticklabels': ('default','default'),
            'xlim': 'default',
            'ylim': ('default','default')
        }

        # Overwrite the possible **kwargs with the actual inputs:
        for key, value in user_inputs.items():
            if key in kwargs:
                kwargs[key] = value
        
        # Split the plt.setp kwargs into 2 dictionaries:
        setpL = dict()
        setpR = dict()

        setpL_keys = ['yticks', 'yticklabels', 'ylim', 'xticks', 'xticklabels', 'xlim']
        setpR_keys = ['yticks', 'yticklabels', 'ylim']

        for key in setpL_keys:
            if len(kwargs[key]) == 2:
                if kwargs[key][0] != 'default':
                    setpL.update({key: kwargs[key][0]})
            else:
                if kwargs[key] != 'default':
                    setpL.update({key: kwargs[key]})

        for key in setpR_keys:
            if len(kwargs[key]) == 2:
                if kwargs[key][1] != 'default':
                    setpR.update({key: kwargs[key][1]})

        # Generate plot:
        fig, (axisL) = plt.subplots(1,1, figsize=kwargs['figsize'])
        axisR = axisL.twinx()
        
        axisL.plot(x, y[0], color='blue')
        axisR.plot(x, y[1], color='red', linestyle='--')
        
        axisL.set_xlabel(kwargs['xlabel'])
        axisL.set_ylabel(kwargs['ylabel'][0])
        axisR.set_ylabel(kwargs['ylabel'][1])
        
        axisL.set_xscale(kwargs['xscale'])
        axisL.set_yscale(kwargs['yscale'][0])
        axisR.set_yscale(kwargs['yscale'][1])
        
        axisL.set_title(kwargs['title'])
        axisL.legend([kwargs['legend'][0]], loc='lower left')
        axisR.legend([kwargs['legend'][1]], loc='lower right')

        plt.setp(axisL, **setpL)
        plt.setp(axisR, **setpR)
        
        axisL.grid()
        plt.tight_layout()
        graph = plt.gcf()

        return graph