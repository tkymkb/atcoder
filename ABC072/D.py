def resolve():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    if p[0] == 1:
        p[0], p[1] = p[1], p[0]
        ans += 1
    if p[n - 1] == n:
        p[n - 2], p[n - 1] = p[n - 1], p[n - 2]
        ans += 1
    for i in range(n - 1):
        if p[i] == i + 1:
            p[i], p[i + 1] = p[i + 1], p[i]
            ans += 1
    print(ans)


if __name__ == "__main__":
    resolve()
