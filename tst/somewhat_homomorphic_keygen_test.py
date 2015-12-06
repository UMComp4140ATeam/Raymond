#!/bin/python

import numpy
import test_utils
import unittest

from src import somewhat_homomorphic_keygen

class SomewhatHomomorphicKeygenTest(unittest.TestCase):
    def test_keygen(self):
        self.maxDiff = None
        # Need to reduce odd modulus check for tests so object initialization doesn't through errors
        somewhat_homomorphic_keygen.simple_error_distribution.MIN_ODD_MODULUS = 0
        
        keygen = somewhat_homomorphic_keygen.SomewhatHomomorphicKeygen(2, 1, 2, 4)
        keygen.set_error_distribution(test_utils.DeterministicErrorDistribution())
        keygen.set_random_vector_generator(test_utils.DeterministicVectorGenerator())
        
        secret_key, eval_key, public_key = keygen.generate_keys()
        
        # Make sure the secret key is correct
        self.assertEqual([0, 3], secret_key.tolist())
        # Ensure that the eval key is correct
        self.assertEqual({
            (1, 0, 0, 0): ([1, 2], 7), 
            (1, 0, 0, 1): ([4, 0], 4), 
            (1, 0, 1, 0): ([2, 2], 12), 
            (1, 0, 1, 1): ([2, 3], 19),
            (1, 0, 2, 0): ([4, 2], 8),
            (1, 0, 2, 1): ([0, 3], 15),
            (1, 1, 1, 0): ([2, 4], 16), 
            (1, 1, 1, 1): ([3, 1], 11),
            (1, 1, 2, 0): ([1, 2], 10),
            (1, 1, 2, 1): ([4, 0], 6),
            (1, 2, 2, 0): ([2, 2], 8),
            (1, 2, 2, 1): ([2, 3], 13)
        }, eval_key)
        # Ensure that the public key is correct
        self.assertEqual([[2, 4], [3, 1], [4, 2], [0, 3]], public_key[0].tolist())
        self.assertEqual([[16], [16], [22], [8]], public_key[1].tolist())

if __name__=="__main__":
    print "SomewhatHomomorphicKeygen Tests"