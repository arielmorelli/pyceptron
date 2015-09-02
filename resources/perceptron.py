

class Perceptron(object):
    def __init__(self, learn_rate, size):
        self.learn_rate = learn_rate
        self.weights = [0]*(size*size)
        print "learn rate:", self.learn_rate, "pesos:", self.weights
