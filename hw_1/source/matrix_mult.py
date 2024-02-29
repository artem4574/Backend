n = int(input())

matrix_1 = [[int(input()) for _ in range(n)] for _ in range(n)]
matrix_2 = [[int(input()) for _ in range(n)] for _ in range(n)]
result_matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            result_matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]

for i in result_matrix:
    print(i, end='')
    print()