class Perceptron(object):
    def __init__(self, learn_rate, size):
        self.learn_rate = learn_rate
        self.size = size
        self.weights = [0]*(size*size+1)
        print "learn rate:", self.learn_rate, "pesos:", self.weights

    def learn(self, tests):
        interation = 0
        done = False
        while not done:
            interation += 1
            done = True
            function_value = 0
            for test in tests:
                for i in range(0, len(self.weights)):
                    function_value += self.weights[i]*test['entry'][i]
                s_out = self._f_value(function_value)
                if s_out != test['expected']:
                    done = False
                    for i in range(0, len(self.weights)):
                        self.weights[i] += self.learn_rate*(test['expected'] - s_out)*test['entry'][i]
        print 'Iterations:', interation
        # print self.weights.reshape(self.size, self.size)
        for i in range(1, self.size*self.size+1, self.size):
            print [self.weights[i+j] for j in range(0, self.size)]

    @staticmethod
    def _f_value(value):
        if value > 0:
            return 1
        return 0