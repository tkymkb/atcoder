def resolve():
    n, k = map(int, input().split())
    s = list(int(input()) for _ in range(n))
    if 0 in s:
        print(len(s))
        return 0
    t = 1
    ans = 0
    l, r = 0, 0
    for r in range(n):
        t *= s[r]
        if t <= k:
            ans = r - l + 1
        else:
            t //= s[l]
            l += 1
    print(ans)


if __name__ == "__main__":
    resolve()
