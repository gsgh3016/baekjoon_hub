import sys


factorials = [0 for _ in range(31)]
factorials[0] = 1

def factorial(i):
    if factorials[i] != 0:
        return factorials[i]
    return i * factorial(i - 1)

def combination(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(combination(m, n))