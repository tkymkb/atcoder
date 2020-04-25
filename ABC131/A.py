def solve():
    s = input()
    return "Bad" if any([s[i] == s[i + 1] for i in range(len(s) - 1)]) else "Good"


if __name__ == "__main__":
    print(solve())
