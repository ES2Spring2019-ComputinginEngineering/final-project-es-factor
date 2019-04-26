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
import numpy.fftpack as fft

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
def plotData(x, y, xlabel, ylabel):
    title = xlabel + " vs. " + ylabel
    plt.figure(figsize = (20, 10))
    plt.plot(x, y)
    plt.title(title, fontsize = 30)
    plt.xlabel(xlabel, fontsize = 24)
    plt.ylabel(ylabel, fontsize = 30)
    plt.xticks(fontsize = 18)
    plt.yticks(fontsize = 18)
    # plt.xlim(0, 5)
    # plt.ylim(-1 * 10**17, 1 * 10**17)
    plt.grid()
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

# Simulate a complex waveform to test for fundamental frequency
# https://pages.uoregon.edu/emi/1.php
def fourierSynthesis(funfreq, freq1, freq2):
    x = 
    y1 = STRONGESTA * sin(funfreq * x)
    y2 = weakA * sin(freq1 * x)
    y3 = weakA * sin(freq2 * x)
    y = 
    plotData(x, y, "Time", "Volts/Pressure")
    return

# Return strength of different frequencies
def fourier(amp):
    strength = fft.fft(amp)
    return strength

# Retuen the fundamental frequency
def fundFreq(strength):
    return fundFreq

# def filterPeriod(T):
# def autoZoom
# def plot3D
# fourier = hertz vs strength
# check by simulating sine waves

def main():
    amp, fs, time = readData()
    plotDataFile(time, amp, "Time", "Volts/Pressure")
    strength = fourierTrans(amp)
    plotDataFile(time, strength, "Frequency", "Strength")
    return 0

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
