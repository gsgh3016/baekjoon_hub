import sys


def dfs(i, j, visited, is_move):
    s = [(i, j)]
    visited[i][j] = True
    graph = [(i, j)]
    acc = populations[i][j]
    num = 1
    
    while s:
        cx, cy = s.pop()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not (0 <= nx < n and 0 <= ny < n) or visited[nx][ny]:
                continue
            diff = abs(populations[cx][cy] - populations[nx][ny])
            if l <= diff <= r and diff != 0:
                is_move = True
                s.append((nx, ny))
                visited[nx][ny] = True
                graph.append((nx, ny))
                acc += populations[nx][ny]
                num += 1
    
    for x, y in graph:
        populations[x][y] = acc // num
    
    return is_move


input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n, l, r = map(int, input().split())
populations = []
for _ in range(n):
    populations.append(list(map(int, input().split())))

day = 0
while True:
    is_move = False
    visited = [[False for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                is_move = dfs(i, j, visited, is_move)
    
    if not is_move:
        break
    day += 1

print(day)