def resolve():
    a, b, c = input().split()
    print("".join([s[0].upper() for s in [a, b, c]]))


if __name__ == "__main__":
    resolve()
