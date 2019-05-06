# Frequencies of a .wav file

This program is designed to:

-Read a WAV sound file and plot it as a amplitude vs. time graph

-Create an amplitude vs. frequency graph from the amplitude vs. time graph

-Create a function which can determine the fundamental frequency from an amplitude vs. frequency graph

-Print out the fundamental frequency derived from the function



The program will produce seven graphs:
1) sound wave from sound file you inputted on line 22
2) the Fourier Transformation of the data from the sound file
3) simulated complex sound wave of the note you inputted on line 35
4) the Fourier Transformation of the simulated complex sound wave
5) the sine wave with the fundamental frequency found from the sound file
6) the sine wave with the fundamental frequency found from the simulation
7) the sine wave with the actual fundamental frequency


## Instructions (inside driver script)

Input a note on lines 22, 35, 48, and 49. The options can be found on line 14

The notes should be the same, but the program runs if they are not


## File List

inputaudio: Module that contains functions that parse sound files, plot 2-D graphs, and determine fundamental frequency

main: Calls inputaudio module and graphs the raw soundwaves, fourier transformations, and sinusoidal waves with the given frequencies of data from the sound file, a simulated complex waveform, and the actual frequency

# Libraries

Libraries used include:
-matplotlib.pyplot
-numpy.fft
-numpy
-wave

# Functions

Important functions used include:
readData(note)
-parses data from sound file

plotData(x, y, xlabel, ylabel)
-plots the data

fourier(amp)
-determines strength of each frequency

fundFreq(strength, freq)
-determines the fundamental frequency

fourierSynthesis(note, time)
-simulates a complex wave form to test for fundamental frequency



