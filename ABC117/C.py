def solve():
    n, m = map(int, input().split())
    x = sorted(list(map(int, input().split())))
    diff = sorted([x[i + 1] - x[i] for i in range(m - 1)], reverse=True)
    return sum(diff[n - 1:])


if __name__ == "__main__":
    print(solve())
