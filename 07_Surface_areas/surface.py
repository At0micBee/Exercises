#
# 7) Surface areas
#

########################################################################################################################
# Importing modules

import numpy as np
import matplotlib.pyplot as pl  # Data visualization
pl.style.use("seaborn-paper")   # I just like this style

########################################################################################################################

# Computes the area of a circle given its radius
def area_circle(radius):
    return np.pi * radius**2

# Computes the are of a square given its side
def area_square(side):
    return side**2

########################################################################################################################

# The prescribed range is 
values = np.linspace(0, 2, 1000)

circle = area_circle(values)    # Associated circle areas
square = area_square(values)    # Associated square areas

########################################################################################################################

pl.figure()

pl.plot(values, circle, color = "purple", label = "$\pi r^{2}$")
pl.plot(values, square, color = "teal", label = "$a^{2}$")

pl.title("Comparing the surfaces")
pl.xlabel("Radius / side")
pl.ylabel("Surface")

pl.legend(loc = "best")

pl.savefig("areas.pdf")
pl.close()

########################################################################################################################
