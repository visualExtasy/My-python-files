# Problem 3-1 from final exam of MIT's "Introduction to
# Computational Thinking and Data Science"

import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up,
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    for i in range(CURRENTRABBITPOP):
        prob_rabbit_repr = 1.0 - (float(CURRENTRABBITPOP)/MAXRABBITPOP)
        a = random.random()
        #if a > prob_rabbit_repr and CURRENTRABBITPOP > 10:
            #CURRENTRABBITPOP -= 1
        if a < prob_rabbit_repr and CURRENTRABBITPOP < 1000:
            CURRENTRABBITPOP += 1

def foxGrowth():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    for i in range(CURRENTFOXPOP):
        fox_win_prob = float(CURRENTRABBITPOP)/MAXRABBITPOP
        b = random.random()
        if b > fox_win_prob and CURRENTFOXPOP > 10:
            c = random.random()
            if c < 0.1: CURRENTFOXPOP -=1

        elif b < fox_win_prob and CURRENTRABBITPOP > 10:
            CURRENTRABBITPOP -= 1
            c = random.random()
            if c < (1/3.0): CURRENTFOXPOP +=1


def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations = []
    fox_populations = []
    # TO DO
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)


    pylab.plot(range(numSteps), rabbit_populations)
    pylab.plot(range(numSteps), fox_populations)
    pylab.show()
    return (rabbit_populations, fox_populations)


runSimulation(200)
"""
rabbit_populations, f_pop = runSimulation(200)
coeff = pylab.polyfit(range(len(rabbit_populations)), rabbit_populations, 2)
pylab.plot(polyval(coeff, range(len(rabbit_populations))))
pylab.show()
"""
