def load_test_set(tests):
    file = open('infile.txt', 'r')
    size = int(file.readline())

    current = 0
    matrix = []
    for line in file:
        if current < size:
            matrix.append(line)
            current += 1
        else:
            in_values = process_matrix(matrix)
            expected_value = int(line)
            test_entry = dict(entry=in_values, expected=expected_value)
            tests.append(test_entry)
            matrix= []
            current = 0

    return size


def process_matrix(matrix):
    vector = []
    vector.append(1) # BIAS
    for line in matrix:
        for char in list(line[:-1]):
            vector.append(int(char))

    return vector
