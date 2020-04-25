def resolve():
    s = input()
    ls = len(s)
    ans = 0
    for i in range(ls):
        if s[i] == "U":
            ans += ls - i - 1
            ans += 2 * i
        else:
            ans += i
            ans += 2 * (ls - i - 1)
    print(ans)


if __name__ == "__main__":
    resolve()
