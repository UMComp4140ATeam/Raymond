#!/bin/python
# -*- coding: utf-8 -*-

import unittest

from src import homomorphic_encryption_scheme

def add_then_mult(arithmetic, ciphertexts, evaluation_key):
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
    
    return [level_2_c1, level_2_c2]

class BoostrappableEncryptionSchemeExperiments(unittest.TestCase):
    '''
    This test executes the two add then multiply circuit on the messages 11 and 2.
    
    On multiple runs this will not always pass.
    '''
    def test_add_then_mult_low_params(self):
        message1 = 11
        message2 = 2
        
        encryption_scheme = homomorphic_encryption_scheme.HomomorphicEncryptionScheme(2, 4, 1, 3, 5, 6)
        
        secret_key, evaluation_keys, public_key = encryption_scheme.keygen()
        
        ciphertext1 = encryption_scheme.encrypt(public_key, message1)
        ciphertext2 = encryption_scheme.encrypt(public_key, message2)

        ciphertexts = ciphertext1
        ciphertexts.extend(ciphertext2)
        
        resulting_ciphertexts = encryption_scheme.evaluate(add_then_mult, ciphertexts, evaluation_keys)
        
        message = encryption_scheme.decrypt(secret_key, resulting_ciphertexts)
        
        self.assertEquals(1, message)
        
    def test_add_then_mult_higher_params(self):
        message1 = 11
        message2 = 2
        
        encryption_scheme = homomorphic_encryption_scheme.HomomorphicEncryptionScheme(3, 16, 1, 7, 23, 30)
        
        secret_key, evaluation_keys, public_key = encryption_scheme.keygen()
        
        ciphertext1 = encryption_scheme.encrypt(public_key, message1)
        ciphertext2 = encryption_scheme.encrypt(public_key, message2)
        
        ciphertexts = ciphertext1
        ciphertexts.extend(ciphertext2)
        
        resulting_ciphertexts = encryption_scheme.evaluate(add_then_mult, ciphertexts, evaluation_keys)
        
        message = encryption_scheme.decrypt(secret_key, resulting_ciphertexts)
        
        self.assertEquals(1, message)
    
    '''
    This test takes the messages m0=19 and m0=26 as input. In the first layer it performs has 4 add gates and 2 multiplication gates. In the second layer is has 1 add gate and 2 multiplication gates.
    Messages are each 5 bits long mi0 indicates the MSbit and mi4 the LSbit
    Layer 1:
    Addition: c10 = add(m00, m03, m04), c11 = add(m01, m02), c12 = add(m10, m11, m13), c13 = add(m12, m13)
    Multiply: c0 = mult(c10, c11), c1 = mult(c12, c13)
    
    Layer 2:
    Addition: c2 = add(c0, c1)
    Multiply: mult(c1, c2), mult(c0, c2)
    
    Result is 10 or 2
    '''
    def test_multi_layer(self):
        message1 = 19
        message2 = 26
        
        encryption_scheme = homomorphic_encryption_scheme.HomomorphicEncryptionScheme(2, 4, 2, 3, 5, 6)
        
        secret_key, evaluation_key, public_key = encryption_scheme.keygen()
        
        ciphertext1 = encryption_scheme.encrypt(public_key, message1)
        ciphertext2 = encryption_scheme.encrypt(public_key, message2)
        
        ciphertexts = ciphertext1
        ciphertexts.extend(ciphertext2)
        
        resulting_ciphertexts = encryption_scheme.evaluate(multi_layer, ciphertexts, evaluation_key)
        
        message = encryption_scheme.decrypt(secret_key, resulting_ciphertexts)
        
        self.assertEquals(2, message)
        
if __name__=="__main__":
    print "BoostrappableEncryptionScheme Experiments"