#!/bin/python

import bit_bootstrappable_decryption

class BootstrappableDecryption(object):
    def __init__(self, short_odd_modulus):
        self.bit_decryption = bit_bootstrappable_decryption.BitBootstrappableDecryption(short_odd_modulus)
        
    def decrypt(self, ciphertext, secret_key):
        message = 0
        for ciphertext_bit in ciphertext:
            message <<= 1
            message |= self.bit_decryption.decrypt(ciphertext_bit, secret_key)
        return message
        
if __name__=="__main__":
    print "BootstrappableDecryption class"