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

class Layer:
    def __init__(self, size, addOrMult):
        self.addOrMult = addOrMult & 1 #1 for multiply, 0 for Add
        self.size = 0
        if size > 0:
            self.size = size
        self.fanin = 2

        if self.addOrMult == 0:
            self.fanin = -1

class Circuit:
    def __init__(self):
        self.layers = []

def evalLayer(layer, ctexts):
    ntexts = ctexts
    if layer.addOrMult == 0:
        for i in range(0, layer.size):
            ntexts = evalAdd(ctexts)
    elif layer.addOrMult == 1:
        for i in range(0, layer.size):
            ntexts = evalMult(ctexts)

    return ntexts

def eval(f, ctexts):
    "f is a circuit, c is an array of ciphertexts"
    ntexts = ctexts
    for layer in f.layers:
        ntexts = evalLayer(layer, ntexts)

    return None
