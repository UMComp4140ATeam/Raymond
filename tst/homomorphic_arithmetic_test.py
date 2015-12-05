#!/bin/python

import numpy
import unittest

from src import ciphertext
from src import homomorphic_arithmetic

class HomomorphicArithmeticTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dimension = 3
        cls.ciphertexts = [
            ciphertext.Ciphertext(numpy.array([1, 2, 3], dtype=numpy.integer), 1, 0),
            ciphertext.Ciphertext(numpy.array([3, 2, 1], dtype=numpy.integer), 2, 0),
            ciphertext.Ciphertext(numpy.array([1, 1, 1], dtype=numpy.integer), 1, 0)
        ]

    def test_homomorphic_add_empty_list(self):
        self.assertIsNone(homomorphic_arithmetic.homomorphic_add(self.dimension, []))

    def test_homomorphic_add_single_ciphertext(self):
        resulting_ciphertext = homomorphic_arithmetic.homomorphic_add(self.dimension, [self.ciphertexts[0]])

        self.assertEquals(self.ciphertexts[0].coefficient_vector.tolist(), resulting_ciphertext.coefficient_vector.tolist())
        self.assertEquals(self.ciphertexts[0].ciphertext, resulting_ciphertext.ciphertext)
        self.assertEquals(self.ciphertexts[0].level, resulting_ciphertext.level)

    def test_homomorphic_add_multiple_ciphertexts(self):
        resulting_ciphertext = homomorphic_arithmetic.homomorphic_add(self.dimension, self.ciphertexts)

        self.assertEquals([5, 5, 5], resulting_ciphertext.coefficient_vector.tolist())
        self.assertEquals(4, resulting_ciphertext.ciphertext)
        self.assertEquals(0, resulting_ciphertext.level)

    def test_homomorphic_add_different_levels(self):
        self.assertRaises(ValueError, homomorphic_arithmetic.homomorphic_add, 3, [self.ciphertexts[0], ciphertext.Ciphertext(numpy.array([1, 1, 1], dtype=numpy.integer), 1, 1)])

    def test_homomorphic_add_different_dimensions(self):
        self.assertRaises(ValueError, homomorphic_arithmetic.homomorphic_add, 3, [ciphertext.Ciphertext(numpy.array([1, 1, 2, 1], dtype=numpy.integer), 1, 0)])

if __name__=="__main__":
    print "HomomorphicArithmetic Tests"
