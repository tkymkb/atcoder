def resolve():
    a = int(input())
    b = int(input())
    if a > b:
        print("GREATER")
    elif a == b:
        print("EQUAL")
    else:
        print("LESS")


if __name__ == "__main__":
    resolve()
