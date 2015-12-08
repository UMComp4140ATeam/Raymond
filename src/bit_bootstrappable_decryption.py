#!/bin/python

import logging

class BitBootstrappableDecryption(object):
    def __init__(self, short_odd_modulus, log=logging.getLogger(__name__)):
        self.__log = log
        self.__log.info("Creating BitBootstrappableDecryption with odd_modulus={odd_mod}".format(odd_mod=short_odd_modulus))
        self.__short_odd_modulus = short_odd_modulus
        
    def decrypt(self, ciphertext, secret_key):
        self.__log.debug("Decrypting ciphertext={ciphertext} with secrect_key={secret_key}".format(ciphertext=ciphertext, secret_key=secret_key))
        return ((ciphertext[1] - ciphertext[0].dot(secret_key)) % self.__short_odd_modulus) % 2

if __name__=="__main__":
    print "BitBootstrappableDecryption class"