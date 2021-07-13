#
# Modifies the database file to a simple column file
# Not relevant for the exercise itself
#

########################################################################################################################

import numpy as np

data = np.loadtxt("./N-BK7.csv", skiprows = 1, delimiter = ',')

new = open("N-BK7.dat", "w+")

new.write("{w:<12}{n:>17}{k:>17}\n".format(w = "Wavelength", n = 'n', k = 'k'))

for i, wave in enumerate(data[:,0]):
    new.write("{w:<12.4e}{n:>17.8e}{k:>17.8e}\n".format(w = wave, n = data[i,1], k = data[i,2]))

new.close()