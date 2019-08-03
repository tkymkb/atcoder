def solve():
    n, a, b = list(map(int, input().split()))
    ok_numbers = []
    for num in range(n + 1):
        total = sum([int(i) for i in str(num)])
        if a <= total <= b:
            ok_numbers.append(num)
    return sum(ok_numbers)


if __name__ == "__main__":
    print(solve())
