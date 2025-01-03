from collections import Counter

n = int(input())
fruits = list(map(int, input().split()))

left = 0
fruit_dict = Counter()
max_length = 0

for right in range(n):
    fruit_dict[fruits[right]] += 1

    while len(fruit_dict) > 2:
        fruit_dict[fruits[left]] -= 1
        if fruit_dict[fruits[left]] == 0:
            del fruit_dict[fruits[left]]
        left += 1

    max_length = max(max_length, right - left + 1)

print(max_length)
