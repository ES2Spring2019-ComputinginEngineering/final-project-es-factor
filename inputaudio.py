#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:13:20 2019

@author: kristinapuzak
"""

# import scipy.signal as sig
import matplotlib.pyplot as plt
# import plotly.plotly as ply
import numpy as np
import wave
import numpy.fft as fft

F4 = 349.23
G4 = 392.00
Ab4 = 415.30
A4 = 440
Bb4 = 466.16
B4 = 493.88
C5 = 523.25

# Imports a sound file and extracts raw audio data (amp) and frames per second
# (fs) and convert frames per second into number of seconds elapsed (Time).
# Returns the y-value as a numpy array of int64, number of frames per second, 
# and amount of time elapsed
def readData(note):
    filename = "Piano" + note + ".wav"
    spf = wave.open(filename, 'r')
    amp = spf.readframes(-1)
    amp = np.frombuffer(amp, "Int32")
    fs = spf.getframerate()
    time = np.linspace(0, len(amp)/fs, num=len(amp))
    return (amp, fs, time)

# Plot an x vs y graph with the x axis and y axis labels and a title
def plotData(x, y, xlabel, ylabel):
    title = xlabel + " vs. " + ylabel
    plt.figure(figsize = (20, 10))
    plt.plot(x, y)
    plt.title(title, fontsize = 30)
    plt.xlabel(xlabel, fontsize = 24)
    plt.ylabel(ylabel, fontsize = 30)
    plt.xticks(fontsize = 18)
    plt.yticks(fontsize = 18)
    # plt.xlim(-.1, .1)
    # plt.ylim(-1 * 10**17, 1 * 10**17)
    plt.grid()
    plt.show()

# Return strength of different frequencies
def fourier(amp):
    strength = fft.fft(amp)
    return strength

# Return the fundamental frequency
def fundFreq(strength, freq):
    index = np.argsort(strength)
    fundFreq = abs(174.02 * freq[index[0]]/0.003954)
    return fundFreq

# Simulate a complex waveform to test for fundamental frequency
def fourierSynthesis(note, time):
    freq1 = np.random.randint(300, 600)
    freq2 = np.random.randint(300, 600)
    x = time
    y1 = 2 * 10**12 * np.sin(note * x)
    y2 = 9 * 10**11 * np.sin(freq1 * x)
    y3 = 9 * 10**11 * np.sin(freq2 * x)
    y = y1 + y2 + y3
    plotData(x, y, "Time", "Volts/Pressure of Simulation")
    return y

# found = [0.007946, 0.00891, 0.0094657, 0.0100, 0.01059, 0.011219, 0.0119]
# known =[349.23, 392, 415.30, 440, 466.16, 493.83, 523.25]
# found = [55.48685, 62.2973, 65.986, 64.81286, 74.05089, 78.44995, 83.113]
# plt.figure(figsize = (20, 10))
# plt.plot(found, known)



######
# Function graveyard
"""
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

#Read Audio Samples
input_data = read("Sample.wav")
audio = input_data[1]

#Plot First # of Samples
plt.plot(audio[0:1000])

#Set Labels
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.title("Sample Wav")
plt.show()


# Use signal processing module to return an array of peaks
def findPeaks(amp):
    peaks, _ = sig.find_peaks(amp)
    peaks.astype(float)
    return peaks

# Return the period by finding the average distance between an array of peaks
def calculatePeriod(peaks):
    i = 1
    period = np.array([])
    while i < len(peaks):
        period = np.append(period, ((peaks[i])-(peaks[i-1])))
        i += 1
        # print(T, T.size)
    return period

def filterPeriod(T):
def autoZoom
def plot3D
fourier = hertz vs strength
check by simulating sine waves
"""
