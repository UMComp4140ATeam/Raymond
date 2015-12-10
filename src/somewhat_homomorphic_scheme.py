#!/bin/python
# -*- coding: utf-8 -*-

import bit_encrypter
import somewhat_homomorphic_keygen
import bootstrappable_decryption
import dimension_modulus_reduction
import homomorphic_arithmetic
import logging

class SomewhatHomomorphicEncryptionScheme(object):
    def __init__(self, dimension, multiplicative_depth, odd_modulus, matrix_rows, short_seed=1, long_seed=1, log=logging.getLogger(__name__)):
        self.__log = log
        self.__log.debug("Contructing Somewhat Homomorphic Encryption Scheme with\ndimension={dim}, multiplicative_depth={mult_depth}, odd_modulus={odd_mod}, matrix_rows={rows}".format(dim=dimension, mult_depth=multiplicative_depth, odd_mod=odd_modulus, rows=matrix_rows))
        self.__keygen = somewhat_homomorphic_keygen.SomewhatHomomorphicKeygen(dimension, multiplicative_depth, odd_modulus, matrix_rows, long_seed, log)
        self.__decrypt_alg = bootstrappable_decryption.BootstrappableDecryption(odd_modulus, log)
        self.__homomorphic_arithmetic = homomorphic_arithmetic.HomomorphicArithmetic(dimension, odd_modulus, log)
        self.__odd_modulus = odd_modulus
        
    def encrypt(self, public_key, message):
        return bit_encrypter.MessageEncrypter(public_key[0], public_key[1], message, self.__odd_modulus, log=self.__log)
        
    def decrypt(self, secret_key, ciphertexts):
        return self.__decrypt_alg.decrypt(ciphertexts, secret_key)
        
    def keygen(self):
        return self.__keygen.generate_keys()
        
    def evaluate(self, function, ciphertexts, evaluation_key):
        resulting_ciphertexts = function(self.__homomorphic_arithmetic, ciphertexts, evaluation_key)
        return resulting_ciphertexts
       
if __name__=="__main__":
    print "SomewhatHomomorphicEncryptionScheme class"