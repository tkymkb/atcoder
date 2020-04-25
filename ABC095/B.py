def resolve():
    n, x = list(map(int, input().split()))
    m = list(int(input()) for _ in range(n))
    print((x - sum(m)) // min(m) + n)


if __name__ == "__main__":
    resolve()
