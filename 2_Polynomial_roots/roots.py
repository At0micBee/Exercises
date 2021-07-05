#
# 2) Polynomial roots
#

########################################################################################################################
# Importing modules

import numpy as np              # Math and arrays

########################################################################################################################

# Computes the delta based on the given coefficients
def delta(a, b, c):
    return b**2 - 4 * a * c

########################################################################################################################

# Asking the user to input the values of the coefficients
a_in = float(input("a = "))
b_in = float(input("b = "))
c_in = float(input("c = "))

# Computing delta with the given input values
d = delta(a_in, b_in, c_in)

# Chaking all the possibilities
if d < 0:
    print("Delta =", d, "< 0, no real answers!")

elif d == 0:
    if a == 0:
        print("a = 0, cannot divide by 0!")
    else:
        x = -b_in / (2 * a_in)
        print("Delta =", d, "= 0, there is one root x =", x)
    
else:
    if a == 0:
        print("a = 0, cannot divide by 0!")
    else:
        x1 = (-b_in + np.sqrt(d)) / (2 * a_in)
        x2 = (-b_in - np.sqrt(d)) / (2 * a_in)
        print("Delta =", d, "> 0, there are two roots (x1, x2) =", x1, x2)
    
# Note how quickly if statements can get crowded! This example leaves the very heavy check on a
# twice to show how, if not careful, they can get out of hand and be complicated to understand.
#
# Try to be as clear as possible, and avoid nested if as much as you can!

########################################################################################################################
