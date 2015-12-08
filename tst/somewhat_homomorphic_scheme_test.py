#!/bin/python
# -*- coding: utf-8 -*-

import logging
import unittest

from src import somewhat_homomorphic_scheme

def test_function(arithmetic, ciphertexts, evaluation_key):
    output_c1 = arithmetic.homomorphic_add(ciphertexts[0:4])
    output_c2 = arithmetic.homomorphic_add(ciphertexts[4:])
    final_output = arithmetic.homomorphic_multiply(output_c1, output_c2, evaluation_key)
    
    return [final_output]

class SomewhatHomomorphicEncryptionSchemeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = logging.getLogger(__name__)
        cls.log.setLevel(logging.DEBUG)
        cls.log.addHandler(logging.FileHandler('somewhat_homomorphic_tests_output.log'))

    def test_integration_simple_full_encrypt_and_evaluate(self):
        message1 = 11
        message2 = 2
        
        # Have to be careful about the values for the parameters selected. If they are too low the scheme won't work
        encryption_scheme = somewhat_homomorphic_scheme.SomewhatHomomorphicEncryptionScheme(4, 1, 17, 16, log=self.log)
        
        secret_key, evaluation_key, public_key = encryption_scheme.keygen()
        
        ciphertext1 = encryption_scheme.encrypt(public_key, message1)
        ciphertext2 = encryption_scheme.encrypt(public_key, message2)
        
        ciphertexts = ciphertext1
        ciphertexts.extend(ciphertext2)
        
        resulting_ciphertexts = encryption_scheme.evaluate(test_function, ciphertexts, evaluation_key)
        
        message = encryption_scheme.decrypt(secret_key, resulting_ciphertexts)
        
        self.assertEquals(1, message)
        
if __name__=="__main__":
    print "SomewhatHomomorphicEncryptionScheme Tests"