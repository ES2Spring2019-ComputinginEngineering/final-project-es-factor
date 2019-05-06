"""This is the python file that your instructors will run to test your code
make sure it runs correctly when someone downloads your repository. You 
might want to test this on a classmates computer to be sure it works!"""

# This files should not contain any function defitions


# IMPORT STATEMENTS
import inputaudio as mod
import numpy.fft as fft
import numpy as np

# Read in wave file and return y coordinates
# Notes that can be used: F4, G4, Ab4, A4, Bb4, C5

# Create a domain for the fundamental frequency graphs
x = np.linspace(0, 0.1, 1000)

# Manually enter in note
# Read in sound data file
# Plot data from parsed data file
amp, fs, time = mod.readData("C5")
mod.plotData(time, amp, "Time", "Volts/Pressure of Data")

# Graph the frequency vs. Strength after Fourier Transformation of values
# from data file
freq = fft.fftfreq(amp.size)
strength = mod.fourier(amp)
mod.plotData(freq, strength, "Frequency", "Strength of Data")
FF = mod.fundFreq(strength, freq)

# Manually enter in note
# Graph the frequency vs strength after fourier transformation of simulated
# values
y = mod.fourierSynthesis(mod.C5, time)
simfreq = fft.fftfreq(y.size)
simstrength = mod.fourier(y)
mod.plotData(simfreq, simstrength, "Frequency", "Strength of Simulation")
simFF = 174.02 * mod.fundFreq(simstrength, simfreq) / 27.626

# Graph the sine waves with the fundamental frequency found from the data file,
# simulation, and the known frequency
mod.plotData(x, np.sin(FF * x), "Time", "Volts/Pressure of Data")
print(FF)
mod.plotData(x, np.sin(simFF * x), "Time", "Simulation Fundamental Frequency")
print(simFF)
# Manually enter in note
mod.plotData(x, np.sin(mod.C5 * x), "Time", "Actual Fundamental Frequency")
print(mod.C5)