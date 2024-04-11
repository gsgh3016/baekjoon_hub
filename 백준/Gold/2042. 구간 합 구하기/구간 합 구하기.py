from math import ceil, log2, pow
import sys


def segment(l, r, i):
    if l == r:
        segment_tree[i] = nums[l - 1]
        return segment_tree[i]
    mid = (l + r) // 2
    segment_tree[i] = segment(l, mid, i * 2) + segment(mid + 1, r, i * 2 + 1)
    return segment_tree[i]

def query_sum(start, end, i, l, r):
    if end < l or r < start:
        return 0
    if l <= start and end <= r:
        return segment_tree[i]
    mid = (start + end) // 2
    return query_sum(start, mid, i * 2, l, r) + query_sum(mid + 1, end, i * 2 + 1, l, r)

def update(start, end, node, i, val):
    if i < start or end < i:
        return
    segment_tree[node] += val
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, node * 2, i, val)
    update(mid + 1, end, node * 2 + 1, i, val)
    

input = sys.stdin.readline
n, m, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
h = ceil(log2(n))
tree_size = int(pow(2, h + 1) - 1)
segment_tree = [0] + [0 for _ in range(tree_size)]

segment(1, n, 1)
for _ in range(m + k):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        diff = cmd[2] - nums[cmd[1] - 1]
        nums[cmd[1] - 1] = cmd[2]
        update(1, n, 1, cmd[1], diff)
    if cmd[0] == 2:
        print(query_sum(1, n, 1, cmd[1], cmd[2]))