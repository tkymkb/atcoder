def resolve():
    l, h = map(int, input().split())
    n = int(input())
    a = list(int(input()) for _ in range(n))
    for ai in a:
        if ai < l:
            print(l - ai)
        elif ai > h:
            print(-1)
        else:
            print(0)


if __name__ == "__main__":
    resolve()
