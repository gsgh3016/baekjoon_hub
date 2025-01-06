import sys

input = sys.stdin.readline
m = int(input())
s = [False for _ in range(21)]

for _ in range(m):
    cmd = input().rstrip()
    if "add" in cmd:
        _, x = cmd.split()
        x = int(x)
        s[x] = True
    elif "remove" in cmd:
        _, x = cmd.split()
        x = int(x)
        s[x] = False
    elif "check" in cmd:
        _, x = cmd.split()
        x = int(x)
        print(1 if s[x] else 0)
    elif "toggle" in cmd:
        _, x = cmd.split()
        x = int(x)
        s[x] = not s[x]
    elif cmd == "all":
        s = [True for _ in range(21)]
    elif cmd == "empty":
        s = [False for _ in range(21)]
