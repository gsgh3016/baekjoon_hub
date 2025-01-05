import sys

input = sys.stdin.readline
n = int(input())
frame = [[" "] * (2 * n) for _ in range(n)]


def triangle(x_t, y_t, x_l, y_l, x_r, y_r, n):
    if n == 3:
        frame[x_t][y_t] = "*"
        frame[x_t + 1][y_t - 1] = "*"
        frame[x_t + 1][y_t + 1] = "*"
        for j in range(y_l, y_r + 1):
            frame[x_l][j] = "*"
        return
    triangle(
        x_t,
        y_t,
        x_t + n // 2 - 1,
        y_l + n // 2,
        x_t + n // 2 - 1,
        y_t + n // 2 - 1,
        n // 2,
    )
    triangle(x_t + n // 2, y_l + n // 2 - 1, x_l, y_l, x_l, y_t - 1, n // 2)
    triangle(x_t + n // 2, y_t + n // 2, x_l, y_t + 1, x_r, y_r, n // 2)


triangle(0, n - 1, n - 1, 0, n - 1, 2 * n - 2, n)
for row in frame:
    print(*row, sep="")
