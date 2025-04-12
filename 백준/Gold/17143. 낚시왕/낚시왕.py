import sys

input = sys.stdin.readline
UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4
R, C, M = map(int, input().split())
board = [[0] * C for _ in range(R)]
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    r, c = r - 1, c - 1
    board[r][c] = (s, d, z)


def fish(j):
    for i in range(R):
        if board[i][j]:
            x = board[i][j][2]
            board[i][j] = 0
            return x
    return 0


def move():
    global board
    new_board = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j]:
                s, d, z = board[i][j]
                ni, nj, nd = get_next_loc(i, j, s, d)
                if new_board[ni][nj]:
                    if new_board[ni][nj][2] < z:
                        new_board[ni][nj] = (s, nd, z)
                else:
                    new_board[ni][nj] = (s, nd, z)
    board = new_board


def get_next_loc(i, j, speed, dir):
    if dir == UP or dir == DOWN:
        cycle = 2 * (R - 1)
        speed += cycle - i if dir == UP else i

        speed %= cycle

        return (cycle - speed, j, UP) if speed >= R else (speed, j, DOWN)

    cycle = 2 * (C - 1)
    speed += cycle - j if dir == LEFT else j

    speed %= cycle

    return (i, cycle - speed, LEFT) if speed >= C else (i, speed, RIGHT)


ans = 0
for j in range(C):
    ans += fish(j)
    move()

print(ans)
