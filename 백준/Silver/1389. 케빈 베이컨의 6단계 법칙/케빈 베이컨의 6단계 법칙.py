import sys
from queue import Queue


input = sys.stdin.readline
n, m = map(int, input().split())
friends = {}

for _ in range(m):
    a, b = map(int, input().split())
    if a not in friends:
        friends[a] = [b]
    else:
        friends[a].append(b)
    if b not in friends:
        friends[b] = [a]
    else:
        friends[b].append(a)
    
def bfs(root):
    visited = [False for _ in range(n + 1)]
    depth = [0 for _ in range(n + 1)]
    q = Queue()
    visited[root] = True
    q.put(root)
    
    while not q.empty():
        cur = q.get()
        for i in friends[cur]:
            if not visited[i]:
                visited[i] = True
                q.put(i)
                depth[i] = depth[cur] + 1
    
    return sum(depth)

bacon = 0x4f4f
person = 0
for i in range(1, n + 1):
    tmp = bfs(i)
    if bacon > tmp:
        person = i
        bacon = tmp
    
print(person)