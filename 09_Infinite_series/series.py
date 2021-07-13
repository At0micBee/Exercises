#
# 9) Infinite series
#

########################################################################################################################
# Importing modules

import numpy as np              # Math and arrays
import matplotlib.pyplot as pl  # Data visualization
pl.style.use("seaborn-paper")   # I just like this style

########################################################################################################################

# Defining the maximum number of steps
n_max = 1000000

index = []      # Index of each terms
terms = []      # The corresponding terms

s = 0           # The value to compute the sum at each step
total = []      # Saving the total after each step

# Creating a loop up to the n_max value
for i in range(1, n_max+1, 1):
    # Adding the index of operation
    index.append(i)

    # Adding the weight of the term to the list
    terms.append(1 / i)

    # Computing the sum and saving it for each step
    s += 1 / i
    total.append(s)

# Plotting the results
pl.figure()

pl.plot(index, total)

pl.title("Sum after $n$ steps")
pl.xlabel("Steps")
pl.ylabel("Sum value")

pl.savefig("series_evolution.pdf")
pl.close()

pl.figure()

# We can specify what type of axis to use, here I am using a log, to better
# represent the value as they shrink
pl.yscale("log")

pl.plot(index, terms)

pl.title("Terms at each steps")
pl.xlabel("Steps")
pl.ylabel("Terms value")

pl.savefig("series_terms.pdf")
pl.close()

########################################################################################################################
