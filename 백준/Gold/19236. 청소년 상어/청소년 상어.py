import sys
from copy import deepcopy


NUM = 0
DIR = 1
input = sys.stdin.readline
dx = [-1, -1, 0, 1, 1, 1, 0, -1]    # idx + 1: 45 deg rotation
dy = [0, -1, -1, -1, 0, 1, 1, 1]
max_num = 0

def is_outbound(x, y):
    return x < 0 or x >= 4 or y < 0 or y >= 4

def change_fish_pos(fish_map, fish_pos):
    for i in range(1, 17):
        if fish_pos[i] == (-1, -1):
            continue
        cx, cy = fish_pos[i]
        cur_fish = fish_map[cx][cy]
        dir = cur_fish[DIR]
        nx, ny = cx + dx[dir], cy + dy[dir]
        for i in range(1, 8):
            if is_outbound(nx, ny) or fish_map[nx][ny] == (-1, -1):
                dir = (dir + 1) % 8
                nx, ny = cx + dx[dir], cy + dy[dir]
                cur_fish = (cur_fish[NUM], dir)
            else:
                break
        target_fish = fish_map[nx][ny]
        fish_pos[cur_fish[NUM]] = (nx, ny)
        fish_pos[target_fish[NUM]] = (cx, cy)
        fish_map[nx][ny] = cur_fish
        fish_map[cx][cy] = target_fish
    return fish_map, fish_pos
        

def backtracking(shark, fish_map, fish_pos):
    global max_num
    cx, cy = shark[0]
    d = shark[1]
    dir_x, dir_y = dx[shark[1]], dy[shark[1]]
    cur_sum = shark[2]
    for i in range(1, 4):
        tmp_map, tmp_pos = deepcopy(fish_map), deepcopy(fish_pos)
        nx, ny = cx + dir_x * i, cy + dir_y * i
        if is_outbound(nx, ny) or tmp_map[nx][ny][DIR] == -1:
            continue
        shark = ((nx, ny), tmp_map[nx][ny][DIR], cur_sum + tmp_map[nx][ny][NUM])
        max_num = max(max_num, shark[2])
        tmp_pos[tmp_map[nx][ny][NUM]] = (-1, -1)
        tmp_map[nx][ny] = (-1, -1)
        tmp_map[cx][cy] = (0, -1)
        tmp_map, tmp_pos = change_fish_pos(tmp_map, tmp_pos)
        backtracking(shark, tmp_map, tmp_pos)
        shark = ((cx, cy), d, cur_sum)

fish_map = [[() for _ in range(4)] for _ in range(4)]
fish_pos = [() for _ in range(17)]
for i in range(4):
    cmd = list(map(int, input().split()))
    for j in range(4):
        a, b = cmd[2 * j], cmd[2 * j + 1] - 1
        fish_map[i][j] = (a, b)
        fish_pos[a] = (i, j)

shark = ((0, 0), fish_map[0][0][DIR], fish_map[0][0][NUM])
fish_pos[fish_map[0][0][NUM]] = (-1, -1)
fish_map[0][0] = (-1, -1)
fish_map, fish_pos = change_fish_pos(fish_map, fish_pos)
backtracking(shark, fish_map, fish_pos)

print(max_num)