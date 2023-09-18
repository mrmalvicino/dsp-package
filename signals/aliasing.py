import numpy as np

class Aliasing:
    """
    Provides methods for processing audio aliasing.
    """

    def __init__(self):
        """
        Constructs an Aliasing object with default settings.
        """
        pass

    def frequencies_sum(frequencies, sampling, duration):
        """
        Performs the sum of the sinusoidal signals with the frequencies entered, with a number of samples entered and with a duration entered.

        Args:
            frequencies (tuple): Frequencies of the sinusoidal signals to sum.
            sampling (int): Number of samples of the result signal. Must be a value between 10 and 100k.
            duration (int): Seconds of the signal duration, begins at 0 and stops at this parameter value.

        Returns:
            time, output (tuple): Time values and sum generated.
        """

        output = 0
        time = np.linspace(0, duration, sampling * duration)

        for count, frequency in enumerate(frequencies):
            output = output + np.sin(2 * np.pi * frequency * time)

        return (time, output)