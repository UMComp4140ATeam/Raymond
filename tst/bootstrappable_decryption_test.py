#!/bin/python

import numpy
import unittest

from src import bootstrappable_decryption

class BootstrappableDecryption(unittest.TestCase):
    def test_decrypt(self):
        v1 = numpy.array([0, 0, 1, 3])
        w1 = 0
        
        v2 = numpy.array([1, 2, 4, 3])
        w2 = 3
        
        v3 = numpy.array([2, 3, 0, 1])
        w3 = 2
        
        v4 = numpy.array([1, 1, 3, 2])
        w4 = 4
        
        secret_key = numpy.array([2, 0, 4, 1])
        decryption_alg = bootstrappable_decryption.BootstrappableDecryption(5)
        
        message = decryption_alg.decrypt([(v1, w1), (v2, w2), (v3, w3), (v4, w4)], secret_key)
        self.assertEqual(9, message)

if __name__=="__main__":
    print "BootstrappableDecryption Tests"