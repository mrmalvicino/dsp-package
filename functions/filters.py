from scipy import signal
import numpy as np
import os
import sys

root_dir = os.path.dirname(__file__)
python_functions_path = os.path.realpath(os.path.join(root_dir, '..', '..', 'python-functions',))
sys.path.insert(0, python_functions_path)
matplotlib_functions_path = os.path.realpath(os.path.join(root_dir, '..', '..', 'matplotlib-functions',))
sys.path.insert(0, matplotlib_functions_path)

import python_functions as py_fx
import matplotlib_functions_path as plt_fx


def f_m(x, b=1, G=2, f_r=1000):
    
    """
    Calculates the central frequency for a given integer index or array of integer indexes. Definitions, notation and formulas are set according to UNE-EN 61260.

    Parameters
    ----------
    
    x : INTEGER, NUMPY ARRAY OF INTEGERS
        Determines which band's central frequencies are going to be calculated. The index x=0 generates the reference frequency, 1k Hz.
    
    b : INTEGER, optional
        Positive integer that determines the bandwith. The default is 1.
    
    G : FLOAT, optional
        Octave ratio. Usual values are 2 or 10^(3/10). The default is 2.
    
    f_r : FLOAT, optional
        Reference frequency. The default is 1000.

    Returns
    -------
    
    f_m : INTEGER, NUMPY ARRAY OF INTEGERS
        Central frequency (or frequencies) of the band (or bands).
    """
    
    if b%2 == 0:
        f_m = round_array(f_r * G**(x/b + 1/(2*b)), sig_digits=5)
    else:
        f_m = round_array(f_r * G**(x/b), sig_digits=5)
    
    return f_m


def f_c(c, f_m, b=1, G=2):
    
    """
    Calculates the cutoff frequencies for a given central frequency. Definitions, notation and formulas are set according to UNE-EN 61260.

    Parameters
    ----------
    
    c : INTEGER
        Determines whether to calculate the lowcut or highcut frequency. The only 2 input values are c=1 that stands for lowcut and c=2 that stands for highcut.
    
    f_m : INTEGER, NUMPY ARRAY OF INTEGERS
        Central frequency (or frequencies) of the band (or bands).
    
    b : INTEGER, optional
        Positive integer that determines the bandwith. The default is 1.
    
    G : FLOAT, optional
        Octave ratio. Usual values are 2 or 10^(3/10). The default is 2.

    Returns
    -------
    
    f_c : INTEGER, NUMPY ARRAY OF INTEGERS
        Cutoff frequency of the band (or bands).
    """
    
    f_c = f_m * (G**(((-1)**c)/(2*b)))
    
    return f_c


def bandpass_filter(x, f_s, b=1, G=2, N_order=3, worN=5120):
    
    """
    Generates a bandpass filter using signal.butter() according to UNE-EN 61260 norm.

    Parameters
    ----------
    
    x : INTEGER
        Determines which band's central frequencies are going to be calculated. The index x=0 generates the reference frequency, 1k Hz.
        
    f_s : INTEGER
        Sampling rate, which determines the Nyquist frequency.
    
    b : INTEGER, optional
        Positive integer that determines the bandwith. The default is 1.
    
    G : FLOAT, optional
        Octave ratio. Usual values are 2 or 10^(3/10). The default is 2.
    
    N_order : INTEGER, optional
        The order of the filter. Parameter of signal.butter(). The default is 3.
    
    worN : INTEGER, optional
        Number of frequencies computed by signal.sosfreqz(). The default is 5120.
    
    Returns
    -------
    
    sos : ARRAY
        Array of second-order filter coefficients.
    
    f_k : ARRAY
        Array of frequency bins.
    
    H_mag : ARRAY
        Array of magnitudes or absolute values of the filter.
    
    H_phase : ARRAY
        Array of phases of the filter.
    """
    
    f_nyq = f_s / 2
    f_1 = f_c(1, f_m(x, b, G), b, G)
    f_2 = f_c(2, f_m(x, b, G), b, G)
    f_1_norm = f_1 / f_nyq
    f_2_norm = f_2 / f_nyq
    
    sos = signal.butter(N_order, [f_1_norm, f_2_norm], btype='band', output='sos')
    omega_k, H = signal.sosfreqz(sos, worN)
    f_k = (omega_k/(2*np.pi))*f_s
    H_mag = 20*np.log10(abs(H))
    H_phase = np.arctan2(np.imag(H),np.real(H))
    
    return sos, f_k, H_mag, H_phase


def mean(v, k=2):
    
    """
    Calculates the generalized mean of a given vector.

    Parameters
    ----------
    
    v : NUMPY ARRAY
        Vector which values are going to be evaluated.
    
    k : INTEGER, optional
        Positive integer that defines the root, being k=2 the RMS value. The default is 2.

    Returns
    -------
    
    v_mean : FLOAT
        Mean value.
    """
    
    N = len(v)
    v_sum = 0
    
    for v_i in v:
        v_sum = v_sum + v_i**k
    
    v_mean = (v_sum/N)**(1/k)
    
    return v_mean


def SPL(v, p_ref=0.00002):
    
    """
    Calculates the sound pressure level for a given reference value by definition.
    
    Parameters
    ----------
    
    v : FLOAT, NUMPY ARRAY
        Pressure [Pa].
    
    p_ref : FLOAT, optional
        Reference value. The default is 20u Pa.
    
    Returns
    -------
    
    SPL : FLOAT, NUMPY ARRAY
        Sound pressure level.
    """
    
    SPL = 10*np.log10((v/p_ref)**2)
    
    return SPL


def SPL_ave(SPL):
    
    """
    Calculates the sound pressure level average by definition.
    
    Parameters
    ----------
    
    SPL : NUMPY ARRAY
        Array of sound pressure levels to evaluate.
    
    Returns
    -------
    
    SPL_ave : FLOAT
        Average sound pressure level.
    """
    
    N = len(SPL)
    SPL_sum = 0
    
    for SPL_i in SPL:
        SPL_sum = SPL_sum + 10**(SPL_i/20)
    
    SPL_ave = 20*np.log10(SPL_sum/N)
    
    return SPL_ave


def filter_bank(audio_input, f_s, p_ref=0.00002, b=1, G=2, N_order=3):
    
    """
    Generates a filter bank and applies it to a given input to obtain the frequency spectrum averaged by fractions of octaves.
    
    Parameters
    ----------
    
    audio_input : ARRAY
        Data to be filtered.
    
    f_s : INTEGER
        Sampling rate, which determines the Nyquist frequency.
    
    b : INTEGER, optional
        Positive integer that determines the bandwith. The default is 1.
    
    G : FLOAT, optional
        Octave ratio. Usual values are 2 or 10^(3/10). The default is 2.
    
    N_order : INTEGER, optional
        The order of the filter. Parameter of signal.butter(). The default is 3.
    
    Returns
    -------
    
    sos_bank : LIST OF ARRAYS
        List of arrays of second-order filter coefficients for each band.
    
    bands : ARRAY OF FLOATS
        Array of bands' central frequencies.
    
    SPL_averages : ARRAY OF FLOATS
        List of bands' sound pressure level average.
    
    """
    
    x_vec = range(-5*b-int(b/3), 5*b-int(b/3), 1) # Frequencies index array
    sos_bank = []
    SPL_averages = np.array([])
    bands = f_m(np.array(x_vec), b)

    for x in x_vec:
        sos_x = bandpass_filter(x, f_s, b, G, N_order)[0]
        sos_bank.append(sos_x)
    
    for sos_x in sos_bank:
        filtered_signal_x = signal.sosfilt(sos_x, audio_input)
        SPL_x = SPL(filtered_signal_x, p_ref)
        SPL_averages = np.concatenate(( SPL_averages, np.array([SPL_ave(SPL_x)]) ))
    
    return sos_bank, bands, SPL_averages


def fft(x, f_s):
    
    """
    Fast Fourier transform of a given time signal.

    Parameters
    ----------
    
    x : NUMPY ARRAY
        Function of time.
    
    f_s : INTEGER
        Sampling rate, which determines the Nyquist frequency..

    Returns
    -------
    
    X_frequencies : NUMPY ARRAY
        Array of frequencies which the function of time is composed of.
    
    X_magnitude : NUMPY ARRAY
        Magnitudes of the frequencies.
    
    X_phase : NUMPY ARRAY
        Phase of the frequencies.
    """
    
    fft_raw = np.fft.fft(x)
    fft = fft_raw[:len(fft_raw)//2]
    X_magnitude = abs(fft)/len(fft)
    X_phase = np.arctan2(np.imag(fft),np.real(fft))
    X_frequencies = np.linspace(0,f_s/2, len(fft))
    
    return X_frequencies, X_magnitude, X_phase