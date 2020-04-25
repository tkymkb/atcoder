import math


def resolve():
    n, m = map(int, input().split())
    mod = 10 ** 9 + 7
    if n == m:
        print(math.factorial(n) * math.factorial(m) * 2 % mod)
    elif n - 1 == m or m - 1 == n:
        print(math.factorial(n) * math.factorial(m) % mod)
    else:
        print(0)


if __name__ == "__main__":
    resolve()
