import sys

input = sys.stdin.readline


def main():
    equation = input().rstrip()

    num_char = ""
    total = 0
    for c in equation:
        if c != "-" and c != "+":
            num_char += c
        elif c == "+" and num_char.find("-") == -1:
            total += int(num_char)
            num_char = ""
        elif c == "+" and num_char.find("-") != -1:
            total += int(num_char)
            num_char = "-"
        elif c == "-":
            total += int(num_char)
            num_char = "-"

    total += int(num_char)
    print(total)


if __name__ == "__main__":
    main()
