#
# 16) Database with pandas
#

########################################################################################################################
# Importing modules

import os                       # OS operations
import pandas as pd             # Dataframes functionalities
import matplotlib.pyplot as pl  # Data visualization
pl.style.use("seaborn-paper")   # I just like this style

########################################################################################################################

# Creating a dictionary to hold the data from each file
data = {}

# Iterating through the input folder
for root, dirs, files in os.walk("./data/"):
    for file in files:
        # Parsing the file content to a dataframe
        data[file] = pd.read_table(root + file, sep = "\s+")

# Creating a figure
pl.figure()

# Setting the scale types of each axis
pl.xscale("log")
pl.yscale("log")

# Going through the loaded data and plotting it
for file, d in data.items():
    pl.plot(d["Wavelength"], d["Intensity"], label = file)

# Displaying info
pl.legend()
pl.title("Mie scattering")
pl.xlabel("Wavelength")
pl.ylabel("Intensity")

# Saving and closing
pl.savefig("./mie.pdf")
pl.close()

########################################################################################################################
