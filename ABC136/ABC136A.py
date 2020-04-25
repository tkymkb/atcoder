def solve():
    a, b, c = map(int, input().split())
    return max(c - (a - b), 0)


if __name__ == "__main__":
    print(solve())
