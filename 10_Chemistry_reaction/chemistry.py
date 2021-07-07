
#
# 11) Chemistry reaction
#

########################################################################################################################
# Importing modules

import matplotlib.pyplot as pl  # Data visualization
pl.style.use("seaborn-paper")   # I just like this style

########################################################################################################################

# Function to compute the rate of change of the X solvent
def dx(a, b, x, y):
    return a - (b + 1) * x + y * x**2

# Function to compute the rate of change of the Y solvent
def dy(a, b, x, y):
    return b * x - y * x**2

# Defining the initial variation of the X solvent
delta_var = 0.2

# Time step to solve the problem, and how many iterations we want
delta_t = 0.01
n_max = 1000

########################################################################################################################

# Asking the user what the initial value of B should be
b_con = float(input("Initial B: "))

# We want to look at the change over time, so we need to create list to keep track of the changes
a_con = 1
x_con = [a_con + delta_var]
y_con = [b_con / a_con]
time = [0]

# We iterate for as many steps as were defined
for i in range(1, n_max+1, 1):

    # We compute the change in concentration for X and Y
    x_con.append( x_con[-1] + dx(a_con, b_con, x_con[-1], y_con[-1]) * delta_t )
    y_con.append( y_con[-1] + dy(a_con, b_con, x_con[-1], y_con[-1]) * delta_t )

    # And we keep track of the time at the iteration
    time.append( time[-1] + delta_t )

# Creating the figure
pl.figure(figsize=(12.8, 4.8))

# We create two figure side by side for easier display
pl.axes([0.07, 0.1, 0.4, 0.8])  # First one

pl.plot(time, x_con, color = "purple")

pl.title("Solvent X")
pl.xlabel("Time [s]")
pl.ylabel("Concentration")

pl.axes([0.57, 0.1, 0.4, 0.8])  # Second one

pl.plot(time, y_con, color = "teal")

pl.title("Solvent Y")
pl.xlabel("Time [s]")
pl.ylabel("Concentration")

# Saving and closing
pl.savefig("chemistry.pdf")
pl.close()

########################################################################################################################
