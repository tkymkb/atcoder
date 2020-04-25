from itertools import combinations
import math


def solve():
    n, d = map(int, input().split())
    x = list(list(map(int, input().split())) for _ in range(n))
    c = 0
    for p1, p2 in combinations(x, 2):
        d = 0
        for i in range(len(p1)):
            d += abs(p1[i] - p2[i]) ** 2
        d = math.sqrt(d)
        if d.is_integer():
            c += 1
    return c


if __name__ == "__main__":
    print(solve())
