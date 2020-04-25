from itertools import combinations


def resolve():
    n = int(input())
    d = list(map(int, input().split()))
    ans = sum([d1 * d2 for d1, d2 in combinations(d, 2)])
    print(ans)


if __name__ == "__main__":
    resolve()
