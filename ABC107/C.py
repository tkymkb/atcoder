def solve():
    n, k = map(int, input().split())
    xs = list(map(int, input().split()))
    min_dist = 10 ** 9
    for i in range(n - k + 1):
        length = abs(xs[i] - xs[i + k - 1])
        dist = min(abs(xs[i]) + length, abs(xs[i + k - 1]) + length)
        if dist < min_dist:
            min_dist = dist
    return min_dist


if __name__ == "__main__":
    print(solve())
