import sys

input = sys.stdin.readline
n, m = map(int, input().split())
name_to_num = {}
num_to_name = [None]

for i in range(n):
    name = input().rstrip()
    name_to_num[name] = i + 1
    num_to_name.append(name)

for _ in range(m):
    query = input().rstrip()
    if query.isnumeric():
        query = int(query)
        print(num_to_name[query])
        continue
    print(name_to_num[query])
