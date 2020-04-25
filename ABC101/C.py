import math


def solve():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    min_index = a.index(min(a))
    print(min_index)
    print(min_index + 1)
    print(n - min_index)
    left = math.ceil((min_index + 1) / k)
    right = math.ceil((n - min_index) / k)
    print(left, right)
    return left + right


if __name__ == "__main__":
    print(solve())
