def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i, ai in enumerate(a):
        if a[ai - 1] == i + 1:
            ans += 1
    print(ans // 2)


if __name__ == "__main__":
    resolve()
