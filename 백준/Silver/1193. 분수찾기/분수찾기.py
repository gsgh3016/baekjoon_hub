import sys


input = sys.stdin.readline
n = int(input())
level = 0
acc = 0
while True:
    level += 1
    start, end, diff = level if level % 2 == 1 else 1, 0 if level % 2 == 1 else level + 1, -1 if level % 2 == 1 else 1
    for i in range(start, end, diff):
        acc += 1
        if acc == n:
            print(f"{i}/{level + 1 - i}")
            exit(0)