def solve():
    s = input()
    t = input()
    if s == t:
        return "Yes"
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            return "Yes"
    return "No"


if __name__ == "__main__":
    print(solve())
