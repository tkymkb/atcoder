def resolve():
    n = int(input())
    a = list(int(input()) for _ in range(n))
    ans = 0
    for i in range(n):
        ans += a[i] // 2
        if i != n - 1 and a[i] % 2 and a[i + 1] % 2:
            ans += 1
            a[i + 1] -= 1
    print(ans)


if __name__ == "__main__":
    resolve()
