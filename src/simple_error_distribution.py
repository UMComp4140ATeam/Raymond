#!/bin/python
import math
import random

MIN_ODD_MODULUS = 1000

'''
A simple error distribution class. That returns a small error relative to the odd modulus. This is a temporary class
that will be used until we have time to look into making a better error distribution.
'''
class SimpleErrorDistribution(object):
    def __init__(self, odd_modulus, seed=1):
        if odd_modulus < MIN_ODD_MODULUS:
            raise ValueError("Odd modulus {0} is too small for error distribution.".format(odd_modulus))
        # If q is sufficiently large, log(q) should be small enough for our max error
        self.__max_rand = int(math.log(odd_modulus))
        # Uses os.urandom function which, according to the documentation, is cryptographically secure
        self.__random_generator = random.SystemRandom(seed)

    def sample_distribution(self):
        return self.__random_generator.randint(0, self.__max_rand)

if __name__=="__main__":
    print "SimpleErrorDistribution class"
