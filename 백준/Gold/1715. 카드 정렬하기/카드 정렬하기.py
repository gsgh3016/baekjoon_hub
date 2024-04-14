import heapq


n = int(input())
card = []
for _ in range(n):
    heapq.heappush(card, int(input()))

acc = 0
while len(card) > 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    acc += a + b
    heapq.heappush(card, a + b)

print(acc)