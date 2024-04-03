import sys


input = sys.stdin.readline
n, k = map(int, input().split())
belt = list(map(int, input().split()))
robot = [False for _ in range(n)]
zero_count = 0
step = 0

def rotate():
    r = belt[-1]
    belt.pop()
    belt.insert(0, r)
    robot.pop()
    robot.insert(0, False)


def move_robot():
    global zero_count
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            robot[i] = False
        elif robot[i] and not robot[i + 1] and belt[i + 1] > 0:
            robot[i] = False
            robot[i + 1] = True
            belt[i + 1] -= 1
            if belt[i + 1] == 0:
                zero_count += 1
    
            
while zero_count < k:
    step += 1
    
    rotate()
    move_robot()
    if not robot[0] and belt[0] > 0:
        robot[0] = True
        belt[0] -= 1
        if belt[0] == 0:
            zero_count += 1
            
print(step)