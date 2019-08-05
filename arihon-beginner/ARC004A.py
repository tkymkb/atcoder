import itertools
import math


def solve():
    n = int(input())
    data = list(list(map(int, input().split())) for _ in range(n))
    longest = 0
    for p1, p2 in itertools.combinations(data, 2):
        d = get_distance(p1, p2)
        if d > longest:
            longest = d
    return math.sqrt(longest)


def get_distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


if __name__ == "__main__":
    print(solve())
