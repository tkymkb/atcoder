import math


def solve():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    m = []
    for i in range(n):
        l, r = a[:i], a[i + 1:]
        gcd_l, gcd_r = 0, 0
        if len(l) == 1:
            gcd_l = l[0]
        else:
            for j in range(len(l) - 1):
                gcd_l = math.gcd(l[j], l[j + 1])
        if len(r) == 1:
            gcd_r = r[0]
        else:
            for j in range(len(r) - 1):
                gcd_r = math.gcd(r[j], r[j + 1])
        m.append(math.gcd(gcd_l, gcd_r))
    return max(m)


if __name__ == "__main__":
    print(solve())
