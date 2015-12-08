#!/bin/python
# -*- coding: utf-8 -*-

import ciphertext
import math
import numpy

class DimensionModulusReduction(object):
    def __init__(self, short_dimension, long_dimension, short_modulus, long_modulus):
        self.__short_dimension = short_dimension
        self.__long_dimension = long_dimension
        self.__short_modulus = short_modulus
        self.__long_modulus = long_modulus
        
    def reduce_dimension_and_modulus(self, long_ciphertext, short_eval_key):
        if len(long_ciphertext.coefficient_vector) != self.__long_dimension:
            raise ValueError("Error: Ciphertext's coefficient vector length ({length}) did not match the long dimension ({long_dimension})".format(length=len(long_ciphertext.coefficient_vector), long_dimension=self.__long_dimension))
    
        bit_coefficient_dict = self.__create_bit_coefficient_dictionary(long_ciphertext)
        v_short = numpy.zeros(self.__short_dimension, dtype=numpy.integer)
        m_short = 0
        for i in range(self.__long_dimension + 1):
            for tau in range(int(math.log(self.__long_modulus, 2))+1):
                v_short += 2 * bit_coefficient_dict[i, tau] * short_eval_key[i, tau][0]
                m_short += 2 * bit_coefficient_dict[i, tau] * short_eval_key[i, tau][1]
        v_short %= self.__short_modulus
        m_short %= self.__short_modulus
        # We set level to 0 because it doesn't matter since this cannot be used in any more evaluations without being decrypted and re-encrypted
        return ciphertext.Ciphertext(v_short, m_short, 0)
        
    def __create_bit_coefficient_dictionary(self, long_ciphertext):
        h_dict = {}
        for i in range(self.__long_dimension + 1):
            value = long_ciphertext.ciphertext
            if i != 0:
                value = long_ciphertext.coefficient_vector[i-1]
                
            hi = (self.__long_modulus + 1) * value / 2
            for tau in range(int(math.log(self.__long_modulus, 2)) + 1):
                h_dict[i, tau] = hi & 1
                hi >>= 1
        return h_dict
    

if __name__=="__main__":
    print "DimensionModulusReduction Module"