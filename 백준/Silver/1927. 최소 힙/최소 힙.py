import heapq
import sys

input = sys.stdin.readline


def main():
    n = int(input())
    h = []
    heapq.heapify(h)
    for _ in range(n):
        num = int(input())
        if num == 0 and len(h) == 0:
            print(0)
        elif num == 0:
            print(heapq.heappop(h))
        else:
            heapq.heappush(h, num)


if __name__ == "__main__":
    main()
