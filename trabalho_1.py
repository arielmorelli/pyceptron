from resources.perceptron import Perceptron
from resources.test_set import load_test_set


def run_perceptron():
    tests = []
    size = load_test_set(tests)
    perceptron = Perceptron(0.01, size)
    perceptron.learn(tests)
    final_matrix = perceptron.get_weights()
    print_matrix(final_matrix)


def print_matrix(matrix):
    print 'Weights matrix:'
    for line in matrix:
            print ['%.4f' % char for char in line]


if __name__ == "__main__":
    run_perceptron()
