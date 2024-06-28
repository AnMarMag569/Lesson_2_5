def get_matrix(n=2, m=2, value=10):
    matrix = []
    for i in range(n):
        mx = []
        matrix.append(mx)
        for j in range(m):
            mx.append(value)
    return matrix
matrix = get_matrix(2, 2, 10)
print(matrix)
get_matrix(2,5,42)
matrix = get_matrix(3, 5, 42)
print(matrix)
get_matrix(4,2,13)
matrix = get_matrix(4, 2, 13)
print(matrix)