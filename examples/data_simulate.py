import numpy
from scipy.stats import norm

def gaussian_spectrum(peaks, widths, amplitudes, x):
    spectrum = numpy.zeros(len(x))
    for i in range(len(peaks)):
        spectrum += amplitudes[i] * numpy.exp(-numpy.power((x - peaks[i])/widths[i], 2))
    return spectrum
