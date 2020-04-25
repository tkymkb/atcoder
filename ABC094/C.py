def resolve():
    n = int(input())
    x = list(map(int, input().split()))
    xs = sorted(x, reverse=True)
    for i in range(n):
        if x[i] < xs[n // 2 - 1]:
            print(xs[n // 2 - 1])
        else:
            print(xs[n // 2])


if __name__ == "__main__":
    resolve()
