import sys
from collections import deque

input = sys.stdin.readline
n, m, r = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * m for _ in range(n)]

for i in range(min(n, m) // 2):
    dq = deque()
    dq.extend(matrix[x][i] for x in range(i, n - i))
    dq.extend(matrix[n - i - 1][i + 1 : m - i - 1])
    dq.extend(matrix[x][m - i - 1] for x in range(n - i - 1, i - 1, -1))
    dq.extend(matrix[i][i + 1 : m - i - 1][::-1])
    dq.rotate(r)
    for x in range(i, n - i):
        result[x][i] = dq.popleft()
    for y in range(i + 1, m - i - 1):
        result[n - i - 1][y] = dq.popleft()
    for x in range(n - i - 1, i - 1, -1):
        result[x][m - i - 1] = dq.popleft()
    for y in range(m - i - 2, i, -1):
        result[i][y] = dq.popleft()

for row in result:
    print(*row)
