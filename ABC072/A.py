def resolve():
    x, t = map(int, input().split())
    print(max(x - t, 0))


if __name__ == "__main__":
    resolve()
