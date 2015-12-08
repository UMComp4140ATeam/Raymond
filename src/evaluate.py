from homomorphic_arithmetic import HomomorphicArithmetic

class Layer:
    def __init__(self, gates=[], addOrMult=0):
        self._addOrMult = addOrMult & 1 #1 for multiply, 0 for Add

        self._gates = gates

    def numOfGates(self):
        return len(self._gates)
    def isAdd(self):
        return self._addOrMult == 0

    def process(self, dimension, odd_modulus, ctexts, evaluation_key=None):
        arithmetic = HomomorphicArithmetic(dimension, odd_modulus)
        ret = []
        for g in self._gates:
            ntexts = []
            for c in g:
                ntexts.append(ctexts[c])

            if self._addOrMult == 0:
                ret.append(arithmetic.homomorphic_add(ntexts))
            elif self._addOrMult == 1:
                ret.append(arithmetic.homomorphic_multiply(ntexts[0], ntexts[1], evaluation_key))

        n = ctexts + ret
        ctexts[:] = n[:]
        return ret
class Circuit:
    def __init__(self, layers=[]):
        self._layers = layers

    def process(self, dimension, odd_modulus, ctexts, evaluation_key):
        for l in self._layers:
            l.process(dimension, odd_modulus, ctexts, evaluation_key)

def eval(dimension, f, ctexts):
    "f is a circuit, c is an array of ciphertexts"
    return f.process(dimension, ctexts)

###Example Construction###

#Construct Layer(s)#
#Construct

