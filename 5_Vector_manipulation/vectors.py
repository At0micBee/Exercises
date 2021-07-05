
#
# 5) Vector manipulation
#

########################################################################################################################

# Defining the vectors as in the text
v1 = [0.2, 1.3, 7.4]
v2 = [-7.1, 2.4, -0.7]

# Declaring the empty list to store our results
v_add = []      # For the addition
v_tot = []      # For the addition of scaled values
v_rot = []      # For the curl
product = 0     # For the dot product

# Iterating through the values to do the computation
# Using enumerate to access both the value and the index
for idx, value in enumerate(v1):
    # Addition
    v_add.append(value + v2[idx])

    # Scalar multiplication and addition of results
    v_tot.append(2 * value - 3 * v2[idx])

    # Computing the scalar product
    product += value * v2[idx]

    # Computing the curl
    v_rot.append( v1[(idx + 1) % len(v1)] * v2[(idx + 2) % len(v1)] - v2[(idx + 1) % len(v1)] * v1[(idx + 2) % len(v1)] )

# Printing the results
print("Addition of v1 and v2:", v_add)
print("Addition of the multiplied vectors:", v_tot)
print("The scalar product of v1 and v2 is:", product)
print("The curl of v1 and v2 is:", v_rot)

########################################################################################################################

# The curl product is more complicated to automatize, so here is a direct way to do it
# Visualizing the method might help you understand what is going on in the loop
v_rot_s = []

x = v1[1] * v2[2] - v2[1] * v1[2]
y = v1[2] * v2[0] - v2[2] * v1[0]
z = v1[0] * v2[1] - v2[0] * v1[1]

v_rot_s.append(x)
v_rot_s.append(y)
v_rot_s.append(z)

print("Simpler curl implementation says also:", v_rot_s)

########################################################################################################################
