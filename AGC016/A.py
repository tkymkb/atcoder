def resolve():
    s = input()
    print(min([max(map(len, s.split(c))) for c in s]))


if __name__ == "__main__":
    resolve()
