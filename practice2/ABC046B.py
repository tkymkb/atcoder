def solve():
    n, k = map(int, input().split())
    return k * (k - 1) ** (n - 1)


if __name__ == "__main__":
    print(solve())
