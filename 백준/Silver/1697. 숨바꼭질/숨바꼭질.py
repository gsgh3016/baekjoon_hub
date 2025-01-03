import sys
from queue import Queue


input = sys.stdin.readline
n, k = map(int, input().split())
pos = [False for _ in range(100_001)]

q = Queue()
q.put((n, 0))
pos[n] = True
cur = 0
s = 0
while not q.empty():
    cur, s = q.get()
    if cur == k:
        break
    if cur + 1 <= 100_000 and not pos[cur + 1]:
        pos[cur + 1] = True
        q.put((cur + 1, s + 1))
    if cur - 1 >= 0 and not pos[cur - 1]:
        pos[cur - 1] = True
        q.put((cur - 1, s + 1))
    if 2 * cur <= 100_000 and not pos[2 * cur]:
        pos[2 * cur] = True
        q.put((2 * cur, s + 1))
        
print(s)