from functools import reduce
from operator import mul


def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    print(3 ** n - reduce(mul, [1 if ai % 2 else 2 for ai in a]))


if __name__ == "__main__":
    resolve()
