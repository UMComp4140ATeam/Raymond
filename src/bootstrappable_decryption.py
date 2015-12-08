#!/bin/python

import bit_bootstrappable_decryption
import logging

class BootstrappableDecryption(object):
    def __init__(self, short_odd_modulus, log=logging.getLogger(__name__)):
        self.__log = log
        self.__log.info("Creating BoostrappableDecryption with odd_modulus={odd_mod}".format(odd_mod=short_odd_modulus))
        self.bit_decryption = bit_bootstrappable_decryption.BitBootstrappableDecryption(short_odd_modulus, log)
        
    def decrypt(self, ciphertext, secret_key):
        self.__log.debug("Decrypting Ciphertext Message with\nciphertexts={ciphertexts}\nsecret_key={skey}".format(ciphertexts=ciphertext, skey=secret_key))
        message = 0
        for ciphertext_bit in ciphertext:
            message <<= 1
            message |= self.bit_decryption.decrypt(ciphertext_bit, secret_key)
            self.__log.debug("Decrypted bit={bit}".format(bit=message & 1))
        self.__log.debug("Decrypted message={message}".format(message=message))
        return message
        
if __name__=="__main__":
    print "BootstrappableDecryption class"