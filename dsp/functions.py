import os
import numpy as np
import datetime


def info(variable_input):
    """
    Gives descriptive information about a given variable.

    Args:
        variable_input (Any type) Variable of which information is being asked for.

    Returns:
        None.
    """

    if type(variable_input) == int:
        print(f'{variable_input} is an integer.')

    elif type(variable_input) == float:
        print(f'{variable_input} is a float.')

    elif type(variable_input) == str:
        print(f'"{variable_input}" is a string.')

    elif type(variable_input) == list:
        print(f'The input is a list which contains {len(variable_input)} elements.')

    elif type(variable_input) == tuple:
        print(f'The input is a tuple of {len(variable_input)} components.')

    elif type(variable_input) == dict:
        print(f'The input is a dictionary of {len(variable_input)} elements:')
        print(variable_input.items())

    elif type(variable_input) == np.ndarray:
        N = str(variable_input.shape[0])

        if len(variable_input.shape) == 1:
            N = 'one dimention'
        else:
            for i in range(1, len(variable_input.shape), 1):
                N = N + 'x' + str(variable_input.shape[i])

        print(f'The input is a {N} array of {variable_input.size} elements.')

    else:
        print(f'There is no information available for {type(variable_input)}.')

    return


def pretty_frequency(frequency):
    if frequency < 1000:
        pretty_number = round_float(frequency, 2)
        pretty_frequency = str(pretty_number) + "Hz"

    elif frequency < 10000:
        pretty_number = round_float(frequency / 1000, 2)
        pretty_number = "{:.1f}".format(pretty_number)
        pretty_frequency = str(pretty_number) + "kHz"

    else:
        pretty_number = round_float(frequency / 1000, 3)
        pretty_frequency = str(pretty_number) + "kHz"

    pretty_frequency = pretty_frequency.replace(".0", "")

    return pretty_frequency


def get_root_dir(param = 0, open_root_dir = False):
    """
    Traces a folder relative to where the script is being executed. Defines this folder as "root directory" and returns it absolute path.

    Args:
        param (string or int) Name of the folder (str) to trace or level of hierarchy (int) to define as root directory.
        open_root_dir (bool, optional) Determines whether the root directory will be opened after being defined. The default is False.

    Returns:
        root_dir (string) Path of the folder defined as root directory.
    """

    if type(param) == int:
        root_dir = os.path.dirname(__file__)

        for i in range(1, param + 1, 1):
            root_dir = os.path.realpath(os.path.join(root_dir, '..'))

    elif type(param) == str:
        root_dir = ''

        for i in __file__:
            if param not in root_dir:
                root_dir = root_dir + i

    else:
        raise ValueError(f'{type(param)} is not a valid input.')

    if open_root_dir == True:
        os.startfile(root_dir)

    return root_dir


def save_plot(graph, **kwargs):
    """
    Saves a given matplotlib graph into a file at the hard drive.

    Args:
        (matplotlib figure) Graph that is going to be saved.
        **kwargs (unpacked dict) Optional parameters.
            file_dir (string) Path where the file is going to be saved. Default is relative directory.
            file_name (string) Name which the file is going to be saved with. Default is local time and computer username.
            bbox_inches (string) Default is 'tight'.
            dpi (int) Default is 300.
            transparent (bool) Default is False.

    Returns:
        None
    """

    save_kwargs = {
        'file_dir': os.path.dirname(__file__),
        'file_name': str(datetime.datetime.now()) + ' by ' + os.getlogin(),
    }

    for key, value in kwargs.items():
        if key in save_kwargs and value != save_kwargs[key]:
            save_kwargs[key] = value

    savefig_kwargs = {
        'bbox_inches': 'tight',
        'dpi': 300,
        'transparent': False
    }

    for key, value in kwargs.items():
        if key in savefig_kwargs and value != savefig_kwargs[key]:
            savefig_kwargs[key] = value

    graph.savefig(os.path.join(save_kwargs['file_dir'], save_kwargs['file_name'] + '.png'), **savefig_kwargs)

    return


def save_array(array, **kwargs):
    """
    Saves a given numpy array into a file at the hard drive.

    Args:
        array (numpy.ndarray) Data that is going to be saved.
        **kwargs (unpacked dict) Optional parameters.
            file_dir (string) Path where the file is going to be saved. Default is relative directory.
            file_name (string) Name which the file is going to be saved with. Default is local time and computer username.

    Returns:
        None
    """

    save_kwargs = {
        'file_dir': os.path.dirname(__file__),
        'file_name': str(datetime.datetime.now()) + ' by ' + os.getlogin()
    }

    for key, value in kwargs.items():
        if key in save_kwargs and value != save_kwargs[key]:
            save_kwargs[key] = value

    np.save(os.path.join(save_kwargs['file_dir'], save_kwargs['file_name']), array)

    return


def to_list(variable_input):
    """
    Attempts to convert a given variable into a list.

    Args:
        variable_input (any type)

    Returns:
        list_output (list)
    """

    if type(variable_input) == list:
        list_output = variable_input

    elif type(variable_input) == np.ndarray:
        list_output = variable_input.tolist()

    else:
        list_output = list(variable_input)

    return list_output


def matrix_to_list(list_input:list):
    """
    Transforms a matrix-like list into a regular one.

    Args:
        list_input (list) Input list to be converted.

    Returns:
        list_output (list) Output list converted.
    """

    list_output = []
    dim = np.array(list_input).shape

    if len(dim) > 1:
        for x in range(len(list_input)):
            for y in range(len(list_input)):
                list_output.append(list_input[x][y])

    else:
        list_output = list_input

    return list_output


def round_float(number_input, significant_digits = 3):
    """
    Attempts to round a given float to a certain number of significant figures. Contemplates that the decimal (. ,) and negative (-) symbols are not digits.

    Args:
        number_input (float) Input that is going to be rounded.
        significant_digits (int, optional) Significant figures or digits. The default is 3.

    Returns:
        (float) Rounded number.
    """

    if '-' not in str(number_input):
        int_digits = len(str(int(number_input)))
    else:
        int_digits = len(str(int(number_input))) - 1

    amount_of_characters = len(str(number_input))
    dec_digits = amount_of_characters - int_digits - 1
    number_input = number_input / 10 ** int_digits
    number_input = round(number_input, significant_digits)
    number_input = number_input * (10 ** int_digits)

    if str(number_input)[-2:] == '.0':
        rounded_float = int(number_input)

    if str(number_input)[1 - dec_digits:] == '9' * (dec_digits - 1):
        rounded_float = round(number_input, 1)

    rounded_float = number_input

    return rounded_float


def round_array(array_input, significant_digits = 3):
    """
    Rounds the floats of a given array to a certain number of significant figures. Contemplates that the decimal (. ,) and negative (-) symbols are not digits.

    Args:
        array_input (numpy.ndarray of floats) Input that is going to be rounded.
        significant_digits (int, optional) Significant figures or digits. The default is 3.

    Returns:
        (numpy.ndarray of floats) Array with rounded elements.
    """

    rounded_array = np.array([])

    for each_element in array_input:
        rounded_element = round_float(each_element)
        rounded_array = np.append(rounded_array, rounded_element)

    return rounded_array


def closest_to_average(numbers_list):
    """
    Returns the value from a given list which is closest to the average of all the values from it.

    Args:
        numbers_list (list, set, tuple or numpy.ndarray) Input variable of floats in which the value that aproximates to the average is going to be the output.

    Returns:
        (float) Float from the input which difference with the exact average is the smallest.
    """

    floats_list = to_list(numbers_list)
    average = sum(floats_list) / len(floats_list)
    closest = 0

    if average in floats_list:
        closest = average
    else:
        for i in floats_list:
            difference = abs(average - i)

            if difference < abs(average - closest):
                closest = i

    return closest


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


def plot_sinewaves_list(self, sinewaves_list, **plot_kwargs):
    """
    Plots a list of sine waveforms in an interval determined by the average period of all the signals.

    Args:
        sinewaves_list (list of tuples) Each tuple contains the x-y axes data in the first two components. The third component of each tuple have to be a string carring the legend of the respective signal, with the following format: 'sin_freq_Hz' being 'freq' the frequency of the sinewave. The legend of the sinewave with the average frequency must have the word 'ave', with the following format: 'sin_freq_Hz_ave'.
        **plot_kwargs (unpacked dict) Arguments for the matplotlib.plot() function.

    Returns:
        (matplotlib figure) Graph.
    """

    plt.grid()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")

    legends_list = []

    for i in range(0, len(sinewaves_list), 1):
        x = sinewaves_list[i][0]
        y = sinewaves_list[i][1]
        plt.plot(x,y, **plot_kwargs)
        legends_list.append(sinewaves_list[i][2])

        if 'ave' in sinewaves_list[i][2]: # Hardcoded 'ave' is the keyword that distincts the average frequency from the others
            cut = len(sinewaves_list[i][2]) - 7 # Hardcoded 7 is the amount of characters from the end until the word 'freq'
            ave_freq = float(sinewaves_list[i][2][4:cut]) # Hardcoded 4 is the amount of characters from the beginin until the word 'freq'

    plt.xticks(np.linspace(0, 1 / ave_freq, 5))
    plt.legend(legends_list, loc = "upper right")
    graph = plt.gcf()

    return graph


def plot_multiple_overlaids(x_data, y_data_list, y_legends_list, is_discrete = False, **kwargs):
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


def plot_dual_axis(x, y, **kwargs):
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