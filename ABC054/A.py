def resolve():
    a, b = map(int, input().split())
    if a == 1:
        a *= 100
    if b == 1:
        b *= 100
    if a < b:
        print("Bob")
    elif a > b:
        print("Alice")
    else:
        print("Draw")


if __name__ == "__main__":
    resolve()
