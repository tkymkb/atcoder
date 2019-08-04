def solve():
    n = int(input())
    num = 10 ** 9 + 7
    power = 1
    for i in range(1, n + 1):
        power = power * i % num
    print(power)


if __name__ == "__main__":
    solve()
