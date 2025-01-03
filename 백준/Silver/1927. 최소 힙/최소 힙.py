import heapq
import sys

input = sys.stdin.readline
n = int(input())
hq = []
heapq.heapify(hq)
for _ in range(n):
    num = int(input())
    if num == 0:
        if not hq:
            print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, num)
