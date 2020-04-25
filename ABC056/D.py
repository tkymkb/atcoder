from math import factorial


def resolve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for ai in a:
        if ai >= k:
            continue



def combi(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))


if __name__ == "__main__":
    resolve()
