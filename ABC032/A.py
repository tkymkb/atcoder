def resolve():
    a = int(input())
    b = int(input())
    n = int(input())
    for i in range(n, n + 10 ** 5):
        if i % a == 0 and i % b == 0:
            print(i)
            return 0


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


if __name__ == "__main__":
    resolve()
