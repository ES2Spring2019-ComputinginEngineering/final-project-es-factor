"""This is the python file that your instructors will run to test your code
make sure it runs correctly when someone downloads your repository. You 
might want to test this on a classmates computer to be sure it works!"""

# This files should not contain any function defitions


# IMPORT STATEMENTS
import inputaudio.py as mod
import numpy.fft as fft


# DEMONSTRATION CODE
# Read in wave file and return y coordinates
# Notes that can be used: F4, G4, Ab4, A4, Bb4, C5

amp, fs, time = mod.readData("Bb4")
mod.plotData(time, amp, "Time", "Volts/Pressure of Data")

freq = fft.fftfreq(amp.size)
strength = mod.fourier(amp)
mod.plotData(freq, strength, "Frequency", "Strength of Data")
FF = mod.fundFreq(strength, freq)
print(FF)
mod.plotData(time, FF, "Time", "Volts/Pressure of Data")

y = mod.fourierSynthesis(mod.Bb4, time)
simfreq = fft.fftfreq(y.size)
simstrength = mod.fourier(y)
mod.plotData(simfreq, simstrength, "Frequency", "Strength of Data")
simFF = 174.02 * mod.fundFreq(simstrength, simfreq) / 27.626
print(simFF)
mod.plotData(time, simFF, "Time", "Volts/Pressure of Simulation")