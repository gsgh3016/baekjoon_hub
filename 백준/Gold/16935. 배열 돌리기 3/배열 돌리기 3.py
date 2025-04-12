import sys

input = sys.stdin.readline
n, m, r = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))

for cmd in command:
    n = len(matrix)
    m = len(matrix[0])
    new_matrix = [[0] * m for _ in range(n)]
    if cmd == 1:
        new_matrix = matrix[::-1]
    if cmd == 2:
        for i in range(n):
            new_matrix[i] = matrix[i][::-1]
    if cmd == 3:
        new_matrix = [list(col) for col in zip(*matrix[::-1])]
    if cmd == 4:
        new_matrix = [list(col) for col in zip(*matrix)][::-1]
    if cmd == 5:
        for i in range(n):
            for j in range(m):
                if i < n // 2 and j < m // 2:
                    new_matrix[i][j + m // 2] = matrix[i][j]
                if i < n // 2 and j >= m // 2:
                    new_matrix[i + n // 2][j] = matrix[i][j]
                if i >= n // 2 and j >= m // 2:
                    new_matrix[i][j - m // 2] = matrix[i][j]
                if i >= n // 2 and j < m // 2:
                    new_matrix[i - n // 2][j] = matrix[i][j]
    if cmd == 6:
        for i in range(n):
            for j in range(m):
                if i < n // 2 and j < m // 2:
                    new_matrix[i + n // 2][j] = matrix[i][j]
                if i >= n // 2 and j < m // 2:
                    new_matrix[i][j + m // 2] = matrix[i][j]
                if i >= n // 2 and j >= m // 2:
                    new_matrix[i - n // 2][j] = matrix[i][j]
                if i < n // 2 and j >= m // 2:
                    new_matrix[i][j - m // 2] = matrix[i][j]

    matrix = new_matrix

for row in matrix:
    print(*row)
