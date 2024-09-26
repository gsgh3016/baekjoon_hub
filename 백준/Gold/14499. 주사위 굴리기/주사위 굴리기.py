import sys
from collections import deque


input = sys.stdin.readline

EAST = 1
WEST = 2
NORTH = 3
SOUTH = 4
dx = [None, 0, 0, -1, 1]
dy = [None, 1, -1, 0, 0]

class Dice:
    def __init__(self):
        self.up = 0
        self.east = 0
        self.west = 0
        self.north = 0
        self.south = 0
        self.down = 0
        
    def roll(self, direction):
        if direction == EAST:
            self.roll_east()
        elif direction == WEST:
            self.roll_west()
        elif direction == NORTH:
            self.roll_north()
        elif direction == SOUTH:
            self.roll_south()
            
    def roll_east(self):
        tmp = self.up
        self.up = self.west
        self.west = self.down
        self.down = self.east
        self.east = tmp
    
    def roll_west(self):
        tmp = self.up
        self.up = self.east
        self.east = self.down
        self.down = self.west
        self.west = tmp
    
    def roll_north(self):
        tmp = self.up
        self.up = self.south
        self.south = self.down
        self.down = self.north
        self.north = tmp
    
    def roll_south(self):
        tmp = self.up
        self.up = self.north
        self.north = self.down
        self.down = self.south
        self.south = tmp

n, m, x, y, k = map(int, input().split())
field = []
for _ in range(n):
    field.append(list(map(int, input().split())))
command = list(map(int, input().split()))
pos = (x, y)

dice = Dice()

for c in command:
    nx, ny = pos[0] + dx[c], pos[1] + dy[c]
    if nx >= n or nx < 0 or ny >= m or ny < 0:
        continue
    dice.roll(c)
    if field[nx][ny] == 0:
        field[nx][ny] = dice.down
    else:
        dice.down = field[nx][ny]
        field[nx][ny] = 0
        
    pos = (nx, ny)
    
    print(dice.up)