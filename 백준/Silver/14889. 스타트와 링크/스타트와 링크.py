import sys
from itertools import combinations, permutations

input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

combination = list(combinations(range(n), n // 2))
team_1 = combination[: len(combination)]
team_2 = combination[len(combination) // 2 :][::-1]

min_val = 0x4F4F4F4F
for t1, t2 in zip(team_1, team_2):
    s1 = 0
    for i, j in permutations(t1, 2):
        s1 += s[i][j]
    s2 = 0
    for i, j in permutations(t2, 2):
        s2 += s[i][j]

    min_val = min(min_val, abs(s1 - s2))

print(min_val)
