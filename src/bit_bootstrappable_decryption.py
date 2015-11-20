#!/bin/python

class BitBootstrappableDecryption(object):
    def __init__(self, short_odd_modulus):
        self.__short_odd_modulus = short_odd_modulus
        
    def decrypt(self, ciphertext, secret_key):
        return ((ciphertext[1] - ciphertext[0].dot(secret_key)) % self.__short_odd_modulus) % 2

if __name__=="__main__":
    print "BitBootstrappableDecryption class"