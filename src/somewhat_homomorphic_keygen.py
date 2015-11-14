#!/bin/python

import math
import numpy
import simple_error_distribution
import rvg

'''
Generates the secret keys, the evaluation key, and the public key that will be used in the homomorphic encryption scheme.
'''
class SomewhatHomomorphicKeygen(object):
    def __init__(self, dimension, multiplicative_depth, odd_modulus, matrix_rows, seed=1, error_distribution=None, random_vector_generator=None):
        self.__dimension = dimension
        self.__multiplicative_depth = multiplicative_depth
        self.__odd_modulus = odd_modulus
        self.__matrix_rows = matrix_rows
        self.__error_distribution = error_distribution
        if error_distribution is None:
            self.__error_distribution = simple_error_distribution.SimpleErrorDistribution(odd_modulus, seed)
            
        self.random_vector_generator = random_vector_generator
        if random_vector_generator is None:
            self.__random_vector_generator = rvg.RVG(dimension, odd_modulus, seed)
            
    def generate_keys(self):
        secret_keys = self.__generate_secret_keys()
        evaluation_key = self.__generate_evaluation_key(secret_keys)
        public_key = self.__generate_public_key(secret_keys)
        return secret_keys[-1], evaluation_key, public_key
        
    def __generate_secret_key(self):
        return [key for key in self.random_vector_generator.generate(self.__multiplicative_depth + 1)]
        
    def __generate_evaluation_key(self, secret_keys):
        evaluation_key = []
        # Assume that 0 is not included because the b component of  the tuple is calculated using curr_depth - 1
        for curr_depth in range(1, self.__multiplicative_depth+1):
            # Paper states to include n as an index to check. This would cause an index out of bounds error, so I'm assuming it was an error in the paper..
            for j in range(self._dimension):
                for i in range(j + 1):
                    tau = 0
                    for coefficient_vector in self.__random_vector_generator.generate(int(math.log(self.__odd_modulus)) + 1):
                        error = self.__error_distribution.sample_distribution()
                        b = coefficient_vector.dot(secret_keys[curr_depth]) + 2 * error + 2**tau * secret_keys[curr_depth-1][i] * secret_keys[curr_depth-1][j]
                        # For now I will leave this as a list of tuples, may need to exchange for a dictionary indexed by the tuple (curr_depth, i, j, tau)
                        evaluation_key.append((coefficient_vector, b))
        return evaluation_key
        
    def __generate_public_key(self, secret_keys):
        coefficient_vectors = []
        for vector in self.__random_vector_generator.generate(self.__matrix_rows):
            coefficient_vectors.append(vector)
        coefficient_matrix = numpy.matrix(coefficient_vectors)
        
        errors = []
        for i in range(self.__matrix_rows):
            errors.append(self.__error_distribution.sample_distribution())
        errors_matrix = numpy.matrix(errors).transpose()
        
        secret_key_vector = numpy.matrix(secret_keys[0]).transpose()
        b = coefficient_matrix.dot(secret_key_vector) + 2 * errors_matrix
        return coefficient_matrix, b

if __name__=="__main__":
    print "SomewhatHomomorphicKeygen Class"