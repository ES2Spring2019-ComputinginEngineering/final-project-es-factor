#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:13:20 2019

@author: kristinapuzak
"""

import scipy.signal as sig
import matplotlib.pyplot as plt
import plotly.plotly as ply
import numpy as np
import wave

def readData():
    spf = wave.open('PianoF.wav', 'r') #import sound file
    #Extract Raw Audio from Wav File
    amp = spf.readframes(-1)
    amp = np.fromstring(amp, 'Int16')
    fs = spf.getframerate() #frames per second
    #Convert Frames to Time
    time = np.linspace(0, len(amp)/fs, num=len(amp))
    return (amp, fs, time)
(amp, fs, time) = readData()

def plotData(time, amp):
    plt.figure(1)
    plt.title('Amplitude Wave')
    plt.plot(time, amp)
    plt.xlim(2,2.05) #Adjust limits of the x-axis
    plt.ylim(-3000,3000) #Adjust limits of the y-axis
    plt.grid()
    plt.show()
plotData(time, amp)

def fourier(amp, fs, time):
    ts = amp / fs
    ff = 


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
