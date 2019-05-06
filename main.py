"""This is the python file that your instructors will run to test your code
make sure it runs correctly when someone downloads your repository. You 
might want to test this on a classmates computer to be sure it works!"""

# This files should not contain any function defitions


# IMPORT STATEMENTS
import inputaudio as mod
import numpy.fft as fft
import numpy as np


# DEMONSTRATION CODE
# Read in wave file and return y coordinates
# Notes that can be used: F4, G4, Ab4, A4, Bb4, C5


x = np.linspace(0, 0.1, 1000)

# Manually enter in note
amp, fs, time = mod.readData("B4")
mod.plotData(time, amp, "Time", "Volts/Pressure of Data")

freq = fft.fftfreq(amp.size)
strength = mod.fourier(amp)
mod.plotData(freq, strength, "Frequency", "Data Fundamental Frequency")
FF = mod.fundFreq(strength, freq)

# Manually enter in note
y = mod.fourierSynthesis(mod.B4, time)
simfreq = fft.fftfreq(y.size)
simstrength = mod.fourier(y)
mod.plotData(simfreq, simstrength, "Frequency", "Strength of Data")
simFF = 174.02 * mod.fundFreq(simstrength, simfreq) / 27.626

mod.plotData(x, np.sin(FF * x), "Time", "Volts/Pressure of Data")
print(FF)
mod.plotData(x, np.sin(simFF * x), "Time", "Simulation Fundamental Frequency")
print(simFF)
# Manually enter in note
mod.plotData(x, np.sin(mod.B4 * x), "Time", "Actual Fundamental Frequency")
print(mod.B4)