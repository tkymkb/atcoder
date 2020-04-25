def resolve():
    n, q = map(int, input().split())
    ab = sorted(list(list(map(int, input().split())) for _ in range(n - 1)))
    px = list(list(map(int, input().split())) for _ in range(q))
    counters = [0] * n
    for p, x in px:
        counters[p - 1] += x
    for i in range(2, n + 1):
        parent = list(filter(lambda x: x[1] == i, ab))[0][0]
        counters[i - 1] += counters[parent - 1]
    print(" ".join([str(c) for c in counters]))


if __name__ == "__main__":
    resolve()
