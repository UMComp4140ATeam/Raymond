#!/bin/python

import ciphertext
import math
import numpy

class HomomorphicArithmetic(object):
    def __init__(self, dimension, odd_modulus):
        self.__dimension = dimension
        self.__odd_modulus = odd_modulus
        
    def homomorphic_add(self, ciphertexts):
        if len(ciphertexts) == 0:
            return None
        
        v_add = numpy.zeros(self.__dimension, dtype=numpy.integer)
        w_add = 0
        level = ciphertexts[0].level
        for curr_ciphertext in ciphertexts:
            if level != curr_ciphertext.level:
                raise ValueError("{ciphertext} did not have a multiplication level that matched {level}.".format(ciphertext=curr_ciphertext, level=level))
            v_add = v_add + curr_ciphertext.coefficient_vector
            w_add = w_add + curr_ciphertext.ciphertext
        
        return ciphertext.Ciphertext(v_add, w_add, level)

    def homomorphic_multiply(self, ciphertext1, ciphertext2, evaluation_key):
        h = self.__create_h_dictionary(ciphertext1, ciphertext2)
        v_mult = numpy.zeros(self.__dimension, dtype=numpy.integer)
        w_mult = 0
        if ciphertext1.level != ciphertext2.level:
            raise ValueError("Levels of ciphertexts ({ciphertext1}, {ciphertext2}) do not match).".format(ciphertext1=ciphertext1, ciphertext2=ciphertext2))
        level = ciphertext1.level + 1
            
        for j in range(self.__dimension+1):
            for i in range(j+1):
                for tau in range(int(math.log(self.__odd_modulus, 2)) + 1):
                    v_mult += h[i, j, tau] * evaluation_key[level, i, j, tau][0]
                    w_mult += h[i, j, tau] * evaluation_key[level, i, j, tau][1]
        return ciphertext.Ciphertext(v_mult, w_mult, level)
        
    def __create_h_dictionary(self, ciphertext1, ciphertext2):
        h = {}
        for j in range(self.__dimension+1):
            for i in range(j+1):
                coefficient_c1 = self.__get_coefficient_value_from_ciphertext(ciphertext1, i)
                coefficient_c2 = self.__get_coefficient_value_from_ciphertext(ciphertext2, j)
                
                # Making the assumption that the negative are not used since the bits of the value are used and no max int is specified. However,
                # it may be the case that the value is mod q(odd modulus). Will try if this way does not work.
                hij = coefficient_c1 * coefficient_c2
                for tau in range(int(math.log(self.__odd_modulus, 2)) + 1):
                    h[i, j, tau] = hij & 1
                    hij >>= 1
        return h

    def __get_coefficient_value_from_ciphertext(self, ciphertext, index):
        if index == 0:
            return ciphertext.ciphertext
        return ciphertext.coefficient_vector[index-1]

if __name__=="__main__":
    print "HomomorphicArithmetic functions"