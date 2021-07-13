#
# 13) Data analyzer
#

########################################################################################################################
# Importing modules

import os                       # OS operations
import numpy as np              # Math and arrays
import matplotlib.pyplot as pl  # Data visualization
pl.style.use("seaborn-paper")   # I just like this style

########################################################################################################################
# We are going to use a dictionary to simplify our data management

data = {}

########################################################################################################################
# We first go over an entire directory to go through each file

for root, dirs, files in os.walk("./Data/"):
    for file in files:
        data[file] = np.loadtxt(root + file, skiprows = 1)

########################################################################################################################
# We are going to create a figure of the mass-radius with atmo7
# Between 0 and 10 Me, to avoid a squashed plot

pl.figure()

# Going through the files and their data to plot them
# d is the name of the file ("index")
# k is the data loaded 
for d, k in data.items():
    pl.plot(k[:,1], k[:,2] + k[:,-1], label = d)

# Some limits to look better
pl.xlim([0, 10])
pl.ylim([0.5, 3])

# Displaying information
pl.title("Mass radius relations")
pl.xlabel("Mass [$M_{}$]".format("\U00002295"))
pl.ylabel("Radius [$R_{}$]".format("\U00002295"))
pl.legend()

# Saving and closing
pl.savefig("all_data.pdf")
pl.close()

########################################################################################################################
