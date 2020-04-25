def resolve():
    s = input()
    ls = len(s)
    for i in range(1, ls - 1):
        t = s[:-i]
        lt = len(t)
        if lt % 2 == 0 and t[:lt // 2] * 2 == t:
            print(lt)
            return 0


if __name__ == "__main__":
    resolve()
