def resolve():
    s = int(input())
    # s = (10**9 * y3 - x3 * 1)
    x2, y2 = 10 ** 9, 1
    y3 = -(-s // 10 ** 9)
    x3 = y3 * 10 ** 9 - s
    print(0, 0, x2, y2, x3, y3)


if __name__ == "__main__":
    resolve()
