# This is a lil program to review some basic python programming skills

# Centroiding is ultimately the name given to finding the centre of mass of a given peak in the data.
# PURPOSE: In addition to the basics of actually centroiding a spectrum, this tutorial is meant as an introduction to loops and conditionals, the building blocks of most python code.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import find_peaks

#Set up plot parameters
plt.rcParams['figure.figsize'] = (20.0, 10.0)

#Load up neon spectrum 
pixels = np.loadtxt('neon.txt',usecols=(0,)) #take zeroth column
signal = np.loadtxt('neon.txt',usecols=(1,)) #take first column