def inverse_filter(x:tuple, T:int, f1:int, f2:int):
    
    """
    Generates an inverse filter from a sweep signal over time.

    Parameters
    ----------
    
    x : TUPLE
        Tuple of a sweep signal with information of the time and magnitude.
    
    T : INTEGER
        Sweep signal duration.
    
    f1 : INTEGER
        Sweep start frequency.
    
    f2 : INTEGER
        Sweep end frequency.

    Returns
    -------
    
    output : TUPLE
        Tuple with data time from 0 to T, and magnitude of inverse filter.
    """

    t = x[0]
    R = np.log(f2/f1) # rate sweep
    L = T/R 
    x = x[1][::-1] # inverse the numpy array
    f = x*np.exp(-t/L)
    output = (t, f)

    return output


def impulse_response(x:np.ndarray, y:np.ndarray, f_s:int):
    
    """
    Get the impulse response of a system using h(t) = ifft(fft(x)*fft(y)).
    
    Parameters
    ----------
    
    x : NUMPY ARRAY
        Amplitude array of the system's input signal.
    
    y : NUMPY ARRAY
        Amplitude array of the system's output signal.
    
    f_s : INTEGER
        Sampling frequency.

    Raises
    ------

    ValueError
        The input and output signals must have the same dimensions.

    Returns
    -------
    
    ir : TUPLE OF NUMPY ARRAYS
        Time and amplitude data of the impulse response.
    """
    
    if x.shape != y.shape:
        raise ValueError('The input and output signals must have the same dimensions.')
    
    X = fft(x)
    Y = fft(y)
    h = np.fft.ifft(X*Y) 
    h = h/max(abs(h)) # Normalize
    t = np.linspace(0, h.size/f_s, h.size)
    ir = (t, h)

    return ir