import sys


input = sys.stdin.readline
t = int(input())
cnt = t
for _ in range(t):
    word = input().rstrip()
    ch_set = set()
    for i in range(len(word)):
        if i >= 1 and word[i] != word[i - 1] and word[i] in ch_set:
            cnt -= 1
            break
        ch_set.add(word[i])

print(cnt)