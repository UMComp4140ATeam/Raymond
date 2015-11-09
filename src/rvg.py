#!/bin/python

import math
import random
import numpy

'''
A simple random vector generator. It is initialized with n, q, and seed. To generate vectors call generate with count being the number of vectors that are wanted. If generate is not specified a count it assumes 1 and gives 1 vector as output.
'''
class RVG(object):
    def __init__(self, n, q, seed):
        self.seed = seed
        self.n = n #number of dimensions
        self.q = q #some large number?

    def generate(self, count=1):
        random.seed(self.seed)
        for i in range(0, count):
            v = numpy.ndarray(self.n, dtype=numpy.integer)
            for j in range(0, self.n):
                v[j] = random.randint(0, self.q)
            yield v

