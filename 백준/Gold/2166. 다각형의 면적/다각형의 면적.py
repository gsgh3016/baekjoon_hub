import sys


input = sys.stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
points.append(points[0])
 
area = 0
for i in range(n):
    area += points[i][0] * points[i + 1][1] - points[i + 1][0] * points[i][1]

print(round(abs(area) / 2, 1))