def solve():
    n = int(input())
    e = [i for i in range(1, n + 1) if i % 2 == 0]
    o = [i for i in range(1, n + 1) if i % 2 == 1]
    return len(e) * len(o)


if __name__ == "__main__":
    print(solve())
