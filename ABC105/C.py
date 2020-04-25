def solve():
    n = int(input())
    digits = 1
    num = 0
    s = ""
    while num != n:
        num += -2 ** digits
        s = "1" + s
        for d in range(2 ** digits):
            d_bit = bin(d)
        if num == n:
            return s

    return "0"


if __name__ == "__main__":
    print(solve())
