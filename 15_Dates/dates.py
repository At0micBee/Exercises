#
# 15) Dates
#

########################################################################################################################
# Importing modules

import datetime as dt       # Date and time handling

########################################################################################################################

# Explicit birthday date, very easily typed
birthday = dt.datetime(1996, 2, 9, 15, 0, 0)

# Getting the time at that moment
now = dt.datetime.now()

# Computing the time delta between these points
age = now - birthday

print("I am now: {} old".format(age))

########################################################################################################################

# Defining a time span
delta = dt.timedelta(hours = 6)

# Computing the date and time at the defined delta
future = now + delta

print("{} from now, it will be {}".format(delta, future.time()))

########################################################################################################################
