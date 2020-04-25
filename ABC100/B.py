def solve():
    d, n = map(int, input().split())
    return (n + (n - 1) // 99) * (100 ** d)


if __name__ == "__main__":
    print(solve())
