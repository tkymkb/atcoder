def resolve():
    n = int(input())
    k = int(input())
    ans = 1
    for _ in range(n):
        ans += min(k, ans)
    print(ans)


if __name__ == "__main__":
    resolve()
