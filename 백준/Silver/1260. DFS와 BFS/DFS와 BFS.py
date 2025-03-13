import sys
from queue import Queue

input = sys.stdin.readline

adj_matrix = []


def dfs(n, cur, visited: list[bool], order: list[int]):
    visited[cur] = True
    order.append(cur)

    for next in range(1, n + 1):
        if not visited[next] and adj_matrix[cur][next]:
            dfs(n, next, visited, order)


def bfs(n, start, order: list[int]):
    visited = [False for _ in range(n + 1)]
    queue = Queue()

    visited[start] = True
    queue.put(start)
    order.append(start)

    while not queue.empty():
        cur = queue.get()

        for next in range(1, n + 1):
            if visited[next] or not adj_matrix[cur][next]:
                continue

            visited[next] = True
            queue.put(next)
            order.append(next)


def main():
    global adj_matrix
    n, m, v = map(int, input().split())

    adj_matrix = [[False for _ in range(n + 1)] for __ in range(n + 1)]
    for _ in range(m):
        s, e = map(int, input().split())
        adj_matrix[s][e] = True
        adj_matrix[e][s] = True

    dfs_order = []
    bfs_order = []
    dfs(n, v, [False for _ in range(n + 1)], dfs_order)
    print(*dfs_order)
    bfs(n, v, bfs_order)
    print(*bfs_order)


if __name__ == "__main__":
    main()
