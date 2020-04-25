import bisect


def resolve():
    A, B, Q = map(int, input().split())
    INF = 10 ** 18
    s = [-INF] + list(int(input()) for _ in range(A)) + [INF]
    t = [-INF] + list(int(input()) for _ in range(B)) + [INF]
    for q in range(Q):
        x = int(input())
        b, d = bisect.bisect_right(s, x), bisect.bisect_right(t, x)
        res = INF
        for S in [s[b - 1], s[b]]:
            for T in [t[d - 1], t[d]]:
                d1, d2 = abs(S - x) + abs(T - S), abs(T - x) + abs(S - T)
                res = min(res, d1, d2)
        print(res)


if __name__ == "__main__":
    resolve()
