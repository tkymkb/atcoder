import math


def solve():
    abcde = [int(input()) for _ in range(5)]
    if any([str(i)[-1] != "0" for i in abcde]):
        last = min([i for i in abcde if not str(i)[-1] == "0"], key=lambda x: abs(int(str(x)[-1])))
    else:
        last = min(abcde)
    hoge = sum([math.ceil(i / 10) * 10 for i in abcde]) - (math.ceil(last / 10) * 10)
    print(hoge + last)


if __name__ == "__main__":
    solve()
