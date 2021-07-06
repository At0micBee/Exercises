#
# 9) Gravity complicated
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
