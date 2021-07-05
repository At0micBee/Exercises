#
# 1) Polynomial coefficients
#

########################################################################################################################
# Importing modules

import numpy as np              # Math and arrays
import matplotlib.pyplot as pl  # Data visualization
pl.style.use("seaborn-paper")   # I just like this style

########################################################################################################################

# Defining functions

# Polynomial of order 2
#
# a: amplitude of the function
# b: center of the gaussian
# c: width of the gaussian
def poly(a, b, c, x):
    return a * x**2 + b * x + c

########################################################################################################################

axis = np.linspace(-5, 5, 1000)     # Creating the x axis to evaluate the function

a_tests = np.linspace(-1, 1, 5)     # Creating the test values for the a coefficient

# Fixing the values for b and c coefficients
fixed_b = 1
fixed_c = 2

pl.figure()                                         # Creating a figure

# Creating a loop through the values of a
for a in a_tests:
    y = poly(a, fixed_b, fixed_c, axis)             # Computing the values of the polynomial
    pl.plot(axis, y, label = "a = {}".format(a))    # Plotting the results

pl.legend(loc = "best")                             # Adding a legend to the figure
pl.xlabel("Abscise")                                # Adding a label to the x axis of the plot
pl.ylabel("Value")                                  # Adding a label to the y axis of the plot
pl.title("$ax^2 + x + 2$")                          # Adding a title to the plot

pl.savefig("polynomial_a.pdf")                      # Saving the figure to a pdf
pl.close()                                          # Closing the figure

########################################################################################################################

b_tests = np.linspace(-1, 1, 5)     # Creating the test values for the a coefficient

# Fixing the values for a and c coefficients
fixed_a = 1
fixed_c = 2

pl.figure()                                         # Creating a figure

# Creating a loop through the values of a
for b in b_tests:
    y = poly(fixed_a, b, fixed_c, axis)             # Computing the values of the polynomial
    pl.plot(axis, y, label = "b = {}".format(b))    # Plotting the results

pl.legend(loc = "best")                             # Adding a legend to the figure
pl.xlabel("Abscise")                                # Adding a label to the x axis of the plot
pl.ylabel("Value")                                  # Adding a label to the y axis of the plot
pl.title("$x^2 + bx + 2$")                          # Adding a title to the plot

pl.savefig("polynomial_b.pdf")                      # Saving the figure to a pdf
pl.close()                                          # Closing the figure

########################################################################################################################

c_tests = np.linspace(-1, 1, 5)     # Creating the test values for the a coefficient

# Fixing the values for a and b coefficients
fixed_a = 1
fixed_b = 2

pl.figure()                                         # Creating a figure

# Creating a loop through the values of a
for c in c_tests:
    y = poly(fixed_a, fixed_b, c, axis)             # Computing the values of the polynomial
    pl.plot(axis, y, label = "c = {}".format(c))    # Plotting the results

pl.legend(loc = "best")                             # Adding a legend to the figure
pl.xlabel("Abscise")                                # Adding a label to the x axis of the plot
pl.ylabel("Value")                                  # Adding a label to the y axis of the plot
pl.title("$x^2 + 2x + c$")                          # Adding a title to the plot

pl.savefig("polynomial_c.pdf")                      # Saving the figure to a pdf
pl.close()                                          # Closing the figure

########################################################################################################################