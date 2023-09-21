import matplotlib.pyplot as plt
from dsp.signal import Signal
from dsp.functions import to_list, generate_sinewave_ticks, generate_phase_deg_ticks


class Grapher:

    def __init__(self, discrete_kwargs = None):
        if discrete_kwargs is None:
            discrete_kwargs = {'alpha': 1, 'color': 'black', 'linestyle': '', 'linewidth': 1, 'marker': 'o'}

        self._discrete_kwargs = discrete_kwargs
        self._signal = Signal()

    @property
    def discrete_kwargs(self):
        return self._discrete_kwargs

    @discrete_kwargs.setter
    def discrete_kwargs(self, discrete_kwargs):
        self._discrete_kwargs = discrete_kwargs

    @property
    def signal(self):
        return self._signal

    @signal.setter
    def signal(self, signal):
        self._signal = signal


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

        ax1.set_xticks(generate_sinewave_ticks(signal.fundamental_frequency))
        ax2.set_xticks(self.generate_octaves()[0])
        ax3.set_xticks(self.generate_octaves()[0])
        ax3.set_yticks(generate_phase_deg_ticks(90))

        ax2.set_xticklabels(self.generate_octaves()[1])
        ax3.set_xticklabels(self.generate_octaves()[1])

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


    def generate_ticks(self, samples_array, amount_of_ticks = 20):
        """
        Generates a list of N ticks that are simetrically distributed along samples_array and can be used in matplotlib.pyplot.setp() method.

        Args:
        samples_array (list) Array like data from where the ticks will be extracted.
        amount_of_ticks (int, optional) Amount of ticks which are going to be extracted from the input data. Default is 20.

        Returns:
            (list) List of generated ticks.
        """

        samples_array = to_list(samples_array)
        ticks = []

        if samples_array != []:
            if len(samples_array) % 2 != 0:
                del samples_array[-1] # Set samples_array to even lenght

            while len(samples_array) % amount_of_ticks != 0:
                amount_of_ticks = amount_of_ticks - 1 # Set amount_of_ticks to greatest common divisor

            ticks = [None] * amount_of_ticks
            K = int(len(samples_array) / amount_of_ticks)

            for i in range(1, amount_of_ticks + 1, 1):
                ticks[i - 1] = samples_array[K * i - 1]

        return ticks


    def generate_octaves(self):
        """
        Generates lists of ticks and tick labels that can both be used in matplotlib.pyplot.setp() method. The ticks are set to octaves, and defined according to UNE-EN 61260.

        Returns:
        ticks_list (list)
        tick_labels (list)
        """

        ticks_list = []
        tick_labels = []

        for i in range(0, 10, 1):
            ticks_list.append(31.25 * (2 ** i))

            if 31.25 * (2 ** i) < 1000:
                tick_labels.append(str(int(31.25 * (2 ** i))))
            else:
                tick_labels.append(str(int((31.25 / 1000) * (2 ** i))) + 'k')

        return ticks_list, tick_labels