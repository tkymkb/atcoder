from collections import Counter


def resolve():
    n = int(input())
    s = input()
    c = Counter(s)
    ans = 1
    mod = 10 ** 9 + 7
    for v in c.values():
        ans *= v + 1
        ans %= mod
    print(ans - 1)


if __name__ == "__main__":
    resolve()
