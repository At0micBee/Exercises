#
# 9) Infinite series
#

########################################################################################################################
# Importing modules

import numpy as np
import matplotlib.pyplot as pl  # Data visualization
pl.style.use("seaborn-paper")   # I just like this style

########################################################################################################################

def term(n):
    return 4 * (-1)**n / (2 * n + 1)

########################################################################################################################

# Defining the maximum number of steps
n_max = 100

index = []      # Index of each terms
terms = []      # The corresponding terms

s = 0           # The value to compute the sum at each step
total = []      # Saving the total after each step

# Creating a loop up to the n_max value
for i in range(0, n_max+1, 1):
    # Adding the index of operation
    index.append(i)

    # Computing the term and adding it to the list
    t = term(i)
    terms.append(t)

    # Computing the sum and saving it for each step
    s += t
    total.append(s)

# Plotting the results
pl.figure()

pl.plot(index, total)

pl.title("Sum after $n$ steps")
pl.xlabel("Steps")
pl.ylabel("Sum value")

pl.savefig("series_evolution_pi.pdf")
pl.close()

pl.figure()

pl.plot(index, terms)

pl.title("Terms at each steps")
pl.xlabel("Steps")
pl.ylabel("Terms value")

pl.savefig("series_terms_pi.pdf")
pl.close()

########################################################################################################################
