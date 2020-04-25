def solve():
    n = input()
    sn = sum([int(d) for d in n])
    return "Yes" if int(n) % sn == 0 else "No"


if __name__ == "__main__":
    print(solve())
