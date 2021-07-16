#
# 17) Numpy and pandas
#

########################################################################################################################
# Importing modules

import os                       # OS operations
import numpy as np              # Math and arrays
import pandas as pd             # Dataframes functionalities
import matplotlib.pyplot as pl  # Data visualization
pl.style.use("seaborn-paper")   # I just like this style

########################################################################################################################

# Creating empty dictionaries for each method
data_num = {}
data_pan = {}

# Iterating through the input files
for root, dirs, files in os.walk("./Comparison/"):
    for file in files:
        data_num[file] = np.loadtxt(root + file, delimiter = ',', skiprows = 1, usecols = [0, 2, 3, 4, 5, 6, 7, 8])
        data_pan[file] = pd.read_csv(root + file)

# Just comparing data types and shape
# We can see that the numpy format couldn't load the string type, so we are lacking one column
for key in data_num.keys():
    print("Key {}".format(key))
    print("    - For numpy, we have type: {}, with shape: {}".format(type(data_num[key]), np.shape(data_num[key])))
    print("    - For pandas, we have type: {}, with shape: {}".format(type(data_pan[key]), data_pan[key].shape))

# We are now going to create the same figure using both methods, and compare the results
# The outputs should be exactly the same!

########################################################################################################################
# Creating the figure using numpy

# Setting the space to use by each figure
x_space = 0.25

# Creating the figure, with 3 times the normal width to accommodate my graphs
pl.figure(figsize = (19.2, 4.8))

# Creating the left figure, for the width
pl.axes([0.05, 0.1, x_space, 0.8])

for key, value in data_num.items():
    pl.plot(value[:,4], value[:,5])

pl.title("Width")
pl.xlabel("Camera position [cm]")
pl.ylabel("Size [mm]")

# Creating the middle figure, for the thickness
pl.axes([0.375, 0.1, x_space, 0.8])

for key, value in data_num.items():
    pl.plot(value[:,4], value[:,6], label = key)

pl.title("Thickness")
pl.xlabel("Camera position [cm]")
pl.ylabel("Size [mm]")
pl.legend()

# Creating the right figure, for the power
pl.axes([0.7, 0.1, x_space, 0.8])

for key, value in data_num.items():
    pl.plot(value[:,4], value[:,7])

pl.title("Power")
pl.xlabel("Camera position [cm]")
pl.ylabel("Power [mW]")

# Saving and closing
pl.savefig("data_from_numpy.pdf")
pl.close()

########################################################################################################################
# Creating the figure using pandas

# Creating the figure, with 3 times the normal width to accommodate my graphs
pl.figure(figsize = (19.2, 4.8))

# Creating the left figure, for the width
pl.axes([0.05, 0.1, x_space, 0.8])

for key, value in data_pan.items():
    pl.plot(value["Camera position (cm)"], value["Nappe width (mm)"])

pl.title("Width")
pl.xlabel("Camera position [cm]")
pl.ylabel("Size [mm]")

# Creating the middle figure, for the thickness
pl.axes([0.375, 0.1, x_space, 0.8])

for key, value in data_pan.items():
    pl.plot(value["Camera position (cm)"], value["Nappe thickness (mm)"])

pl.title("Thickness")
pl.xlabel("Camera position [cm]")
pl.ylabel("Size [mm]")
pl.legend()

# Creating the right figure, for the power
pl.axes([0.7, 0.1, x_space, 0.8])

for key, value in data_pan.items():
    pl.plot(value["Camera position (cm)"], value["Beam power (mW)"])

pl.title("Power")
pl.xlabel("Camera position [cm]")
pl.ylabel("Power [mW]")

# Saving and closing
pl.savefig("data_from_pandas.pdf")
pl.close()

########################################################################################################################
