#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:13:20 2019

@author: kristinapuzak
"""

import scipy.signal as sig
import matplotlib.pyplot as plt
import numpy as np
import wave

def readData():
    spf = wave.open('PianoF.wav', 'r')
    #Extract Raw Audio from Wav File
    amp = spf.readframes(-1)
    amp = np.fromstring(amp, 'Int16')
    fs = spf.getframerate()
    #Convert Frames to Time
    Time = np.linspace(0, len(amp)/fs, num=len(amp))

    return (amp, Time)
(amp, Time) = readData()

def plotData(Time, amp):
    plt.figure(1)
    plt.title('Amplitude Wave')
    plt.plot(Time, amp)
    plt.xlim(2,2.05) #Adjust limits of the x-axis
    plt.ylim(-3000,3000) #Adjust limits of the y-axis
    plt.grid()
    plt.show()
    
plotData(Time, amp)


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
