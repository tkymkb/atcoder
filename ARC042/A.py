def resolve():
    n, m = map(int, input().split())
    a = list(int(input()) for _ in range(m))
    wrote = [False] * n
    for ai in a[::-1]:
        if not wrote[ai - 1]:
            print(ai)
            wrote[ai - 1] = True
    for i in range(n):
        if not wrote[i]:
            print(i + 1)


if __name__ == "__main__":
    resolve()
