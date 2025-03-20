import sys

input = sys.stdin.readline


def main():
    x = int(input())
    dp = [0x4F4F4F4F for i in range(x + 1)]
    dp[1] = 0
    for i in range(1, x + 1):
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i > 1:
            dp[i] = min(dp[i], dp[i - 1] + 1)

    print(dp[x])


if __name__ == "__main__":
    main()
