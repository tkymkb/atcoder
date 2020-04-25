import math


def resolve():
    a, b, x = map(float, input().split())
    h = x / (a ** 2)
    if h >= b / 2:
        degree = math.degrees(math.atan(2 * (b - h) / a))
    else:
        degree = math.degrees(math.atan(b ** 2 / (2 * a * h)))
    print(degree)


if __name__ == "__main__":
    resolve()
