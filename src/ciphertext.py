#!/bin/python

"""
An immutable class to hold a ciphertext for the LWE fully homomorphic encryption scheme. It is immutable to ensure that if it was created in valid state
it remains in a valid state.
"""
class Ciphertext(tuple):
    def __new__(cls, coefficient_vector, ciphertext_vector, level):
        return tuple.__new__(cls, (coefficient_vector, ciphertext, level))
    
    @property
    def coefficient_vector(self):
        return self[0]
        
    @property
    def ciphertext(self):
        return self[1]
        
    @property
    def level(self):
        return self[2]
        
    def __str__(self):
        return "<Ciphertext coef:{0} ciphertext:{1} level:{2}>".format(self.coefficient_vector, self.ciphertext, self.level)
        
    def __setattr__(self, *args):
        return NotImplemented
        
    def __delattr__(self, *args):
        return NotImplemented


if __name__=="__main__":
    print "Ciphertext Class"