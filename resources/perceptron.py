class Perceptron(object):
    def __init__(self, learn_rate, size_x, size_y):
        self.learn_rate = learn_rate
        self.size_x = size_x
        self.size_y = size_y
        self.weights = [0]*(size_x*size_y+1)

    def learn(self, tests):
        interation = 0
        done = False
        while not done:
            done = True
            interation += 1
            for test in tests:
                function_value = 0
                for i in range(0, len(self.weights)):
                    function_value += self.weights[i]*test['entry'][i]
                s_out = self._f_value(function_value)
                if s_out != test['expected']:
                    done = False
                    for i in range(0, len(self.weights)):
                        self.weights[i] += self.learn_rate*(test['expected'] - s_out)*test['entry'][i]
        print 'Number of iterations:', interation

    def print_weights(self):
        final_matrix = self.weights[1:]
        print 'Weights:'
        print 'w0:', self.weights[0], '(bias)'
        for y in range(0, self.size_y):
            print ['%.4f' % final_matrix[x+(y*self.size_x)] for x in range(0, self.size_x)]

    @staticmethod
    def _f_value(value):
        if value > 0:
            return 1
        return 0
