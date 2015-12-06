#!/bin/python

import ciphertext
import numpy

def homomorphic_add(dimension, ciphertexts):
    if len(ciphertexts) == 0:
        return None
    
    v_add = numpy.zeros(dimension, dtype=numpy.integer)
    w_add = 0
    level = ciphertexts[0].level
    for curr_ciphertext in ciphertexts:
        if level != curr_ciphertext.level:
            raise ValueError("{ciphertext} did not have a multiplication level that matched {level}.".format(ciphertext=curr_ciphertext, level=level))
        v_add = v_add + curr_ciphertext.coefficient_vector
        w_add = w_add + curr_ciphertext.ciphertext
    
    return ciphertext.Ciphertext(v_add, w_add, level)

def homomorphic_multiply(ciphertext1, ciphertext2):
    return None

if __name__=="__main__":
    print "HomomorphicArithmetic functions"