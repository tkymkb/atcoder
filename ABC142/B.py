def resolve():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    oks = [1 for hi in h if hi >= k]
    print(len(oks))


if __name__ == "__main__":
    resolve()
