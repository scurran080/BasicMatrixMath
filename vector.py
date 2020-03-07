

def add_vector(a, b):
    if len(a) != len(b):
        return
    new_vec = [None] * len(a)
    for i in range(len(a)):
        new_vec[i] = a[i] + b[i]
    return new_vec

def subtract_vector(a,b):
    if len(a) != len(b):
        return
    new_vec = [None] * len(a)
    for i in range(len(a)):
        new_vec[i] = a[i] - b[i]
    return new_vec

#Come back and fix this, only has second vector in the matrix.
def create_matrix(vector_list):
    matrix = [[None for _ in range(len(vector_list[0]))] for _ in range(len(vector_list))]
    idx = 0
    for i in range(len(vector_list)):
        count = 0
        for x in range(len(vector_list[i])):
            matrix[idx][count] = vector_list[idx][count]
            count += 1
        idx += 1
    return matrix
