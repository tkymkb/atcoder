import bisect


def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            k = bisect.bisect_left(l, l[i] + l[j])
            ans += max(k - j - 1, 0)
    print(ans)


if __name__ == "__main__":
    resolve()
