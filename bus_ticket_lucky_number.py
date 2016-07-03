# Code calculates the probability that sum of the first 3 numbers
# of bus ticket is equal to the sum of the second 3 numbers
tickets = range(100000, 1000000)


lucky = 0
for x in tickets:
    y = str(x)
    lo = []
    for i in y:
        lo.append(int(i))
    if sum(lo[:3]) == sum(lo[3:]):
        lucky += 1
print 'Probability of lucky number is: ' + str(float(lucky)/len(tickets))
