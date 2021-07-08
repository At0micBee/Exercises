#
# 12) Data generator
#

########################################################################################################################
# Importing modules

import numpy as np

########################################################################################################################

# Prepparing the range of the data
x = np.linspace(-1, 2, 1250)

# Computing some stuff
s = np.sin(x)
c = np.cos(x)

# Opening a file to write the data
data = open("data_1.dat", "w+")

# Writing the data at each point
for i, val in enumerate(x):
    data.write("{v:<10.5f}{si:>10.5f}{co:>10.5f}\n".format(v = val, si =s[i], co =c[i]))

# Closing the file
data.close()

########################################################################################################################
