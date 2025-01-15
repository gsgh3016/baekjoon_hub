import sys

input = sys.stdin.readline
n, k = map(int, input().split())
coins = []
min_num = 0

for _ in range(n):
    coins.append(int(input()))

for i in range(n - 1, -1, -1):
    cur_coin_num = k // coins[i]
    k -= coins[i] * cur_coin_num
    min_num += cur_coin_num

    if k == 0:
        break

print(min_num)
