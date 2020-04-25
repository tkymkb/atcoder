def resolve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    c = 0
    if a[0] > x:
        c += a[0] - x
        a[0] = x
    for i in range(n - 1):
        s = a[i] + a[i + 1]
        if s > x:
            c += s - x
            a[i + 1] -= s - x
    print(c)


if __name__ == "__main__":
    resolve()
