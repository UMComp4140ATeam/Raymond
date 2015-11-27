import numpy
import rvg
from ciphertext import CipherText

seed = 5684
def BitEncrypter(A, b, mbit):

    mbit = 1 & mbit # we only want a bit

    m0 = len(A)
    # r is probably not correct...
    r = numpy.ndarray([m0, 1], dtype=numpy.integer) #generate random vector r<-{0,1}^m?
    s = rvg.RVG(m0, 1, seed)
    sp = s.generate()
    sp = next(sp)
    r[:, 0] = sp[:] & 1

    v = A.T*r
    w = b.T*r + mbit

    return Ciphertext(v, w, 0)

def MessageEncrypter(A, b, m):
    bstring = bin(m)

    out = []
    for i in range(2, len(bstring)):
        out.append(BitEncrypter(A, b, bstring[i]))

    return out
