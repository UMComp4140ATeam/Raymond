#!/bin/python

import numpy
import test_utils
import unittest

from src import bootstrappable_keygen

class MockSomewhatHomomorphicKeygen(object):
    def generate_keys(self):
        return numpy.array([1, 2, 3, 4]), numpy.array([[4, 3], [1, 0]]), None

class BootstrappableKeygenTest(unittest.TestCase):
    def test_keygen(self):
        bootstrappable_keygen.somewhat_homomorphic_keygen.simple_error_distribution.MIN_ODD_MODULUS = 0
        keygen = bootstrappable_keygen.BootstrappableKeygen(2, 4, 1, 2, 2, 4)
        keygen.set_sh_keygen(MockSomewhatHomomorphicKeygen())
        keygen.set_short_error_distribution(test_utils.DeterministicErrorDistribution())
        keygen.set_short_random_vector_generator(test_utils.DeterministicVectorGenerator())
        
        secret_key, eval_keys, public_keys = keygen.generate_keys()
        
        # Make sure the secret_key is correct
        self.assertEqual([4, 2], secret_key.tolist())
        
        # Make sure the first eval_key is the eval key returned by the somewhat homomorphic keygen
        self.assertEqual([[4, 3], [1, 0]], eval_keys[0].tolist())
        
        # Make sure the short eval key is correct
        self.assertEqual([[[0, 3], 1], [[1, 2], 1], [[4, 0], 1], [[2, 2], 1], [[2, 3], 1], [[2, 4], 0], [[3, 1], 0], [[4, 2] ,1]], eval_keys[1].tolist())
        

if __name__=="__main__":
    print "BootstrappableKeygen Tests"