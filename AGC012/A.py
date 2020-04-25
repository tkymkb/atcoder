def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    for i in range(n):
        ans += a[2 * i + 1]
    print(ans)


if __name__ == "__main__":
    resolve()
