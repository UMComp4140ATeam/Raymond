#!/bin/python
# -*- coding: utf-8 -*-

import numpy
import unittest

from src import ciphertext
from src import dimension_modulus_reduction

class DimensionModulusReductionTests(unittest.TestCase):
    def test_dimension_modulus_reduction(self):
        eval_key = {
            (0, 0): (numpy.array([0, 1], dtype=numpy.integer), 1),
            (0, 1): (numpy.array([0, 0], dtype=numpy.integer), 1),
            (0, 2): (numpy.array([0, 1], dtype=numpy.integer), 0),
            (1, 0): (numpy.array([1, 1], dtype=numpy.integer), 1),
            (1, 1): (numpy.array([1, 1], dtype=numpy.integer), 0),
            (1, 2): (numpy.array([0, 1], dtype=numpy.integer), 1),
            (2, 0): (numpy.array([1, 0], dtype=numpy.integer), 0),
            (2, 1): (numpy.array([1, 0], dtype=numpy.integer), 0),
            (2, 2): (numpy.array([1, 1], dtype=numpy.integer), 1),
            (3, 0): (numpy.array([0, 0], dtype=numpy.integer), 0),
            (3, 1): (numpy.array([1, 1], dtype=numpy.integer), 0),
            (3, 2): (numpy.array([1, 0], dtype=numpy.integer), 1)
        }
        
        dim_mod_redux = dimension_modulus_reduction.DimensionModulusReduction(2, 3, 2, 5)
        long_ciphertext = ciphertext.Ciphertext(numpy.array([2, 1, 4]), 3, 0)
        
        resulting_ciphertext = dim_mod_redux.reduce_dimension_and_modulus(long_ciphertext, eval_key)
        
        self.assertEquals([0, 0], resulting_ciphertext.coefficient_vector.tolist())
        self.assertEquals(0, resulting_ciphertext.ciphertext)
        self.assertEquals(0, resulting_ciphertext.level)
        
    def test_dimnension_modulus_reduction_invalid_cipherttext(self):
        dim_mod_redux = dimension_modulus_reduction.DimensionModulusReduction(2, 3, 2, 5)
        invalid_ciphertext = ciphertext.Ciphertext(numpy.array([2, 1], dtype=numpy.integer), 1, 0)
        
        self.assertRaises(ValueError, dim_mod_redux.reduce_dimension_and_modulus, invalid_ciphertext, {})

if __name__=="__main__":
    print "DimensionModulusReduction Tests"