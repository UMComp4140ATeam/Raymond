from homomorphic_arithmetic import HomomorphicArithmetic

class Layer:
    def __init__(self, gates=[], addOrMult):
        self._addOrMult = addOrMult & 1 #1 for multiply, 0 for Add

        self._gates = gates

    def process(self, dimension, odd_modulus, ctexts):
        arithmetic = HomomorphicArithmetic(dimension, odd_modulus)
        for g in self._gates:
            ntexts = []
            for c in g:
                ntexts.append(ctexts[c])

            if self._addOrMult == 0:
                arithmetic.homorphic_add(dimension, ntexts)
            elif self._addOrMult == 1:
                arithmetic.homorphic_mult(dimension, ntexts)

class Circuit:
    def __init__(self, layers=[]):
        self._layers = layers

    def process(self, dimension, ctexts):
        for l in self._layers:
            l.process(dimension, ctexts)

def eval(dimension, f, ctexts):
    "f is a circuit, c is an array of ciphertexts"
    return f.process(dimension, ctexts)

###Example Construction###

#Construct Layer(s)#
g0 = [0, 1]
g1 = [1, 2]
g2 = [2, 3, 4]
l0 = Layer([g0,g1,g2], 0)

g3 = [5, 1]
g4 = [6, 7]
l1 = Layer([g3, g4], 1) #mult

g5 = [8, 9]
l2 = Layer([g5], 0)

Circuit([l0, l1, l2])
#Construct

