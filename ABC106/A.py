def solve():
    a, b = map(int, input().split())
    return a * b - (a + b - 1)


if __name__ == "__main__":
    print(solve())
