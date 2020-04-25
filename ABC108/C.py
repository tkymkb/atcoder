from functools import reduce
import fractions
import itertools


def solve():
    n, k = map(int, input().split())
    count = 0
    for a in range(1, n + 1):
        for b in range(k - a, n + 1):
            if (a + b) % k:
                continue
            print("ok", a, b)
            for c in range(1, n + 1):
                (a + b + c) = 3 * n * k / 2
                if (a + c) % k or (b + c) % k:
                    continue
                print(a, b, c)
                count += 1
                # if (a + c) % k == (b + c) % k == 0:
                #     count += 1
    return count


if __name__ == "__main__":
    print(solve())
