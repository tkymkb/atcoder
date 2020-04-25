def resolve():
    s = input()
    a = s.index("A")
    z = s[::-1].index("Z")
    print(len(s) - z - a)


if __name__ == "__main__":
    resolve()
