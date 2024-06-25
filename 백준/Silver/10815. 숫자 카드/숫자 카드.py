import sys


input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()
ans = [0] * m

for i, t in enumerate(b):
    l, r = 0, n - 1
    found = False
    while l <= r:
        mid = (l + r) // 2
        if a[mid] > t:
            r = mid - 1
        elif a[mid] < t:
            l = mid + 1
        else:
            found = True
            break
    ans[i] = 1 if found else 0

print(' '.join(map(str, ans)))