import logging
import numpy
import rvg
from ciphertext import Ciphertext

seed = 5684
def BitEncrypter(A, b, mbit, modulus, log=logging.getLogger(__name__)):

    mbit = 1 & mbit # we only want a bit

    m0 = len(A)
    # r is probably not correct...
    r = numpy.ndarray([m0, 1], dtype=numpy.integer) #generate random vector r<-{0,1}^m?
    s = rvg.RVG(m0, 2, seed)
    sp = s.generate()
    sp = next(sp)
    r[:, 0] = sp[:] & 1
    
    # Need to use dot here, because in numpy dot is actually matrix multiplication while * is not.
    # Very intuitive! \s
    log.debug("R={r}\nA={A}\n m={m}".format(r=r, A=A, m=mbit))
    v = numpy.asarray(numpy.mod(A.T.dot(r).T, modulus))
    w = (b.T.dot(r) + mbit) % modulus
    
    ciphertext = Ciphertext(numpy.squeeze(v), w.item(0), 0)
    log.debug("Ciphertext={c}".format(c=ciphertext))
    return ciphertext

def MessageEncrypter(A, b, m, modulus, log=logging.getLogger(__name__)):
    bstring = bin(m)

    out = []
    for i in range(2, len(bstring)):
        # Need to convert back to int, so that operation in BitEncrypter do not throw exceptions
        out.append(BitEncrypter(A, b, int(bstring[i]), modulus, log=log))

    return out
