import sys

input = sys.stdin.readline
n, m = map(int, input().split())
s1, s2 = set(), set()

for _ in range(n):
    s1.add(input().rstrip())

for _ in range(m):
    s2.add(input().rstrip())

inter = sorted(list(s1.intersection(s2)))
print(len(inter))
for name in inter:
    print(name)
