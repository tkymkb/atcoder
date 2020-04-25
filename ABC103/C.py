import fractions
from functools import reduce


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    lcm_a = lcm(*a)
    fm = sum([(lcm_a - 1) % ai for ai in a])
    return fm


def lcm_base(x, y):
    return x * y // fractions.gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


if __name__ == "__main__":
    print(solve())
