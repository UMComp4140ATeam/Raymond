#!/bin/python

import unittest

from src import somewhat_homomorphic_scheme

def add_then_multiply(arithmetic, ciphertexts, evaluation_key):
    output_c1 = arithmetic.homomorphic_add(ciphertexts[0:4])
    output_c2 = arithmetic.homomorphic_add(ciphertexts[4:])
    final_output = arithmetic.homomorphic_multiply(output_c1, output_c2, evaluation_key)
    
    return [final_output]
    
def multi_layer(arithmetic, ciphertexts, evaluation_key):
    output_c1 = arithmetic.homomorphic_add([ciphertexts[0], ciphertexts[3], ciphertexts[4]])
    output_c2 = arithmetic.homomorphic_add([ciphertexts[1], ciphertexts[2]])
    output_c3 = arithmetic.homomorphic_add([ciphertexts[5], ciphertexts[6], ciphertexts[8]])
    output_c4 = arithmetic.homomorphic_add([ciphertexts[7], ciphertexts[8]])
    
    level_1_c1 = arithmetic.homomorphic_multiply(output_c1, output_c2, evaluation_key)
    level_1_c2 = arithmetic.homomorphic_multiply(output_c3, output_c4, evaluation_key)
    level_1_c3 = arithmetic.homomorphic_add([level_1_c1, level_1_c2])
    
    level_2_c1 = arithmetic.homomorphic_multiply(level_1_c3, level_1_c2, evaluation_key)
    level_2_c2 = arithmetic.homomorphic_multiply(level_1_c1, level_1_c3, evaluation_key)
    
class SomewhatHomomorphicExperimentation(unittest.TestCase):
    '''
    This test executes the two add then multiply circuit on the messages 11 and 2.
    
    On multiple runs this will not always pass.
    '''
    def test_two_add_then_multiply_low_parameters(self):
        message1 = 11
        message2 = 2
        
        encryption_scheme = somewhat_homomorphic_scheme.SomewhatHomomorphicEncryptionScheme(3, 1, 7, 15)
        
        secret_key, evaluation_key, public_key = encryption_scheme.keygen()
        
        ciphertext1 = encryption_scheme.encrypt(public_key, message1)
        ciphertext2 = encryption_scheme.encrypt(public_key, message2)
        
        ciphertexts = ciphertext1
        ciphertexts.extend(ciphertext2)
        
        resulting_ciphertexts = encryption_scheme.evaluate(add_then_multiply, ciphertexts, evaluation_key)
        
        message = encryption_scheme.decrypt(secret_key, resulting_ciphertexts)
        
        self.assertEquals(1, message)
        
    def test_two_add_then_multiply_higher_parameters(self):
        message1 = 11
        message2 = 2
        
        encryption_scheme = somewhat_homomorphic_scheme.SomewhatHomomorphicEncryptionScheme(4, 1, 17, 25)
        
        secret_key, evaluation_key, public_key = encryption_scheme.keygen()
        
        ciphertext1 = encryption_scheme.encrypt(public_key, message1)
        ciphertext2 = encryption_scheme.encrypt(public_key, message2)
        
        ciphertexts = ciphertext1
        ciphertexts.extend(ciphertext2)
        
        resulting_ciphertexts = encryption_scheme.evaluate(add_then_multiply, ciphertexts, evaluation_key)
        
        message = encryption_scheme.decrypt(secret_key, resulting_ciphertexts)
        
        self.assertEquals(1, message)
        
if __name__=="__main__":
    print "Somewhat Homomorphic Encryption Scheme Experimentation"