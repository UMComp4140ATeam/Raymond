#!/bin/python

import numpy
import unittest

from src import ciphertext
from src import homomorphic_arithmetic

class HomomorphicArithmeticTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dimension = 3
        cls.odd_modulus = 5
        cls.ciphertexts = [
            ciphertext.Ciphertext(numpy.array([1, 2, 3], dtype=numpy.integer), 1, 0),
            ciphertext.Ciphertext(numpy.array([3, 2, 1], dtype=numpy.integer), 2, 0),
            ciphertext.Ciphertext(numpy.array([1, 1, 1], dtype=numpy.integer), 1, 0)
        ]
    def test_homomorphic_add_empty_list(self):
        arithmetic = homomorphic_arithmetic.HomomorphicArithmetic(self.dimension, self.odd_modulus)
        self.assertIsNone(arithmetic.homomorphic_add([]))

    def test_homomorphic_add_single_ciphertext(self):
        arithmetic = homomorphic_arithmetic.HomomorphicArithmetic(self.dimension, self.odd_modulus)
        resulting_ciphertext = arithmetic.homomorphic_add([self.ciphertexts[0]])

        self.assertEquals(self.ciphertexts[0].coefficient_vector.tolist(), resulting_ciphertext.coefficient_vector.tolist())
        self.assertEquals(self.ciphertexts[0].ciphertext, resulting_ciphertext.ciphertext)
        self.assertEquals(self.ciphertexts[0].level, resulting_ciphertext.level)

    def test_homomorphic_add_multiple_ciphertexts(self):
        arithmetic = homomorphic_arithmetic.HomomorphicArithmetic(self.dimension, self.odd_modulus)
        resulting_ciphertext = arithmetic.homomorphic_add(self.ciphertexts)
        
        self.assertEquals([0, 0, 0], resulting_ciphertext.coefficient_vector.tolist())
        self.assertEquals(4, resulting_ciphertext.ciphertext)
        self.assertEquals(0, resulting_ciphertext.level)

    def test_homomorphic_add_different_levels(self):
        arithmetic = homomorphic_arithmetic.HomomorphicArithmetic(self.dimension, self.odd_modulus)
        self.assertRaises(ValueError, arithmetic.homomorphic_add, [self.ciphertexts[0], ciphertext.Ciphertext(numpy.array([1, 1, 1], dtype=numpy.integer), 1, 1)])

    def test_homomorphic_add_different_dimensions(self):
        arithmetic = homomorphic_arithmetic.HomomorphicArithmetic(self.dimension, self.odd_modulus)
        self.assertRaises(ValueError, arithmetic.homomorphic_add, [ciphertext.Ciphertext(numpy.array([1, 1, 2, 1], dtype=numpy.integer), 1, 0)])

    def test_homomorphic_multi(self):
        evaluation_key = {
            (1, 0, 0, 0): (numpy.array([1, 1], dtype=numpy.integer), 1),
            (1, 0, 0, 1): (numpy.array([0, 2], dtype=numpy.integer), 2),
            (1, 0, 0, 2): (numpy.array([1, 2], dtype=numpy.integer), 3),
            (1, 0, 1, 0): (numpy.array([4, 0], dtype=numpy.integer), 0),
            (1, 0, 1, 1): (numpy.array([3, 1], dtype=numpy.integer), 1),
            (1, 0, 1, 2): (numpy.array([3, 2], dtype=numpy.integer), 1),
            (1, 1, 1, 0): (numpy.array([0, 1], dtype=numpy.integer), 2),
            (1, 1, 1, 1): (numpy.array([0, 0], dtype=numpy.integer), 0),
            (1, 1, 1, 2): (numpy.array([1, 4], dtype=numpy.integer), 4),
            (1, 0, 2, 0): (numpy.array([2, 4], dtype=numpy.integer), 1),
            (1, 0, 2, 1): (numpy.array([3, 3], dtype=numpy.integer), 3),
            (1, 0, 2, 2): (numpy.array([1, 0], dtype=numpy.integer), 0),
            (1, 1, 2, 0): (numpy.array([2, 1], dtype=numpy.integer), 1),
            (1, 1, 2, 1): (numpy.array([1, 3], dtype=numpy.integer), 4),
            (1, 1, 2, 2): (numpy.array([1, 2], dtype=numpy.integer), 3),
            (1, 2, 2, 0): (numpy.array([4, 4], dtype=numpy.integer), 1),
            (1, 2, 2, 1): (numpy.array([0, 1], dtype=numpy.integer), 4),
            (1, 2, 2, 2): (numpy.array([2, 2], dtype=numpy.integer), 1)
        }

        ciphertext1 = ciphertext.Ciphertext(numpy.array([4, 1], dtype=numpy.integer), 2, 0)
        ciphertext2 = ciphertext.Ciphertext(numpy.array([0, 3], dtype=numpy.integer), 1, 0)

        arithmetic = homomorphic_arithmetic.HomomorphicArithmetic(2, self.odd_modulus)
        resulting_ciphertext = arithmetic.homomorphic_multiply(ciphertext1, ciphertext2, evaluation_key)

        self.assertEquals([4, 2], resulting_ciphertext.coefficient_vector.tolist())
        self.assertEquals(3, resulting_ciphertext.ciphertext)
        self.assertEquals(1, resulting_ciphertext.level)

    def test_homomorphic_multi_different_levels(self):
        ciphertext1 = ciphertext.Ciphertext(numpy.array([4, 1], dtype=numpy.integer), 2, 0)
        ciphertext2 = ciphertext.Ciphertext(numpy.array([0, 3], dtype=numpy.integer), 1, 1)

        arithmetic = homomorphic_arithmetic.HomomorphicArithmetic(2, self.odd_modulus)
        self.assertRaises(ValueError, arithmetic.homomorphic_multiply, ciphertext1, ciphertext2, {})

if __name__=="__main__":
    print "HomomorphicArithmetic Tests"
