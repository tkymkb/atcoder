def solve():
    n = int(input())
    c = 0
    for i in range(1, n + 1):
        if len(str(i)) % 2:
            c += 1
    return c


if __name__ == "__main__":
    print(solve())
