def resolve():
    x = int(input())
    n = (x // 11) * 2
    if 1 <= x % 11 <= 6:
        n += 1
    elif x % 11 > 6:
        n += 2
    print(n)


if __name__ == "__main__":
    resolve()
