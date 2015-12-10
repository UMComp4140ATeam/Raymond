#!/bin/python

import numpy
import unittest

from src import bit_encrypter

curr_vector = 0
num_vectors = 1
vectors = 0

class MockRVG(object):
    def __init__(self, *args):
        pass

    def generate(self):
        return self
        
    def __iter__(self):
        return self
        
    def next(self):
        global curr_vector
        to_return = vectors[curr_vector]
        curr_vector = (curr_vector + 1) % num_vectors
        return to_return

class BitEncrypterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.oldrvg = bit_encrypter.rvg.RVG
        bit_encrypter.rvg.RVG = MockRVG
        
        cls.A = numpy.array([[2, 1, 3, 5], [0, 1, 2, 0], [3, 0, 4, 4], [1, 1, 1, 2], [0, 3, 2, 1]], dtype=numpy.integer)
        cls.b = numpy.array([[1, 2, 3, 4, 5]], dtype=numpy.integer).T
        
    @classmethod
    def tearDownClass(cls):
        bit_encrypter.rvg.RVG = cls.oldrvg
    
    def test_encrypt_bit(self):
        global curr_vector, num_vectors, vectors
        r = numpy.array([1, 0, 1, 0, 1], dtype=numpy.integer)
        curr_vector = 0
        vectors = [r]
        num_vectors = 1
        
        resulting_ciphertext = bit_encrypter.BitEncrypter(self.A, self.b, 1, 5)
        
        self.assertEqual([0, 4, 4, 0], resulting_ciphertext.coefficient_vector.T.tolist())
        self.assertEqual(0, resulting_ciphertext.ciphertext)
        self.assertEqual(0, resulting_ciphertext.level)
        
    def test_message_encrypt(self):
        global curr_vector, num_vectors, vectors
        r = [
            numpy.array([1, 0, 1, 0, 1], dtype=numpy.integer),
            numpy.array([1, 0, 0, 0, 1], dtype=numpy.integer),
            numpy.array([0, 0, 0, 1, 1], dtype=numpy.integer),
            numpy.array([0, 1, 1, 0, 0], dtype=numpy.integer)
        ]
        curr_vector = 0
        vectors = r
        num_vectors = 4
        
        resulting_ciphertexts = bit_encrypter.MessageEncrypter(self.A, self.b, 0xb, 5)
        
        self.assertEqual(4, len(resulting_ciphertexts))
        self.assertEqual([0, 4, 4, 0], resulting_ciphertexts[0].coefficient_vector.T.tolist())
        self.assertEqual(0, resulting_ciphertexts[0].ciphertext)
        self.assertEqual([2, 4, 0, 1], resulting_ciphertexts[1].coefficient_vector.T.tolist())
        self.assertEqual(1, resulting_ciphertexts[1].ciphertext)
        self.assertEqual([1, 4, 3, 3], resulting_ciphertexts[2].coefficient_vector.T.tolist())
        self.assertEqual(0, resulting_ciphertexts[2].ciphertext)
        self.assertEqual([3, 1, 1, 4], resulting_ciphertexts[3].coefficient_vector.T.tolist())
        self.assertEqual(1, resulting_ciphertexts[3].ciphertext)
        
if __name__=="__main__":
    print "BitEncrypter tests"