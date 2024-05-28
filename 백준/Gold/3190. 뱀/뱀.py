import sys
from collections import deque


input = sys.stdin.readline
dx = [0, 1, 0, -1] # clockwise
dy = [1, 0, -1, 0]
EMPTY = 0
SNAKE = 1
APPLE = 2

class Snake:
    def __init__(self):
        self.deque = deque()
        self.deque.append((0, 0))
        self.d = 0
    
    def go_ahead(self):
        global n
        head_pos = self.deque.popleft()
        self.deque.appendleft(head_pos)
        nx, ny = head_pos[0] + dx[self.d], head_pos[1] + dy[self.d]
        if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == SNAKE:
            return True
        self.deque.appendleft((nx, ny))
        if board[nx][ny] == EMPTY:
            tx, ty = self.deque.pop()
            board[tx][ty] = EMPTY
        board[nx][ny] = SNAKE
        return False
            
    def l_rotate(self):
        self.d = (self.d + 3) % 4

    def r_rotate(self):
        self.d = (self.d + 1) % 4
        

def process(sec, cmd):
    global cur_t
    while cur_t < sec:
        cur_t += 1
        is_crashed = snake.go_ahead()
        if is_crashed:
            return False
    if cmd == 'L':
        snake.l_rotate()
    if cmd == 'D':
        snake.r_rotate()
    return True


snake = Snake()

n = int(input())
board = [[EMPTY for _ in range(n)] for __ in range(n)]
board[0][0] = SNAKE
for _ in range(int(input())):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = APPLE
    
cur_t = 0
commands = []
for _ in range(int(input())):
    sec, cmd = input().split()
    sec = int(sec)
    commands.append((sec, cmd))
is_success = False
for sec, cmd in commands:
    is_success = process(sec, cmd)
    if not is_success:
        break
if is_success:
    process(0x4f4f4f, '_')
print(cur_t)