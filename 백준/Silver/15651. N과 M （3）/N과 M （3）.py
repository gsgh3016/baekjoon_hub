import sys


input = sys.stdin.readline
n, m = map(int, input().split())

def backtracking(n, m, res=[]):
    if m == 0:
        print(' '.join(map(str, res)))
        return
    for i in range(1, n + 1):
        backtracking(n, m - 1, res + [i])

backtracking(n, m)