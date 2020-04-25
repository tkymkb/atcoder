import fractions


def solve():
    n = int(input())
    return lcm(2, n)


def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)


if __name__ == "__main__":
    print(solve())
