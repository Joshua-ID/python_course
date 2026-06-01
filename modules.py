# import math to use math functions
import random
import datetime
import math

x = 2.9
print(math.ceil(x))  # round up
print(math.floor(x))  # round down
print(round(x))  # round to nearest

# import datetime to use datetime functions

t = datetime.datetime.now()
print(t)
print(t.year)
print(t.month)
print(t.day)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)
print(t.timestamp(), 'timestamp')

# import random to use random functions

print(random.randint(0, 100))
