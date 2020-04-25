def solve():
    s = input()
    c0 = s[0] == "A"
    c1 = s[2:-1].count("C") == 1
    c2 = sum([1 for c in s if c.isupper()]) == 2
    return "AC" if c0 and c1 and c2 else "WA"


if __name__ == "__main__":
    print(solve())
