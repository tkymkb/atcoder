import itertools
import math


def solve():
    d, g = map(int, input().split())
    data = list(list(map(int, input().split())) for _ in range(d))
    print(data)


if __name__ == "__main__":
    print(solve())
