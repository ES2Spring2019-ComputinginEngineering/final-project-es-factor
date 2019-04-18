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
import sys

def readData():
    spf = wave.open('wavfile.wav', 'r')

    #Extract Raw Audio from Wav File
    amp = spf.readframes(-1)
    amp = np.fromstring(amp, 'Int16')
    fs = spf.getframerate()

    return (amp)


def plotData(Time, amp):
    Time = np.linspace(0, len(amp).fs, num=len(amp))
    
    plt.figure(1)
    plt.title('Amplitude Wave')
    plt.plot(Time, amp)
    plt.show()


######
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
