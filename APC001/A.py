def resolve():
    x, y = map(int, input().split())
    if x % y == 0:
        print(-1)
    else:
        print(x)


if __name__ == "__main__":
    resolve()
