def solve():
    s = input()
    return s.count("+") - s.count("-")


if __name__ == "__main__":
    print(solve())
