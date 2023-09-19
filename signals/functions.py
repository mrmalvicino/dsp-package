import os
import numpy as np
import datetime


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

    dec_digits = len(str(number_input)) - int_digits - 1
    number_input = number_input / 10 ** int_digits
    number_input = round(number_input, significant_digits)
    number_input = number_input * (10 ** int_digits)

    if str(number_input)[-2:] == '.0':
        rounded_float = int(number_input)

    if str(number_input)[1 - dec_digits:] == '9' * (dec_digits - 1):
        rounded_float = round(number_input, 1)

    rounded_float = number_input

    return rounded_float


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