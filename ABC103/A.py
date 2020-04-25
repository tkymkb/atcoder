def solve():
    abc = sorted(list(map(int, input().split())))
    return abc[2] - abc[0]


if __name__ == "__main__":
    print(solve())
