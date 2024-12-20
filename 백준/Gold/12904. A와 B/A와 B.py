import sys

input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

state = 0
for _ in range(len(t) - len(s)):
    if t[-1] == "A":
        t.pop()
    else:
        t.pop()
        t = t[::-1]
    if s == t:
        state = 1

print(state)
