#!/bin/python

import logging
import math
import numpy
import simple_error_distribution
import rvg

'''
Generates the secret keys, the evaluation key, and the public key that will be used in the homomorphic encryption scheme.
'''
class SomewhatHomomorphicKeygen(object):
    def __init__(self, dimension, multiplicative_depth, odd_modulus, matrix_rows, seed=1, log=logging.getLogger(__name__)):
        self.__dimension = dimension
        self.__multiplicative_depth = multiplicative_depth
        self.__odd_modulus = odd_modulus
        self.__matrix_rows = matrix_rows
        
        self.__error_distribution = simple_error_distribution.SimpleErrorDistribution(odd_modulus, seed)    
        self.__random_vector_generator = rvg.RVG(dimension, odd_modulus, seed)
        self.__log = log
        
    def set_error_distribution(self, new_error_distribution):
        self.__error_distribution = new_error_distribution
        
    def set_random_vector_generator(self, new_random_vector_generator):
        self.__random_vector_generator = new_random_vector_generator
        
    def generate_keys(self):
        secret_keys = self.__generate_secret_key()
        evaluation_key = self.__generate_evaluation_key(secret_keys)
        public_key = self.__generate_public_key(secret_keys)
        return secret_keys[-1], evaluation_key, public_key
        
    def __generate_secret_key(self):
        self.__log.info("Generating Secret Keys")
        keys = [key for key in self.__random_vector_generator.generate(self.__multiplicative_depth + 1)]
        self.__log.debug("Generated secrect keys: {keys}".format(keys=keys))
        return keys
        
    def __generate_evaluation_key(self, secret_keys):
        self.__log.info("Generating Evaluation Key")
        evaluation_key = {}
        # Assume that 0 is not included because the b component of  the tuple is calculated using curr_depth - 1
        for curr_depth in range(1, self.__multiplicative_depth+1):
            for j in range(self.__dimension+1):
                for i in range(j + 1):
                    tau = 0
                    for coefficient_vector in self.__random_vector_generator.generate(int(math.log(self.__odd_modulus, 2)) + 1):
                        self.__log.debug("Generating Evaluation Key for level={level} i={i} j={j} tau={tau}".format(level=curr_depth, i=i, j=j, tau=tau))
                        self.__log.debug("Vector Generated = {vector}".format(vector=coefficient_vector))
                        error = self.__error_distribution.sample_distribution()
                        self.__log.debug("Error Generated = {error}".format(error=error))
                        
                        # Artifacts of the notations used, see start of section 2 of the paper right near the top of page 9. Don't ask me why this is used
                        # it is incredibly confusing.
                        # Note: These 1 values are also not used in the inner product
                        si = 1
                        if i != 0:
                            si = secret_keys[curr_depth-1][i-1]
                            
                        sj = 1
                        if j != 0:
                            sj = secret_keys[curr_depth-1][j-1]
                        
                        self.__log.debug("Calculating b. Inputs: cvector={cvector}, skey={skey}, error={error}, tau={tau}, si={si}, sj={sj}".format(cvector=coefficient_vector, skey=secret_keys[curr_depth], error=error, tau=tau, si=si, sj=sj))
                        b = (coefficient_vector.dot(secret_keys[curr_depth]) + 2 * error + 2**tau * si * sj) % self.__odd_modulus
                        # For now I will leave this as a list of tuples, may need to exchange for a dictionary indexed by the tuple (curr_depth, i, j, tau). Also
                        # because numpy is stupid and doesn't properly implement == we have to covert the coefficient_vector to a list
                        evaluation_key[(curr_depth, i, j, tau)] = (coefficient_vector, b)
                        self.__log.debug("Evaluation Key Entry={entry}".format(entry=(coefficient_vector, b)))
                        tau += 1
        return evaluation_key
        
    def __generate_public_key(self, secret_keys):
        self.__log.info("Generating Public Key")
        coefficient_vectors = []
        for vector in self.__random_vector_generator.generate(self.__matrix_rows):
            coefficient_vectors.append(vector)
        coefficient_matrix = numpy.matrix(coefficient_vectors)
        self.__log.debug("Coefficient Matrix={matrix}".format(matrix=coefficient_matrix))
        
        errors = []
        for i in range(self.__matrix_rows):
            errors.append(self.__error_distribution.sample_distribution())
        errors_matrix = numpy.matrix(errors).transpose()
        self.__log.debug("Errors={errors}".format(errors=errors_matrix))
        
        secret_key_vector = numpy.matrix(secret_keys[0]).transpose()
        b = numpy.mod(coefficient_matrix.dot(secret_key_vector) + 2 * errors_matrix, self.__odd_modulus)
        self.__log.debug("B={b}".format(b=b))
        return coefficient_matrix, b

if __name__=="__main__":
    print "SomewhatHomomorphicKeygen Class"