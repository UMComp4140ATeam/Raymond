#!/bin/python

import numpy
import somewhat_homomorphic_keygen
import unittest

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
    
    def generate(self, count=1):
        for i in range(count):
            yield vectors[count % len(vectors)]
            
class DeterministicErrorDistribution(object):
    errors = [0, 1, 1, 1, 0, 0]
    
    def __init__(self):
        self.__index = 0
    
    def sample_distribution(self):
        result = self.errors[self.__index]
        self.__index = (self.__index + 1) % len(self.errors)
        return result

class SomewhatHomomorphicKeygenTest(unittest.TestCase):
    def test_keygen(self):
        keygen = somewhat_homomorphic_keygen.SomewhatHomomorphicKeygen(2, 1, 2, 4, seed=1, error_distribution=DeterministicErrorDistribution(), random_vector_generator=DeterministicVectorGenerator())
        secret_key, eval_key, public_key = keygen.generate_keys()
        # Make sure the secret key is correct
        self.assertEqual([0, 3], secrect_key.tolist())

if __name__=="__main__":
    print "SomewhatHomomorphicKeygen Tests"