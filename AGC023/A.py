from collections import defaultdict


def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    d[0] = 1
    s = 0
    for i in range(n):
        s += a[i]
        d[s] += 1
    print(sum([v * (v - 1) for v in d.values()]) // 2)


if __name__ == "__main__":
    resolve()
