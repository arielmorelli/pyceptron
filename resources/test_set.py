def load_test_set(tests, file_name):
    file = open(file_name, 'r')
    sizes = file.readline().split('\n')
    sizes = sizes[0].split('x')
    size_x = int(sizes[0])
    size_y = int(sizes[1])

    current = 0
    matrix = []
    for line in file:
        if current < size_y:
            matrix.append(line)
            current += 1
        else:
            in_values = process_matrix(matrix)
            expected_value = int(line)
            test_entry = dict(entry=in_values, expected=expected_value)
            tests.append(test_entry)
            matrix= []
            current = 0

    return size_x, size_y


def process_matrix(matrix):
    vector = []
    vector.append(1) # BIAS
    for line in matrix:
        for char in list(line[:-1]):
            vector.append(int(char))

    return vector
