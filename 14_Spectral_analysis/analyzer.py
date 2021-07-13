#
# 14) Spectral data
#

########################################################################################################################
# Importing modules

import numpy as np              # Math and arrays
import matplotlib.pyplot as pl  # Data visualization
pl.style.use("seaborn-paper")   # I just like this style

########################################################################################################################
# Defining functions and constants

c_fixed = 1     # We're going to say the peak have fixed width for now

# Gaussian function, to simulate the rays
def gaussian(a, b, c, x):
    return a * np.exp( - (x - b)**2 / (2 * c**2) )

########################################################################################################################

# Loading the spectral data from the file
data = np.loadtxt("./all.tab", usecols = [0, 1])

# Creating the continuum on which to add the components of each rays
continuum = np.zeros(len(data[:,0]))

# Computing the gaussian and adding it to the continuum
for idx, wave in enumerate(data[:,0]):
    continuum += gaussian(data[:,1][idx], wave, c_fixed, data[:,0])

########################################################################################################################

# Creating the figure
pl.figure(figsize=(20, 5))

# Maximizing space on the figure
pl.axes([0.04, 0.1, 0.95, 0.8])

# Plotting the spectrum
pl.plot(data[:,0], continuum, color = "purple")

# Limits for better display
pl.xlim([min(data[:,0]), max(data[:,0])])

# Displaying information
pl.title("Spectrum of 122P/deVico")
pl.xlabel("Wavelength [Å]")
pl.ylabel("Intensity [arbitrary units]")

# Saving and closing
pl.savefig("intensities.pdf")
pl.close()

########################################################################################################################
