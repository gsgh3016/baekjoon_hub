import sys

input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    s1, s2 = set(), set()
    for _ in range(n):
        s1.add(input().rstrip())
    for _ in range(m):
        s2.add(input().rstrip())
    inter = list(s1.intersection(s2))
    inter.sort()

    print(len(inter))
    for name in inter:
        print(name)


if __name__ == "__main__":
    main()
