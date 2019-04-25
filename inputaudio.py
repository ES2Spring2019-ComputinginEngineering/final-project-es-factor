#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:13:20 2019

@author: kristinapuzak
"""

import scipy.signal as sig
import matplotlib.pyplot as plt
# import plotly.plotly as ply
import numpy as np
import wave

# Imports a sound file and extracts raw audio data (amp) and frames per second
# (fs) and convert frames per second into number of seconds elapsed (Time).
# Returns the y-value as a numpy array of int64, number of frames per second, 
# and amount of time elapsed
def readData():
    spf = wave.open("PianoF.wav", 'r')
    amp = spf.readframes(-1)
    amp = np.frombuffer(amp, "Int64")
    fs = spf.getframerate()
    time = np.linspace(0, len(amp)/fs, num=len(amp))
    return (amp, fs, time)

# Plot a time vs amp graph that is zoomed in to see the individual waves
def plotData(time, amp):
    plt.figure(figsize = (20, 10))
    plt.plot(time, amp)
    plt.title("Time vs Pressure", fontsize = 30)
    plt.xlabel("Time", fontsize = 24)
    plt.ylabel("Volts/Pressure", fontsize = 30)
    plt.xticks(fontsize = 18)
    plt.yticks(fontsize = 18)
    plt.xlim(0, 5)
    # plt.ylim(-1 * 10**17, 1 * 10**17)
    plt.grid()
    plt.show()

def findPeaks(amp):
    peaks, _ = sig.find_peaks(amp)
    peaks.astype(float)
    return peaks

def calculatePeriod(peaks):
    i = 1
    T = np.array([])
    while i < len(peaks):
        T = np.append(T, ((peaks[i])-(peaks[i-1])))
        i += 1
        # print(T, T.size)
    return T

# def filterPeriod(T):
    
    

# def fourier(amp, fs, time):
    # ts = amp / fs
    # ff = 

# frequency = amplitude/time

(amp, fs, time) = readData()
oned = np.fft.fft(amp)
plotData(time, amp)
plotData(time, oned)
peaks = findPeaks(amp)
T = calculatePeriod(peaks)
plotData(time[:T.size], T)

######
"""from scipy.io.wavfile import read
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
plt.show()"""
