#
# 12) Data plotter
#

########################################################################################################################
# Importing modules

import numpy as np
import matplotlib.pyplot as pl  # Data visualization
pl.style.use("seaborn-paper")   # I just like this style

########################################################################################################################

# Defining the function that computes the exit angle
def get_angle(n1, n2, theta1):
    return np.arcsin(n1 * np.sin(theta1) / n2)

########################################################################################################################

# Loading the N-BK7 data from the file
data = np.loadtxt("./N-BK7.dat", skiprows = 1)

# Creating a figure to show n and k evolution
pl.figure()

pl.plot(data[:,0], data[:,1], color = "purple")

pl.xlabel("Wavelength [$\lambda$]")
pl.ylabel("n (purple)")
pl.title("n, k indexes for N-BK7")

pl.twinx()
pl.plot(data[:,0], data[:,2], color = "teal")

pl.ylabel("k (blue)")

pl.savefig("data.pdf")
pl.close()

########################################################################################################################

# Defining the incident angle and n1 value
theta_incident = np.deg2rad(30)
n_air = 1.0

# Computing the exit angle of the beam depending on the wavelength
exit_angle = get_angle(n_air, data[:,1], theta_incident)

# Creating a figure to illustrate the variation
pl.figure()

pl.plot(data[:,0], np.rad2deg(exit_angle), color = "firebrick")

pl.title(r"Exit angle ($n_{air}=1$, $\theta_1$ = 30°)")
pl.xlabel("Wavelength [µm]")
pl.ylabel("Angle [deg]")

pl.savefig("exit_angle.pdf")
pl.close()

########################################################################################################################