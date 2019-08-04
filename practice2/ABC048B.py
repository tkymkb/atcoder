def solve():
    a, b, x = map(int, input().split())
    return b // x - (a - 1) // x


if __name__ == "__main__":
    print(solve())
