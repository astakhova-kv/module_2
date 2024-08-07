def get_matrix(n, m, value):
    matrix = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[i][j] = value
    return (matrix)


mat = get_matrix(2, 2, 10)
for i in range(len(mat)):
    print(*mat[i])
