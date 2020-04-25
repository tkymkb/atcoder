def solve():
    n, d = map(int, input().split())
    if not n % (2 * d + 1):
        return n // (2 * d + 1)
    else:
        return n // (2 * d + 1) + 1


if __name__ == "__main__":
    print(solve())
