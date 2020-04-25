def resolve():
    n, m = map(int, input().split())
    if m <= 2 * n:
        print(m // 2)
    else:
        print(n + (m - 2 * n) // 4)


if __name__ == "__main__":
    resolve()
