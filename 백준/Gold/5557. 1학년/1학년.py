import sys


input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

dp = [[0 for i in range(21)] for j in range(n - 1)]
dp[0][nums[0]] = 1

for i in range(1, n - 1):   # i번쨰 숫자
    for j in range(21):     # 이전 결과와 i번 숫자를 연산했을 때 j
        if dp[i - 1][j] == 0: # 이전 숫자를 골랐을때 경우의 수가 0
            continue
        if 0 <= j + nums[i] <= 20:
            dp[i][j + nums[i]] += dp[i - 1][j]
        if 0 <= j - nums[i] <= 20:
            dp[i][j - nums[i]] += dp[i - 1][j]

print(dp[n - 2][nums[-1]])