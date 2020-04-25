def solve():
    n, a, b = map(int, input().split())
    return min(a * n, b)


if __name__ == "__main__":
    print(solve())