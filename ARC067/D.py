def resolve():
    n, a, b = list(map(int, input().split()))
    x = list(map(int, input().split()))
    e = 0
    for i in range(n - 1):
        e += min(abs(x[i + 1] - x[i]) * a, b)
    print(e)


if __name__ == "__main__":
    resolve()
