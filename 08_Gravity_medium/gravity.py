#
# 8) Gravity medium
#

########################################################################################################################
# Importing modules

import numpy as np              # Math and arrays
import matplotlib.pyplot as pl  # Data visualization
pl.style.use("seaborn-paper")   # I just like this style

########################################################################################################################
# Defining constants and functions

m_sun = 1.989e30        # Mass of the Sun :: kg
m_earth = 5.972e24      # Mass of the Earth :: kg
au = 150e9              # 1 AU = 150e9 m
g_grav = 6.674e-11      # Gravitational constant :: m3.kg-1.s-2

# Force of gravity between two objects of given mass
# The distance needs ot be given in m!!
def gravity(r):
    return g_grav * m_sun * m_earth / r**2

########################################################################################################################

# Defining the distance array, and computing the associated gravity force
distance = np.linspace(0.3 * au, 5 * au, 100)
force = gravity(distance)

# Plotting the results
pl.figure()

pl.plot(distance, force, color = "purple")

pl.title("Gravitational force")
pl.xlabel("Distance [m]")
pl.ylabel("Force [N]")

pl.savefig("force.pdf")
pl.close()

########################################################################################################################
