import numpy as np
from functions import closest_to_average

class Generator:
    """
    Provides methods for generating signals.
    """


    def __init__(self):
        """
        Constructs an Aliasing object with default settings.
        """
        pass


    def generate_samples_array(starting_sample = -10, ending_sample = 10, is_closed_interval = True):
        """
        Generates array of samples to use as the domain of a discrete signal.
        """

        if not starting_sample < ending_sample:
            raise ValueError('The parameter starting_sample must be less than ending_sample by definition.')

        samples_array = np.arange(starting_sample, ending_sample + int(is_closed_interval), 1)

        return samples_array


    def generate_unit_impulse(samples_array, starting_sample = -10, ending_sample = 10, center_sample = 10):
        """
        Generates unit impulse.
        """

        if center_sample > len(samples_array):
            raise ValueError('The parameter center_sample does not belong to the interval [starting_sample,ending_sample].')

        x = np.zeros(len(n))
        x[center_sample] = 1

        return


    def generate_unit_step(samples_array):
        """
        Generates a unit step.
        """

        if center_sample > len(samples_array):
            raise ValueError('The parameter center_sample does not belong to the interval [starting_sample,ending_sample].')

        x = np.concatenate((np.zeros(center_sample), np.ones(len(samples_array) - center_sample)), axis = 0)

        return


    def generate_square_pulse(samples_array):
        """
        Generates a square pulse.
        """

        duty_cycle = (turn_off - turn_on) * 100 / len(samples_array)

        if duty_cycle > 100:
            raise ValueError('Duty Cycle can not be greater than 100%.')

        x = np.concatenate((np.zeros(turn_on), np.ones(turn_off - turn_on), np.zeros(len(samples_array) - turn_off)), axis = 0)

        return


    def generate_triangular_pulse(samples_array):
        """
        Generates a triangular pulse.
        """

        if half_base <= 0 or half_base > len(samples_array) / 2:
            raise ValueError('The parameter half_base must be greater than 0 and less than (ending_sample - starting_sample) / 2.')

        x = np.zeros(len(n))

        for i in range(- half_base, half_base, 1):
            n_i = int((ending_sample - starting_sample) / 2 + i)
            x[n_i] = 1 - abs(i * (1 / half_base))

        return


    def generate_random_signal():
        """
        Generates a random signal.
        """

        x = np.random.normal(mu_expectation, sigma_variance, len(n))

        return


    def gen_discrete_signals(signal_name, starting_sample = -10, ending_sample = 10, center_sample = 10, turn_on = 5, turn_off = 15, half_base = 5, mu = 0, sigma = 1, is_closed_interval = True, **kwargs):
        """
        Generates a custom discrete signal and optionally saves the plot and arrays involved.

        Args:
            signal_name : STR
                Name of the signal which is going to be generated. E.g., unitImpulse, unitStep, sqPulse, triangPulse, rnd.
            
            starting_sample : INT, optional
                Starting sample. The default is -10.
            
            ending_sample : INT, optional
                Ending sample. The default is 10.
            
            center_sample : INT, optional
                Sample at which the unitImpulse is and at which the unitStep begins. The default is 10.
            
            turn_on : INT, optional
                Sample at which the sqPulse goes from 0 to 1. The default is 5.
            
            turn_off : INT, optional
                Sample at which the sqPulse goes from 1 to 0. The default is 15.
            
            half_base : INT, optional
                Half of the triangPulse base lenght. The default is 5.
            
            mu : INT, optional
                Mean or expected value. The default is 0.
            
            sigma : FLOAT, optional
                Standard deviation. The default is 1.
            
            is_closed_interval : BOOL, optional
                Determines whether the bound of the samples interval belongs to it or not. The default is True.
        
        **kwargs : UNPACKED DICT
            Optional saving parameters.
        
            save_plot : BOOL
                Determines whether the plot is saved to a .png file.
                
            save_array : BOOL
                Determines whether the sample and amplitude arrays are saved to .npy files.

        Raises:
            ValueError
                The parameter starting_sample must be less than ending_sample by definition.
            
            ValueError
                The parameter center_sample does not belong to the interval [starting_sample,ending_sample].
            
            ValueError
                Duty Cycle can not be greater than 100%.
            
            ValueError
                The parameter m must be greater than 0 and less than (ending_sample-starting_sample)/2.
            
            ValueError
                Invalid input.

        Returns:
            None.
        """
        
        # Defines samples interval



        # Defines signal waveform
        
        if signal_name == 'unitImpulse':
            
        elif signal_name == 'unitStep':
            
        elif signal_name == 'sqPulse':
            
        elif signal_name == 'triangPulse':
            
        elif signal_name == 'rnd':
            
        else:
            raise ValueError('Invalid input.')
        
        # Plot
        
        plot_kwargs = {'alpha': 1, 'color': 'black', 'linestyle': '', 'linewidth': 1, 'marker': 'o'}
        
        plt.figure(figsize=(8,4))
        plt.plot(n,x, **plot_kwargs)
        plt.grid()
        plt.xlabel("Samples")
        plt.ylabel("Amplitude")
        
        if len(n) < 21:
            plt.xticks(n)
        else:
            plt.xticks(matplt.gen_ticks(n, N=21))
        
        graph = plt.gcf()
        
        
        # Kwargs
        
        for key, value in kwargs.items():
            
            if key == 'save_plot' and value == True:
                save(graph, file_dir=os.path.join(root_dir, 'images'), file_name=signal_name+'Plot')
            
            if key == 'save_array' and value == True:
                save(n, file_dir=os.path.join(root_dir, 'files'), file_name=signal_name+'Array_n')
                save(x, file_dir=os.path.join(root_dir, 'files'), file_name=signal_name+'Array_x')
        
        return


    def gen_sin_list(*frequencies, A=1, f_s = 44100, is_closed_interval = True):
        """
        Generates a sine wave for each input frequency.

        Parameters
        ----------
        
        *frequencies : UNPACKED TUPLE OF FLOATS
            Unpacked tuple containing the frequency values of the sine waves which are going to be generated.
        
        A : FLOAT, optional
            Amplitude of all the sine waves which are going to be generated. The default is 1.
        
        f_s : FLOAT, optional
            Sampling frequency rate. The default is 44100.
            
        is_closed_interval : BOOL, optional
            Determines whether the bound of the samples interval belongs to it or not. The default is True.

        Returns
        -------
        
        output : LIST OF TUPLES
            For each sine wave generated, the function returns a list of one tuple for every signal.
            Each tuple has three components that contains the time vector, the amplitude vector and a label respectively.
            Thus, the output for n signals generated would be:
            [ (time_1, amplitude_1, label_1) , (time_2, amplitude_2, label_2) , ... , (time_n, amplitude_n, label_n) ]
            Where time_i and amplitude_i are numpy arrays which holds the signal data and label_i is a string with descriptive porposes, being i a natural number between 1 and n.
            The average frequency is specified between brackets in its' label.

        """
        
        t = np.arange(0, 1/closest_to_average(frequencies) + int(is_closed_interval)/f_s , 1/f_s)
        
        output = []
        
        for i in range(0, len(frequencies), 1):
            omega_i = 2*np.pi*frequencies[i]
            y_i = A*np.sin(omega_i*t)
            if frequencies[i] == closest_to_average(frequencies):
                label = f'sin_{i+1}_freq_{frequencies[i]}Hz(ave)'
            else:
                label= f'sin_{i+1}_freq_{frequencies[i]}Hz'
            signal_i = (t , y_i , label)
            output.append(signal_i)
        
        return output

    def generate_time_array(wave_frequency = 1000, amount_of_periods = 1, sampling_rate = 44100):
        """
        Generates a time array with sampling time values to use as the domain of a signal.

        Args:
            wave_frequency (int) The frequency of the waveform in hertz (default is 1k Hz).
            amount_of_periods (int) The number of periods to generate (default is 1).
            sampling_rate (int) The sampling rate in samples per second (default is 44100 samples per second).

        Returns:
            time_array (numpy array) An array containing sampling time values.
        """

        wave_period = 1 / wave_frequency
        interval_lenght = amount_of_periods * wave_period
        step = 1 / sampling_rate
        time_array = np.arange(0, interval_lenght, step)

        return time_array

    def generate_sinewave(time_array, wave_frequency, phase_deg = 0, wave_amplitude = 1):
        omega = 2 * np.pi * wave_frequency
        phase_rad = phase_deg * (np.pi / 180)
        sine_array = wave_amplitude * np.sin(omega * time_array + phase_rad)

        return sine_array