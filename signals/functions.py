import os
import numpy as np


def root_dir(param=0, open_root_dir=False):
    
    """
    Traces a folder relative to where the script is being executed.
    Defines this folder as "root directory" and returns it absolute path.
    
    Parameters
    ----------
    
    param : STRING OR INTEGER
        Name of the folder (str) to trace or level of hierarchy (int) to define as root directory.
    
    open_root_dir : BOOLEAN, optional
        Determines whether the root directory will be opened after being defined. The default is False.
    
    Raises
    ------
    
    ValueError
        Invalid input.

    Returns
    -------
    
    root_dir : STRING
        Path of the folder defined as root directory.
    
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


def save(param, **kwargs):
    
    """
    Saves a given numpy array or matplotlib plot.
    
    Parameters
    ----------
    
    param : FIGURE OR ARRAY
        Object that is going to be saved.
    
    **kwargs : UNPACKED DICTIONARY
    
        **save_kwargs : UNPACKED DICTIONARY
            Kwargs for internal use.
    
            file_dir : STRING
                Path of the directory where the file is going to be saved.
    
            file_name : STRING
                Name of the file which is going to be saved.
    
            ask_for_confirmation : BOOLEAN
                Determines whether the script should ask for user input confirmation.
    
        **savefig_kwargs : UNPACKED DICTIONARY
            Kwargs for the savefig() method.
    
            bbox_inches : STRING
    
            dpi : INTEGER
    
            transparent : BOOLEAN
    
    Raises
    ------
    
    ValueError
        Invalid input.
    
    Returns
    -------
    
    None.

    """
    
    save_kwargs = {'file_dir': os.path.dirname(__file__), 'file_name': 'saved_by_' + os.getlogin(), 'ask_for_confirmation': False}
    
    for key, value in kwargs.items():
        if key in save_kwargs and value != save_kwargs[key]:
            save_kwargs[key] = value
    
    if save_kwargs['ask_for_confirmation'] == True:
        save = 'ask'
    else:
        save = 'y'

    while save != 'y' and save != 'n':
        save = input('Do you really want to save? [y/n] ')
    
    if save == 'y':
        if type(param) == plt.Figure:
            savefig_kwargs = {'bbox_inches': 'tight', 'dpi': 300, 'transparent': False}
            
            for key, value in kwargs.items():
                if key in savefig_kwargs and value != savefig_kwargs[key]:
                    savefig_kwargs[key] = value
            
            param.savefig(os.path.join(save_kwargs['file_dir'], save_kwargs['file_name'] + '.png'), **savefig_kwargs)
        
        elif type(param) == np.ndarray:
            np.save(os.path.join(save_kwargs['file_dir'], save_kwargs['file_name']), param)
        
        else:
            raise ValueError(f'{type(param)} input not supported.')
    
    return


def make_list(v):

    """
    Attempts to convert a given variable into a list.

    Parameters
    ----------

    v : ANY TYPE

    Returns
    -------

    lst : LIST

    """

    if type(v) == list:
        lst = v
    elif type(v) == np.ndarray:
        lst = v.tolist()
    else:
        lst = list(v)

    return lst


def round_array(v, sig_digits=3):
    
    """
    Attempts to round a given float or the floats of a given array to a certain number of significant figures. Contemplates that the decimal (. ,) and negative (-) symbols are not digits.

    Parameters
    ----------
    
    v : FLOAT, NUMPY ARRAY OF FLOATS
        Input that is going to be rounded.
    
    sig_digits : TYPE, optional
        Significant figures or digits. The default is 3.

    Returns
    -------
    
    w : FLOAT, NUMPY ARRAY OF FLOATS
        Rounded output.

    """
    
    if type(v) == np.ndarray:
        w = np.array([])
        for v_i in v:
            if '-' not in str(v_i):
                int_digits = len(str(int(v_i)))
            else:
                int_digits = len(str(int(v_i))) - 1
            v_i = v_i/10**int_digits
            v_i = round(v_i, sig_digits)
            v_i = v_i * (10**int_digits)
            if type(v_i) == float and str(v_i)[-2:] == '.0':
                v_i = int(v_i)
            w = np.append(w, v_i)
    elif type(v) == float:
        if '-' not in str(v):
            int_digits = len(str(int(v)))
        else:
            int_digits = len(str(int(v))) - 1
        dec_digits = len(str(v)) - int_digits - 1
        v = v/10**int_digits
        v = round(v, sig_digits)
        v = v * (10**int_digits)
        if type(v) == float and str(v)[-2:] == '.0':
            w = int(v)
        if type(v) == float and str(v)[-dec_digits+1:] == '9'*(dec_digits-1):
            w = round(v, 1)
        w = v
    
    return w


def closest_to_average(v):
    
    """
    Returns the value from a given list which is closest to the average of all the values from it.

    Parameters
    ----------

    v : LIST OF FLOATS
        Input variable of floats in which the value that aproximates to the average is going to be the output. The variable may also be a set, a tuple or a numpy array.

    Returns
    -------

    closest : FLOAT
        Float from the input which difference with the exact average is the smallest.

    """
    
    floats_list = make_list(v)
    average = sum(floats_list)/len(floats_list)
    closest = 0
    
    if average in floats_list:
        closest = average
    else:
        for i in floats_list:
            difference = abs(average - i)
            if difference < abs(average - closest):
                closest = i
    return closest


def info(v):
    
    """
    Gives descriptive information about a given variable.

    Parameters
    ----------
    
    v : (Any type)
        Variable of which information is being asked for.

    Returns
    -------
    
    None.

    """
    
    if type(v) == int:
        print(f'{v} is an integer.')
    
    elif type(v) == float:
        print(f'{v} is a float.')
    
    elif type(v) == str:
        print(f'"{v}" is a string.')
    
    elif type(v) == list:
        print(f'The input is a list which contains {len(v)} elements.')
    
    elif type(v) == tuple:
        print(f'The input is a tuple of {len(v)} components.')
    
    elif type(v) == dict:
        print(f'The input is a dictionary of {len(v)} elements:')
        print(v.items())
    
    elif type(v) == np.ndarray:
        N = str(v.shape[0])
        
        if len(v.shape) == 1:
            N = 'one dimention'
        else:
            for i in range(1,len(v.shape),1):
                N = N + 'x' + str(v.shape[i])
        
        print(f'The input is a {N} array of {v.size} elements.')
    
    else:
        print(f'There is no information available for {type(v)}.')
    
    return


def list_udim(list_in:list):
    
    """
    Transforms a matrix-like list into a regular one.

    Parameters
    ----------
    
    list_in: LIST
        Input list to be converted.

    Returns
    -------
    
    list_out: LIST
        Output list converted.

    """
    
    list_out = []
    dim = np.array(list_in).shape

    if len(dim) > 1:    
        for x in range(len(list_in)):
            for y in range(len(list_in)):
                list_out.append(list_in[x][y])
    else:
        list_out = list_in
        
    return list_out