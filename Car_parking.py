# There's a car parking with 13 parking spaces
# Tom and Mary randomly choose two parking spaces
# Code calculates the probability that there's at least 2 free parking spaces between Tom and Mary

import random

purpose = 0
for i in range(10000):
    places = range(13)
    tom = places.pop(random.choice(range(len(places))))
    mary = places.pop(random.choice(range(len(places))))
    if abs(tom - mary) >= 2: purpose +=1
print purpose/10000.0
