def solve():
    n, k = map(int, input().split())
    h = sorted(list(int(input()) for _ in range(n)))
    return min(h[i + k - 1] - h[i] for i in range(n - k + 1))


if __name__ == "__main__":
    print(solve())
