import sys

input = sys.stdin.readline
n = int(input())
file_names = [input().rstrip() for _ in range(n)]

str_len = len(file_names[0])
cmd = ""
for j in range(str_len):
    cur_ch = ""
    for i in range(n):
        if i == 0:
            cur_ch = file_names[0][j]
        if cur_ch != file_names[i][j]:
            cur_ch = "?"
            break
    cmd += cur_ch

print(cmd)
