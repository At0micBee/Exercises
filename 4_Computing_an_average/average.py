#
# 4) Computing an average
#

########################################################################################################################

# The values defined in the exercise
v = [2.5, 3.2, 4.1, 0.8, 1.2, 2.4]

########################################################################################################################

# A function that sums the elements within a given list
def sum_list(ls):
    total = 0       # Initializing the counter value
    for x in ls:    # iterating through the items
        total += x  # Adding to the total
    return total    # Returning the total

# A function that computes the average of the  elements of a list
def average_list(ls):
    return sum_list(ls) / len(ls)

########################################################################################################################

# Printing the results of our function on the test list v
print("The sum of v is:", sum_list(v))
print("The average of v is:", average_list(v))

########################################################################################################################
