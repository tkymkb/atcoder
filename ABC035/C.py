def resolve():
    n, q = map(int, input().split())
    lrs = list(list(map(int, input().split())) for _ in range(q))
    a = [0 for _ in range(n + 1)]
    for l, r in lrs:
        a[l - 1] += 1
        a[r] -= 1
    c = 0
    ans = ""
    for i in range(n):
        c += a[i]
        ans += str(c % 2)
    print(ans)


if __name__ == "__main__":
    resolve()
