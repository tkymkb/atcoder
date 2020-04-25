import fractions
from functools import reduce


def solve():
    n, m = map(int, input().split())
    ab = list(list(map(int, input().split())) for _ in range(m))
    bridges = set([i for i in range(n)])
    for a, b in ab:
        bridges &= set([i for i in range(a - 1, b - 1)])
    print(bridges)


if __name__ == "__main__":
    print(solve())
