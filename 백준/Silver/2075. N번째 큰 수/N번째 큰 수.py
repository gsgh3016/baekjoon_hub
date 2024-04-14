import heapq


n = int(input())
min_heap = []
for _ in range(n):
    nums = map(int, input().split())
    for num in nums:
        if len(min_heap) < n:
            heapq.heappush(min_heap, num)
            continue
        if num > min_heap[0]:
            heapq.heapreplace(min_heap, num)

print(min_heap[0])