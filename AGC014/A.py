import math


def resolve():
    a, b, c = map(int, input().split())
    if a == b == c:
        if a % 2:
            print(0)
        else:
            print(-1)
        return 0
    for i in range(int(math.log2(10 ** 9)) + 1):
        if a % 2 or b % 2 or c % 2:
            print(i)
            return 0
        a_new, b_new, c_new = (b + c) // 2, (a + c) // 2, (a + b) // 2,
        a, b, c = a_new, b_new, c_new
    print(-1)


if __name__ == "__main__":
    resolve()
