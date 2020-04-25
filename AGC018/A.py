def resolve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    large = [ai for ai in a if ai > k]
    for l in large:
        for i in range(n - 1):
            if abs(a[i] - a[i + 1]) == l - k:
                print("POSSIBLE")
    print("IMPOSSIBLE")


if __name__ == "__main__":
    resolve()
