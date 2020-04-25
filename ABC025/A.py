from itertools import product


def resolve():
    s = input()
    n = int(input())
    print(["".join(ci) for ci in product(s, repeat=2)][n - 1])


if __name__ == "__main__":
    resolve()
