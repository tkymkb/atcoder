def resolve():
    w, a, b = map(int, input().split())
    if a + w < b:
        print(b - a - w)
    elif b + w < a:
        print(a - b - w)
    else:
        print("0")


if __name__ == "__main__":
    resolve()
