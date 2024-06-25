import sys


input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
max_acc = nums[0]

for i in range(1, n):
    nums[i] = max(nums[i], nums[i] + nums[i - 1])
    max_acc = max(max_acc, nums[i])

print(max_acc)