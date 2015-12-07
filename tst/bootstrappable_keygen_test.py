#!/bin/python

import numpy
import test_utils
import unittest

from src import bootstrappable_keygen

class MockSomewhatHomomorphicKeygen(object):
    def generate_keys(self):
        return numpy.array([1, 2, 3, 4], dtype=numpy.integer), {(0, 0): [4, 3], (0, 1): [1, 0], (1, 0): [2, 1], (1, 1): [3, 0]}, None

class BootstrappableKeygenTest(unittest.TestCase):
    def test_keygen(self):
        bootstrappable_keygen.somewhat_homomorphic_keygen.simple_error_distribution.MIN_ODD_MODULUS = 0
        keygen = bootstrappable_keygen.BootstrappableKeygen(2, 4, 1, 2, 2, 4)
        keygen.set_sh_keygen(MockSomewhatHomomorphicKeygen())
        keygen.set_short_error_distribution(test_utils.DeterministicErrorDistribution())
        keygen.set_short_random_vector_generator(test_utils.DeterministicVectorGenerator())
        
        secret_key, eval_keys, public_keys = keygen.generate_keys()
        
        # Have to convertt eval_keys because numpy is dumb. See other somewhat homomorphic keygen test for longer explaination as to why.
        eval_keys = (eval_keys[0], {key: (value[0].tolist(), value[1]) for key, value in eval_keys[1].iteritems()})
        
        # Make sure the secret_key is correct
        self.assertEqual([4, 2], secret_key.tolist())
        
        # Make sure the first eval_key is the eval key returned by the somewhat homomorphic keygen
        self.assertEqual({
            (0, 0): [4, 3],
            (0, 1): [1, 0],
            (1, 0): [2, 1],
            (1, 1): [3, 0]
        }, eval_keys[0])
        
        # Make sure the short eval key is correct
        self.assertEqual({
            (0, 0): ([0, 3], 1), 
            (0, 1): ([1, 2], 1), 
            (1, 0): ([4, 0], 0), 
            (1, 1): ([2, 2], 1), 
            (2, 0): ([2, 3], 0), 
            (2, 1): ([2, 4], 0), 
            (3, 0): ([3, 1], 1), 
            (3, 1): ([4, 2] ,1),
            (4, 0): ([0, 3], 1),
            (4, 1): ([1, 2], 1)
        }, eval_keys[1])
        

if __name__=="__main__":
    print "BootstrappableKeygen Tests"