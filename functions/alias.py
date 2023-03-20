def frec_sum(frequencies, sampling, duration):
    
    """
    Performs the sum of the sinusoidal signals with the frequencies entered, with a number of samples entered and with a duration entered.

    Parameters
    ----------
    
    frequencies : TUPLE
        Frequencies of the sinusoidal signals to sum.
    
    sampling : INTEGER
        Number of samples of the result signal. Must be a value between 10 and 100k.
    
    duration : INTEGER
        Seconds of the signal duration, begins at 0 and stops at this parameter value.
        
    Returns
    -------

    output : TUPLE
        Tuple with the time values and the sum generated.
    """
    
    output = 0
    time = np.linspace(0, duration, sampling*duration)
    for count, frequency in enumerate(frequencies):
        output = output + np.sin(2*np.pi*time*frequency)
    
    return (time, output)