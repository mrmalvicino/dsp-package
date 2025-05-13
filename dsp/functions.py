import numpy as np
import math


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


def get_lower_frequency(self, *signals):
    fundamental_frequency = signals[0].fundamental_frequency

    for i in range(1, len(signals), 1):
        if signals[i].fundamental_frequency < fundamental_frequency:
            fundamental_frequency = signals[i].fundamental_frequency

    return fundamental_frequency


def extend_to_min(*signals):
    max_period = 1 / get_lower_frequency(*signals)

    for i in range(0, len(signals), 1):
        signals[i].extend(max_period)

    return


def get_sum_period(*signals):
    frequencies_list = []

    for i in range(0, len(signals), 1):
        frequencies_list.append(signals[i].fundamental_frequency)

    gcd_result = math.gcd(*tuple(frequencies_list))
    T_0 = 1 / gcd_result

    return T_0


def extend_to_sum(*signals):
    sum_period = get_sum_period(*signals) * 4 # Probando signal.extend(), sacar * 4 al terminar

    for i in range(0, len(signals), 1):
        signals[i].extend(sum_period)

    return


def buble_decreasing_sort(master_arr, slave_arr_1, slave_arr_2):
    size = len(master_arr)

    for i in range(0, size, 1):
        for j in range(0, size - 1, 1):
            if master_arr[j] < master_arr[j+1]:
                aux = master_arr[j+1]
                master_arr[j+1] = master_arr[j]
                master_arr[j] = aux

                aux = slave_arr_1[j+1]
                slave_arr_1[j+1] = slave_arr_1[j]
                slave_arr_1[j] = aux

                aux = slave_arr_2[j+1]
                slave_arr_2[j+1] = slave_arr_2[j]
                slave_arr_2[j] = aux

    return master_arr, slave_arr_1, slave_arr_2


def buble_increasing_sort(master_arr, slave_arr_1, slave_arr_2):
    size = len(master_arr)

    for i in range(0, size, 1):
        for j in range(0, size - 1, 1):
            if master_arr[j+1] < master_arr[j]:
                aux = master_arr[j+1]
                master_arr[j+1] = master_arr[j]
                master_arr[j] = aux

                aux = slave_arr_1[j+1]
                slave_arr_1[j+1] = slave_arr_1[j]
                slave_arr_1[j] = aux

                aux = slave_arr_2[j+1]
                slave_arr_2[j+1] = slave_arr_2[j]
                slave_arr_2[j] = aux

    return master_arr, slave_arr_1, slave_arr_2