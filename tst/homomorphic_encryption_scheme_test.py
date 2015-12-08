#!/bin/python
# -*- coding: utf-8 -*-

import unittest

from src import homomorphic_encryption_scheme

def test_function(arithmetic, ciphertexts, evaluation_key):
    output_c1 = arithmetic.homomorphic_add(ciphertexts[0:4])
    output_c2 = arithmetic.homomorphic_add(ciphertexts[4:])
    final_output = arithmetic.homomorphic_multiply(output_c1, output_c2, evaluation_key)
    
    return [final_output]

class HomomorphicEncryptionSchemeTest(unittest.TestCase):
    @unittest.skip("Testing without bootstrapping")
    def test_integration_simple_full_encrypt_and_evaluate(self):
        message1 = 11
        message2 = 2
        
        encryption_scheme = homomorphic_encryption_scheme.HomomorphicEncryptionScheme(2, 4, 1, 3, 5, 6)
        
        secret_key, evaluation_keys, public_key = encryption_scheme.keygen()
        
        ciphertext1 = encryption_scheme.encrypt(public_key, message1)
        ciphertext2 = encryption_scheme.encrypt(public_key, message2)
        #print ciphertext1, ciphertext2
        ciphertexts = ciphertext1
        ciphertexts.extend(ciphertext2)
        
        resulting_ciphertexts = encryption_scheme.evaluate(test_function, ciphertexts, evaluation_keys)
        
        message = encryption_scheme.decrypt(secret_key, resulting_ciphertexts)
        
        self.assertEquals(1, message)
        
if __name__=="__main__":
    print "HomomorphicEncryptionScheme Tests"