# This is your Final Project ReadMe Template

The file is inside your final project repository called "README.md"

You should include in your final project readme a description of the project, a list of all the files that you have created and instructions for use.

This readme is written in a language called markdown. This is not a programming language but a formatting langauge. There are symbols (syntax) used to indicate how to format the text. For example the pound symbol (i.e. the hashtag) is used to format a title; two of the same symbol format a heading, and three format a sub-heading.

Below is some example text in markdown however this alone is not suffiecent for the final project. **Make sure you follow the directions on Canvas.**

Delete the instructions above this line and the line:

---------------------------------------------

# Project Title

Read a WAV sound file and plot it as a amplitude vs. time graph
Create an amplitude vs. frequency graph from the amplitude vs. time graph
Create a function which can determine the fundamental frequency from an amplitude vs. frequency graph
Print out the fundamental frequency derived from the function

The program will produce seven graphs:
1) sound wave from sound file you inputted on line 22
2) the Fourier Transformation of the data from the sound file
3) simulated complex sound wave of the note you inputted on line 35
4) the Fourier Transformation of the simulated complex sound wave
5) the sine wave with the fundamental frequency found from the sound file
6) the sine wave with the fundamental frequency found from the simulation
7) the sine wave with the actual fundamental frequency


## Instructions

Input a note on lines 22, 35, 48, and 49. The options can be found on line 14

The notes should be the same, but the program runs if they are not

Describe how the users(instructors) should run your code to see an ***easy to run example of the functionality***. This should all be in a *main.py* "driver" script.

## File List

inputaudio: Module that contains functions that parse sound files, plot 2-D graphs, and determine fundamental frequency

main: Calls inputaudio module and graphs the raw soundwaves, fourier transformations, and sinusoidal waves with the given frequencies of data from the sound file, a simulated complex waveform, and the actual frequency

## How to format your readme

In your readme, you can:
```
Give code examples
```

You can also include useful links, like this one with information about [formatting markdown](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)

You can 
- Also
- Make
- Lists
