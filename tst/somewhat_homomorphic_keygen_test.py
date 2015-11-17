#!/bin/python

import numpy
import unittest

from src import somewhat_homomorphic_keygen

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

class SomewhatHomomorphicKeygenTest(unittest.TestCase):
    def test_keygen(self):
        # Need to reduce odd modulus check for tests so object initialization doesn't through errors
        somewhat_homomorphic_keygen.simple_error_distribution.MIN_ODD_MODULUS = 0
        
        keygen = somewhat_homomorphic_keygen.SomewhatHomomorphicKeygen(2, 1, 2, 4)
        keygen.set_error_distribution(DeterministicErrorDistribution())
        keygen.set_random_vector_generator(DeterministicVectorGenerator())
        
        secret_key, eval_key, public_key = keygen.generate_keys()
        
        # Make sure the secret key is correct
        self.assertEqual([0, 3], secret_key.tolist())
        # Ensure that the eval key is correct
        self.assertEqual([[[1, 2], 22], [[4, 0], 34], [[2, 2], 16], [[2, 3], 27], [[2, 4], 16], [[3, 1], 11]], eval_key.tolist())
        # Ensure that the public key is correct
        self.assertEqual([[4, 2], [0, 3], [1, 2], [4, 0]], public_key[0].tolist())
        self.assertEqual([[20], [8], [10], [18]], public_key[1].tolist())

if __name__=="__main__":
    print "SomewhatHomomorphicKeygen Tests"