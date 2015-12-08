#!/bin/python

import numpy
import unittest

from src import evaluate
from src import ciphertext
from src import homomorphic_arithmetic


class EvaluateLayerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dimension = 3
        cls.odd_modulus = 5
        cls.ciphertexts = [
            ciphertext.Ciphertext(numpy.array([1, 2, 3], dtype=numpy.integer), 1, 0),
            ciphertext.Ciphertext(numpy.array([3, 2, 1], dtype=numpy.integer), 2, 0),
            ciphertext.Ciphertext(numpy.array([1, 1, 1], dtype=numpy.integer), 1, 0),
            ciphertext.Ciphertext(numpy.array([4, 1], dtype=numpy.integer), 2, 0),
            ciphertext.Ciphertext(numpy.array([0, 3], dtype=numpy.integer), 1, 0)
        ]

    def test_CreateADD(self):
        g0 = [0, 1]
        g1 = [1, 2]
        g2 = [0, 1, 2]
        l0 = evaluate.Layer([g0,g1,g2], 0)

        self.assertEquals(l0.isAdd(), True)
        self.assertEquals(l0.numOfGates(), 3)

    def test_CreateMULT(self):
        g3 = [0, 1]
        g4 = [0, 2]
        l1 = evaluate.Layer([g3, g4], 1) #mult

        self.assertEquals(l1.isAdd(), False)
        self.assertEquals(l1.numOfGates(), 2)


    def test_process_add(self):
        g0 = [0, 1]
        g1 = [1, 2]
        g2 = [0, 1, 2]
        l0 = evaluate.Layer([g0,g1,g2], 0)

        ret = l0.process(self.dimension, self.odd_modulus, self.ciphertexts)
        print ret
        self.assertEquals(len(ret), 3)
        #print "TEST ",  self.dimension

        self.assertEquals([5, 5, 5], ret[2].coefficient_vector.tolist())
        self.assertEquals(4, ret[2].ciphertext)
        self.assertEquals(0, ret[2].level)

    def test_process_mult(self):
        "process mult"

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
        g3 = [3, 4]
        g4 = [4, 3]
        l1 = evaluate.Layer([g3, g4], 1) #mult
        ret = l1.process(2, self.odd_modulus, self.ciphertexts, evaluation_key)
        print ret

        self.assertEquals([9, 12], ret[0].coefficient_vector.tolist())
        self.assertEquals(13, ret[0].ciphertext)
        self.assertEquals(1, ret[0].level)
"""
class EvaluateCircuitTest():
    def setup():
        g0 = [0, 1]
        g1 = [1, 2]
        g2 = [2, 3, 4]
        l0 = evaluate.Layer([g0,g1,g2], 0)

        g3 = [5, 1]
        g4 = [6, 7]
        l1 = evaluate.Layer([g3, g4], 1) #mult

        g5 = [8, 9]
        l2 = evaluate.Layer([g5], 0)

        evaluate.Circuit([l0, l1, l2])
"""

if __name__ == '__main__':
    print "Evaluate Tests"
