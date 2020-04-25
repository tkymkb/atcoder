from collections import defaultdict


def resolve():
    n, m = map(int, input().split())
    xys = list(list(map(int, input().split())) for _ in range(m))
    num = [1] * n
    red = [False] * n
    red[0] = True
    for x, y in xys:
        if red[x - 1]:
            red[y - 1] = True
        num[x - 1] -= 1
        num[y - 1] += 1
        if num[x - 1] == 0:
            red[x - 1] = False
    print(red.count(True))


if __name__ == "__main__":
    resolve()
