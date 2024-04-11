import sys
from queue import PriorityQueue


dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
input = sys.stdin.readline
n = int(input())
shark_size = 2
fish, time = 0, 0
x, y = 0, 0
adj_map = []
for i in range(n):
    row = list(map(int, input().split()))
    try:
        x, y = i, row.index(9)
    except:
        pass
    adj_map.append(row)
    
 
def bfs(rx, ry):
    global shark_size, fish, time
    visited = [[False for j in range(n)] for i in range(n)]
    q = PriorityQueue()
    visited[rx][ry] = True
    adj_map[rx][ry] = 0
    q.put((0, rx, ry))
    
    while not q.empty():
        dist, cx, cy = q.get()
        
        if 0 < adj_map[cx][cy] < shark_size:
            fish += 1
            if fish == shark_size:
                shark_size += 1
                fish = 0
            adj_map[cx][cy] = 0
            time += dist
            return cx, cy, True
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and adj_map[nx][ny] <= shark_size:
                visited[nx][ny] = True
                q.put((dist + 1, nx, ny))
                
    return rx, ry, False

while True:
    x, y, found = bfs(x, y)
    if not found:
        break
print(time)