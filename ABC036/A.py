import math


def resolve():
    a, b = map(int, input().split())
    print(math.ceil(b / a))


if __name__ == "__main__":
    resolve()
