import homomorphic_arithmetic

def evalAdd(ctexts):
    if not isinstance(ctexts, list):
        return None
    v = None
    w = None
    l = None

    return None

def evalMult(ctexts):
    if not isinstance(ctexts, list):
        return None
    if len(ctexts) != 2:
        return None


    return None

class Gate:
    def __init__(self, inputs, addOrMult):
        self._inputs = inputs
        self._addOrMult = addOrMult & 1

    def setInput(self, inputs):
        self._inputs = inputs

    def process(self, ctexts):
        c = []
        for i in range(0, len(self._inputs)):
            if i == 1:
                c.append(ctexts[i])
class Layer:
    def __init__(self, sizei=1, addOrMult):
        self.addOrMult = addOrMult & 1 #1 for multiply, 0 for Add
        self.size = 0
        if size > 0:
            self.size = size

        self.gates = []*self.size

    def setInput(self, inputs):
        for i in inputs:
            self.gates.setInput(i)

    def process(self, ctexts):
        for i in range(0, self.size):
            "process"

class Circuit:
    def __init__(self, layers=[]):
        self._layers = layers

    def process(self, ctexts):
        for l in self._layers:
            l.process(ctexts)

def evalLayer(layer, ctexts):
    ntexts = ctexts
    if layer.addOrMult == 0:
        for i in range(0, layer.size):
            ntexts = evalAdd(ctexts)
    elif layer.addOrMult == 1:
        for i in range(0, layer.size):
            ntexts = evalMult(ctexts)

    return ntexts

def getCipherTextsByLayer(ctexts, layer):
    ret = []
    for c in ctexts:
        if c.layer() == layer:
            ret.append(c)
    return ret

def eval(dimension, f, ctexts):
    "f is a circuit, c is an array of ciphertexts"
    ntexts = ctexts
    start = 0
    end = 0
    for layer in f.layers:
        end = start + layer.size
        ntexts0 = evalLayer(layer, ntexts[start:end])

    return None

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

