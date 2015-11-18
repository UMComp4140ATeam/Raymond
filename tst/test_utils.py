#!/bin/python

import numpy

class DeterministicVectorGenerator(object):
    vectors = [
        numpy.array([4, 2]),
        numpy.array([0, 3]),
        numpy.array([1, 2]),
        numpy.array([4, 0]),
        numpy.array([2, 2]),
        numpy.array([2, 3]),
        numpy.array([2, 4]),
        numpy.array([3, 1])
    ]
    
    def __init__(self):
        self.__curr_index = 0
    
    def generate(self, count=1):
        for i in range(count):
            yield self.vectors[self.__curr_index]
            self.__curr_index = (self.__curr_index + 1) % len(self.vectors)
            
class DeterministicErrorDistribution(object):
    errors = [0, 1, 1, 1, 0, 0]
    
    def __init__(self):
        self.__index = 0
    
    def sample_distribution(self):
        result = self.errors[self.__index]
        self.__index = (self.__index + 1) % len(self.errors)
        return result

if __name__=="__main__":
    print "Test Utilities"