#
# 3) Factorial function
#

########################################################################################################################

# Factorial function, takes in an integer n
# and returns the product up to that number
def fact(n):
    prod = 1
    for i in range(1, n+1, 1):
        prod *= i
    return prod

########################################################################################################################

# Declaring the array that we are going to use as number and results
numbers = []
n_fact = []

# Counting up to to ten with integers
for num in range(0, 11, 1):
    numbers.append(num)
    n_fact.append(fact(num))

# Printing the results
print("We have the following values:")
print(numbers)
print(n_fact)

########################################################################################################################
