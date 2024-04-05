import sys


nums = [[[] for i in range(10)] for j in range(11)]
nums[1] = [[i] for i in range(10)]

n = int(input())

cnt = 9
if n <= 9:
    print(n)
    exit(0)
for length in range(1, 11):
    for first_digit in range(10):
        for i in range(length - 2, first_digit):
            for num in nums[length - 1][i]:
                new_num = first_digit * (10 ** (length - 1)) + num
                nums[length][first_digit].append(new_num)
                cnt += 1
#                print(f'length: {length}, {nums[length][first_digit]}')
                if cnt == n:
                    print(new_num)
                    exit(0)
print(-1)