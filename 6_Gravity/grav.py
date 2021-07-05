#
# 6) Gravity
#

########################################################################################################################
# Importing modules

import numpy as np              # Math and arrays
import matplotlib.pyplot as pl  # Data visualization
pl.style.use("seaborn-paper")   # I just like this style

########################################################################################################################

# Earth gravity
g = 9.81

# Setting the axis for the time
time = np.linspace(0, 10, 1000)

# To give an example of the usefulness of the numpy module, we use the properties of the arrays to very easily
# obtain the results by multiplying them by a scalar directly.

# Computing the velocity and position
vel = g * time
pos = (g / 2) * time**2

########################################################################################################################
# Plotting the results

# Creating a figure
pl.figure()

# Plotting the velocity
pl.plot(time, vel, color = "teal", label = "Velocity")

# Giving info on the figure
pl.xlabel("Time [s]")
pl.ylabel("Velocity [m.s$^{-1}$]")
pl.legend(loc = "upper left")

# Flipping the axis to plot on the right side
pl.twinx()

# Plotting the position
pl.plot(time, pos, color = "purple", label = "Position")

# More info on the figure
pl.ylabel("Position [m]")
pl.legend(loc = "lower right")

# Saving the figure and closing it
pl.savefig("gravity.pdf")
pl.close()

########################################################################################################################
