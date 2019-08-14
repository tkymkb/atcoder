def solve():
    n, m = map(int, input().split())
    ka = [list(map(int, input().split())) for _ in range(n)]
    common = set([i for i in range(1, m + 1)])
    for i in range(len(ka)):
        common = set(set(ka[i][1:]) & common)
    return len(common)


if __name__ == "__main__":
    print(solve())
