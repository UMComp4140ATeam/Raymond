#!/bin/python

import numpy
import unittest

from src import bit_bootstrappable_decryption

class BitBootstrappableDecryptionTest(unittest.TestCase):
    def test_decrypt(self):
        v = numpy.array([1, 1, 3, 2])
        w = 4
        secret_key = numpy.array([2, 0, 4, 1])
        decryption_alg = bit_bootstrappable_decryption.BitBootstrappableDecryption(5)
        
        message = decryption_alg.decrypt((v, w), secret_key)
        
        self.assertEqual(1, message)

if __name__=="__main__":
    print "BitBootstrappableDecryption Tests"