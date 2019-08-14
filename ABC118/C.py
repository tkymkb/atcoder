from functools import reduce
import math
import fractions


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    return reduce(fractions.gcd, a)


if __name__ == "__main__":
    print(solve())
