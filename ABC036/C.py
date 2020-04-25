def resolve():
    n = int(input())
    a = list(int(input()) for _ in range(n))
    s = sorted(set(a))
    d = {}
    for i in range(len(s)):
        d[s[i]] = i
    for ai in a:
        print(d[ai])


if __name__ == "__main__":
    resolve()
