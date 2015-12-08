#!/bin/python
# -*- coding: utf-8 -*-

import bit_encrypter
import bootstrappable_keygen
import bootstrappable_decryption
import dimension_modulus_reduction
import homomorphic_arithmetic

class HomomorphicEncryptionScheme(object):
    def __init__(self, short_dimension, long_dimension, multiplicative_depth, short_odd_modulus, long_odd_modulus, matrix_rows, short_seed=1, long_seed=1):
        self.__keygen = bootstrappable_keygen.BootstrappableKeygen(short_dimension, long_dimension, multiplicative_depth, short_odd_modulus, long_odd_modulus, matrix_rows, short_seed, long_seed)
        self.__decrypt_alg = bootstrappable_decryption.BootstrappableDecryption(short_odd_modulus)
        self.__dimension_modulus_reduction = dimension_modulus_reduction.DimensionModulusReduction(short_dimension, long_dimension, short_odd_modulus, long_odd_modulus)
        self.__homomorphic_arithmetic = homomorphic_arithmetic.HomomorphicArithmetic(long_dimension, long_odd_modulus)
        
    def encrypt(self, public_key, message):
        return bit_encrypter.MessageEncrypter(public_key[0], public_key[1], message)
        
    def decrypt(self, secret_key, ciphertexts):
        return self.__decrypt_alg.decrypt(ciphertexts, secret_key)
        
    def keygen(self):
        return self.__keygen.generate_keys()
        
    def evaluate(self, function, ciphertexts, evaluation_keys):
        # Temporary, will substitute in other scheme when it is complete
        reduced_ciphertexts = []
        resulting_ciphertexts = function(self.__homomorphic_arithmetic, ciphertexts, evaluation_keys[0])
        for ciphertext in resulting_ciphertexts:
            reduced_ciphertexts.append(self.__dimension_modulus_reduction.reduce_dimension_and_modulus(ciphertext, evaluation_keys[1]))
        return reduced_ciphertexts
       
if __name__=="__main__":
    print "HomomorphicEncryptionScheme class"