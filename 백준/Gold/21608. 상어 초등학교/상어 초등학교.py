import sys
from queue import PriorityQueue


def is_like(x, y, student):
    return classroom[x][y] in like_students[student]

def is_empty(x, y):
    return classroom[x][y] == 0

def is_in(x, y):
    return 0 <= x < n and 0 <= y < n

def count_by_condition(x, y, student):
    like_cnt, empty_cnt = 0, 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not is_in(nx, ny):
            continue
        if is_like(nx, ny, student):
            like_cnt += 1
        if is_empty(nx, ny):
            empty_cnt += 1
    return like_cnt, empty_cnt


def place_students(student):
    pq = PriorityQueue()
    
    for i in range(n):
        for j in range(n):
            if classroom[i][j] != 0:
                continue
            like_cnt, empty_cnt = count_by_condition(i, j, student)
            pq.put((-like_cnt, -empty_cnt, i, j))

    res_x, res_y = pq.get()[2:]
    classroom[res_x][res_y] = student


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
input = sys.stdin.readline
student_order = []
like_students = {}
deg_convert = {0:0, 1:1, 2:10, 3:100, 4:1000}
n = int(input())
classroom = [[0 for j in range(n)] for i in range(n)]
for i in range(n ** 2):
    student_order.append(list(map(int, input().split())))
    like_students[student_order[-1][0]] = set(student_order[-1][1:])

for order in student_order:
    place_students(order[0])

ans = 0
for i in range(n):
    for j in range(n):
        deg, _ = count_by_condition(i, j, classroom[i][j])
        ans += deg_convert[deg]
        
print(ans)