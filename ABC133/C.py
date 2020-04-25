from itertools import combinations
import math


def solve():
    l, r = map(int, input().split())
    a = 2018
    for i in range(l, r):
        for j in range(i + 1, r + 1):
            amari = (i * j) % 2019
            if amari == 0:
                return 0
            elif amari < a:
                a = amari
    return a


if __name__ == "__main__":
    print(solve())
