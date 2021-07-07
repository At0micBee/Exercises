#
# 10) Gravity complicated
#

########################################################################################################################
# Importing modules

import numpy as np
import matplotlib.pyplot as pl  # Data visualization
pl.style.use("seaborn-paper")   # I just like this style

########################################################################################################################
# Defining some constants and function

r_earth = 6371e3        # Radius of Earth :: m
m_earth = 5.972e24      # Mass of Earth :: kg
g_grav = 6.674e-11      # Gravitational constant :: m3.kg-1.s-2

delta_t = 0.1           # Time step for integration :: s

# Computes the gravity above the surface of Earth at a given altitude z
#
# Units must be in SI to be consistent!
def get_grav(z):
    return -g_grav * m_earth / (r_earth + z)**2

########################################################################################################################
# Showing the change in gravity

altitude = np.linspace(0, 100e3, 1000)  # 1000 altitude points (in meters!!)
grav_var = get_grav(altitude)           # Computes the associated gravity :: m.s-2

pl.figure()

pl.plot(altitude, grav_var, color = "purple")

pl.xlabel("Altitude [m]")
pl.ylabel("Gravity [m.s$^{-2}$]")

pl.savefig("gravity_altitude.pdf")
pl.close()

########################################################################################################################

# Creating an array to keep track of the time
time = [0]

# Creating the velocity list, and we initialize it with a speed of 0
velocity = [0]

# Creating the position list, and we initialize it at and altitude of 100km
position = [100e3]

# Telling the program to compute until we cross the ground
while position[-1] > 0:

    # Computing the gravity at the altitude of the object
    g_alt = get_grav(position[-1])

    # Computing the velocity at next step, Euler explicit
    velocity.append(velocity[-1] + g_alt * delta_t)

    # Computing position at next step, Euler explicit
    position.append(position[-1] + velocity[-2] * delta_t)

    # Adding the step to the time list
    time.append(time[-1] + delta_t)

pl.figure()

# Don't worry about this, it's just to get the graph to fit
pl.axes([0.12, 0.1, 0.77, 0.8])

# Plotting the position over time
pl.plot(time, position, color = "purple", label = "Altitude")

# Showing when the object hits the ground
pl.axvline(time[-1], color = "black", dashes = [1, 1], label = "Impact: {:.3f}s".format(time[-1]))

# Displaying information
pl.title("Evolution during the fall")
pl.xlabel("Time [s]")
pl.ylabel("Altitude [m]")
pl.legend(loc = "lower left")

# Plotting on the right side to have a better scale
pl.twinx()

# Plotting the velocity over time
pl.plot(time, velocity, color = "teal", label = "Velocity")

# Displaying information
pl.ylabel("Velocity [m.s$^{-1}$]")
pl.legend(loc = "upper right")

# Saving and closing
pl.savefig("fall.pdf")
pl.close()

########################################################################################################################
