def solve():
    r = int(input())
    if r < 1200:
        return "ABC"
    elif r < 2800:
        return "ARC"
    else:
        return "AGC"


if __name__ == "__main__":
    print(solve())
