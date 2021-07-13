#
# 15) Dates
#

########################################################################################################################
# Importing modules

import numpy as np          # Math and arrays
import datetime as dt       # Date and time handling

########################################################################################################################
# Computing a delta based on two dates

# Explicit birthday date, very easily typed
birthday = dt.datetime(1996, 2, 9, 15, 0, 0)

# Getting the time at that moment
now = dt.datetime.now()

# Computing the time delta between these points
age = now - birthday

print("I am now: {} old".format(age))

########################################################################################################################
# Computing a date based on a date and a delta

# Defining a time span
delta = dt.timedelta(hours = 6)

# Computing the date and time at the defined delta
future = now + delta

print("{} from now, it will be {}".format(delta, future.time()))

########################################################################################################################
# Computing a delta based on two deltas

# Creating two delta
d_1 = dt.timedelta(hours = 6)
d_2 = dt.timedelta(days = 1)

# Computing the total
d_tot = d_1 + d_2

print("The duration of {} and {} is {}".format(d_1, d_2, d_tot))

########################################################################################################################
# Checking if dates are within a range

# Time span to check for
span = dt.timedelta(days = 365)

# Loading the data from the files
all_dates = np.loadtxt("./dates.dat", skiprows = 1, dtype = int)

# Creating an empty list
converted = []

# Going through the file and creating dates
for i, y in enumerate(all_dates[:,0]):
    converted.append(
        dt.datetime(
            y,
            all_dates[i,1],
            all_dates[i,2],
            all_dates[i,3],
            all_dates[i,4],
            all_dates[i,5]
        )
    )

# Printing the dates and checking their validity
for e in converted:
    if e > now - span and e <= now + span:
        print("{} is within {} of now!".format(e, span))

########################################################################################################################
