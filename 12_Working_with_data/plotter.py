#
# 12) Data plotter
#

########################################################################################################################
# Importing modules

import numpy as np
import matplotlib.pyplot as pl  # Data visualization
pl.style.use("seaborn-paper")   # I just like this style

########################################################################################################################

data = np.loadtxt("./data_1.dat")

print( data[:,1] )

pl.figure()

pl.plot(data[:,0], data[:,1])

pl.savefig("data.pdf")
pl.close()

########################################################################################################################
