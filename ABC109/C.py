from functools import reduce
import fractions


def solve():
    n, X = map(int, input().split())
    xs = list(map(int, input().split()))
    diffs = [abs(x - X) for x in xs]
    return reduce(fractions.gcd, diffs)


if __name__ == "__main__":
    print(solve())
