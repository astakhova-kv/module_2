def get_matrix(n, m, value):
    matrix = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[i][j] = value
    return (matrix)


result = get_matrix(2, 2, 10)
print(result)
