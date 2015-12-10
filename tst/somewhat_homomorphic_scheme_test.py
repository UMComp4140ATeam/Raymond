#!/bin/python
# -*- coding: utf-8 -*-

import logging
import unittest

from src import somewhat_homomorphic_scheme

def test_add_then_multiply(arithmetic, ciphertexts, evaluation_key):
    output_c1 = arithmetic.homomorphic_add(ciphertexts[0:4])
    output_c2 = arithmetic.homomorphic_add(ciphertexts[4:])
    final_output = arithmetic.homomorphic_multiply(output_c1, output_c2, evaluation_key)
    
    return [final_output]
    
def test_add(arithmetic, ciphertexts, evaluation_key):
    output_c1 = arithmetic.homomorphic_add(ciphertexts)
    
    return [output_c1]
    
def test_mult(arithmetic, ciphertexts, evaluation_key):
    return [arithmetic.homomorphic_multiply(ciphertexts[0], ciphertexts[1], evaluation_key)]
    

class SomewhatHomomorphicEncryptionSchemeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = logging.getLogger(__name__)
        cls.log.setLevel(logging.DEBUG)
        cls.log.addHandler(logging.FileHandler('somewhat_homomorphic_tests_output.log', mode='w'))
        
    def test_integration_encrypt_then_decrypt(self):
        message = 1
        
        self.log.info("\nTest encrypt_then_decrypt\n")
        
        encryption_scheme = somewhat_homomorphic_scheme.SomewhatHomomorphicEncryptionScheme(2, 0, 13, 3, log=self.log)
        
        secret_key, evaluation_key, public_key = encryption_scheme.keygen()
        ciphertext = encryption_scheme.encrypt(public_key, message)
        returned_message = encryption_scheme.decrypt(secret_key, ciphertext)
        
        self.assertEquals(1, returned_message)
        
    def test_integration_simple_add(self):
        message1 = 1
        message2 = 1
        
        self.log.info("\nTest simple_add\n")
        
        encryption_scheme = somewhat_homomorphic_scheme.SomewhatHomomorphicEncryptionScheme(4, 0, 17, 5, log=self.log)
        secret_key, evaluation_key, public_key = encryption_scheme.keygen()
        
        ciphertext1 = encryption_scheme.encrypt(public_key, message1)
        ciphertext2 = encryption_scheme.encrypt(public_key, message2)
        
        ciphertexts = ciphertext1
        ciphertexts.extend(ciphertext2)
        
        resulting_ciphertexts = encryption_scheme.evaluate(test_add, ciphertexts, evaluation_key)
        
        message = encryption_scheme.decrypt(secret_key, resulting_ciphertexts)
        
        self.assertEquals(0, message)
        
    def test_integration_mutliple_add(self):
        message1 = 1
        message2 = 1
        message3 = 1
        message4 = 1
        
        self.log.info("\nTest simple_add\n")
        
        encryption_scheme = somewhat_homomorphic_scheme.SomewhatHomomorphicEncryptionScheme(4, 0, 17, 5, log=self.log)
        secret_key, evaluation_key, public_key = encryption_scheme.keygen()
        
        ciphertext1 = encryption_scheme.encrypt(public_key, message1)
        ciphertext2 = encryption_scheme.encrypt(public_key, message2)
        ciphertext3 = encryption_scheme.encrypt(public_key, message3)
        ciphertext4 = encryption_scheme.encrypt(public_key, message4)
        
        ciphertexts = ciphertext1
        ciphertexts.extend(ciphertext2)
        
        resulting_ciphertexts = encryption_scheme.evaluate(test_add, ciphertexts, evaluation_key)
        
        message = encryption_scheme.decrypt(secret_key, resulting_ciphertexts)
        
        self.assertEquals(0, message)
        
    def test_integration_simple_multiply(self):
        message1 = 1
        message2 = 1
        
        self.log.info("\nTest simple_mult\n")
        
        encryption_scheme = somewhat_homomorphic_scheme.SomewhatHomomorphicEncryptionScheme(2, 1, 7, 7, log=self.log)
        secret_key, evaluation_key, public_key = encryption_scheme.keygen()
        
        ciphertext1 = encryption_scheme.encrypt(public_key, message1)
        ciphertext2 = encryption_scheme.encrypt(public_key, message2)
        
        ciphertexts = ciphertext1
        ciphertexts.extend(ciphertext2)
        
        resulting_ciphertexts = encryption_scheme.evaluate(test_mult, ciphertexts, evaluation_key)
        
        message = encryption_scheme.decrypt(secret_key, resulting_ciphertexts)
        
        self.assertEquals(1, message)
        
    def test_integration_simple_full_encrypt_and_evaluate(self):
        message1 = 11
        message2 = 2
        
        self.log.info("\nTest simple_full_encrypt_and_evaluate\n")
        
        # Have to be careful about the values for the parameters selected. If they are too low the scheme won't work
        encryption_scheme = somewhat_homomorphic_scheme.SomewhatHomomorphicEncryptionScheme(4, 1, 13, 10, log=self.log)
        
        secret_key, evaluation_key, public_key = encryption_scheme.keygen()
        
        ciphertext1 = encryption_scheme.encrypt(public_key, message1)
        ciphertext2 = encryption_scheme.encrypt(public_key, message2)
        
        ciphertexts = ciphertext1
        ciphertexts.extend(ciphertext2)
        
        resulting_ciphertexts = encryption_scheme.evaluate(test_add_then_multiply, ciphertexts, evaluation_key)
        
        message = encryption_scheme.decrypt(secret_key, resulting_ciphertexts)
        
        self.assertEquals(1, message)
        
if __name__=="__main__":
    print "SomewhatHomomorphicEncryptionScheme Tests"