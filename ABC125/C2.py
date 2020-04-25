import math


def solve():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    m = []
    for i in range(n):
        gcd = 0
        b = [a[x] for x in range(n) if x != i]
        for j in range(n - 2):
            gcd = math.gcd(b[j], b[j + 1])
        m.append(gcd)
    return max(m)


if __name__ == "__main__":
    print(solve())
