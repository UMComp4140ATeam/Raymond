#!/bin/python

import math
import numpy
import simple_error_distribution
import somewhat_homomorphic_keygen
import rvg

class BootstrappableKeygen(object):
    def __init__(self, short_dimension, long_dimension, multiplicative_depth, short_odd_modulus, long_odd_modulus, matrix_rows, short_seed=1, long_seed=1):
        self.__short_dimension = short_dimension
        self.__long_dimension = long_dimension
        self.__multiplicative_depth = multiplicative_depth
        self.__short_odd_modulus = short_odd_modulus
        self.__long_odd_modulus = long_odd_modulus
        
        self.__short_error_distribution = simple_error_distribution.SimpleErrorDistribution(short_odd_modulus, short_seed)
        self.__short_random_vector_generator = rvg.RVG(short_dimension, short_odd_modulus, short_seed)
        
        self.__sh_keygen = somewhat_homomorphic_keygen.SomewhatHomomorphicKeygen(long_dimension, multiplicative_depth, long_odd_modulus, matrix_rows, long_seed)
        
    def set_short_error_distribution(self, new_short_error_distribution):
        self.__short_error_distribution = new_short_error_distribution
        
    def set_short_random_vector_generator(self, new_short_random_vector_generator):
        self.__short_random_vector_generator = new_short_random_vector_generator
        
    def set_sh_keygen(self, sh_keygen):
        self.__sh_keygen = sh_keygen
        
    def generate_keys(self):
        secret_key, eval_key, public_key = self.__sh_keygen.generate_keys()
        
        short_secret_key, short_eval_key = self.__generate_short_keys(secret_key)
        
        return short_secret_key, (eval_key, short_eval_key), public_key
        
    def __generate_short_keys(self, secret_key):
        short_secret_key = [vector for vector in self.__short_random_vector_generator.generate()][0]
        short_eval_key = {}
        for i in range(self.__long_dimension+1):
            tau = 0
            for coefficient_vector in self.__short_random_vector_generator.generate(int(math.log(self.__long_odd_modulus, 2)) + 1):
                error = self.__short_error_distribution.sample_distribution()
                
                key_element = 1
                if i != 0:
                    key_element = secret_key[i-1]
                    
                b = (coefficient_vector.dot(short_secret_key) + error + int(round(float(self.__short_odd_modulus)/self.__long_odd_modulus) * 2 ** tau * key_element)) % self.__short_odd_modulus
                
                short_eval_key[(i, tau)] = (coefficient_vector.tolist(), b)
                
                tau += 1
       
        return short_secret_key, short_eval_key
            

if __name__=="__main__":
    print "BootstrappableKeygen"