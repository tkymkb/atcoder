def solve():
    a, b, t = map(int, input().split())
    return int((t + 0.5) // a * b)


if __name__ == "__main__":
    print(solve())
