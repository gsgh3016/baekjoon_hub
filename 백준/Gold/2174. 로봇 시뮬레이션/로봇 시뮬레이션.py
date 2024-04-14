robots = [None]
adj_map = []
direction = {
    "N": 0,
    "W": 1,
    "S": 2,
    "E": 3
}
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def rotate_l(target, times):
    robots[target][2] = (robots[target][2] + times % 4) % 4

def rotate_r(target, times):
    robots[target][2] = (robots[target][2] - times % 4 + 4) % 4

def is_out_bound(target, x, y):
    if not (0 <= x < b and 0 <= y < a):
        print(f"Robot {target} crashes into the wall")
        exit(0)

def is_crash_robot(target, x, y):
    if adj_map[x][y] != 0:
        print(f"Robot {target} crashes into robot {adj_map[x][y]}")
        exit(0)
        
def go_forward(target, times):
    x, y, d = robots[target]
    nx, ny = x + dx[d] * times, y + dy[d] * times
    origin_x, origin_y = x, y
    while (x, y) != (nx, ny):
        x, y = x + dx[d], y + dy[d]
        is_out_bound(target, x, y)
        is_crash_robot(target, x, y)
    adj_map[origin_x][origin_y] = 0
    adj_map[nx][ny] = target
    robots[target] = [nx, ny, d]
    
command = {
    "L": rotate_l,
    "R": rotate_r,
    "F": go_forward
}

def convert_coord(x, y):
    return b - y, x - 1 


a, b = map(int, input().split())
n, m = map(int, input().split())
adj_map = [[0 for i in range(a)] for j in range(b)]
for i in range(1, n + 1):
    init_x, init_y, init_direction = input().split()
    x, y, d = int(init_x), int(init_y), direction[init_direction]
    x, y = convert_coord(x, y)
    robots.append([x, y, d])
    adj_map[x][y] = i
for _ in range(m):
    target, cmd, times = input().split()
    target, cmd, times = int(target), command[cmd], int(times)
    cmd(target, times)
print("OK")