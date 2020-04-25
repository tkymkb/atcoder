from collections import defaultdict


def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    for ai in a:
        for i in range(ai - 1, ai + 2):
            d[i] += 1
    m = max(d.items(), key=lambda x: x[1])
    print(m[1])


if __name__ == "__main__":
    resolve()
