import itertools


def solve():
    a, b, c = input().split()
    v = itertools.permutations([a, b, c], 3)
    max_a = 0
    for e1, e2, e3 in v:
        a = max(eval(e1 + "+" + e2 + e3), eval(e1 + e2 + "+" + e3))
        if a > max_a:
            max_a = a
    return max_a


if __name__ == "__main__":
    print(solve())
