def resolve():
    a, b, c = map(int, input().split())
    if a == b: print(c)
    if c == b: print(a)
    if a == c: print(b)


if __name__ == "__main__":
    resolve()
