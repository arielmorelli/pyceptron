from resources.perceptron import Perceptron
from resources.test_set import load_test_set


def run_perceptron():
    tests = []
    sizes = load_test_set(tests, 'infile2.txt')
    perceptron = Perceptron(0.5, sizes[0], sizes[1])
    perceptron.learn(tests)
    perceptron.print_weights()


if __name__ == "__main__":
    run_perceptron()
