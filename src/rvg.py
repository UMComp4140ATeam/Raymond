#!/bin/python

import math
import random
import numpy

'''
A simple random vector generator. It is initialized with n, q, and seed. To generate vectors call generate with count being the number of vectors that are wanted. If generate is not specified a count it assumes 1 and gives 1 vector as output.
'''
class RVG(object):
    def __init__(self, n, q, seed):
        self.__seed__ = seed
        self.__n__ = n #number of dimensions
        self.__q__ = q #some large number?
        self.__g__ = random.SystemRandom(self.__seed__)

    def generate(self, count=1):
        for i in range(0, count):
            v = numpy.ndarray(self.__n__, dtype=numpy.integer)
            for j in range(0, self.__n__):
                v[j] = self.__g__.randint(0, self.__q__) #% self.q #.randint(0, self.q)
            yield v
