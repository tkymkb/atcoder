from collections import defaultdict


def resolve():
    n = int(input())
    v = list(map(int, input().split()))
    d_o = defaultdict(int)
    d_e = defaultdict(int)
    for i in range(n):
        if i % 2:
            d_o[v[i]] += 1
        else:
            d_e[v[i]] += 1
    d_e[0] = 0
    d_o[0] = 0
    de = sorted(d_e.items(), key=lambda x: -x[1])
    do = sorted(d_o.items(), key=lambda x: -x[1])
    if de[0][0] != do[0][0]:
        print(n - de[0][1] - do[0][1])
    else:
        p01 = de[0][1] + do[1][1]
        p10 = de[1][1] + do[0][1]
        print(n - max(p01, p10))


if __name__ == "__main__":
    resolve()
