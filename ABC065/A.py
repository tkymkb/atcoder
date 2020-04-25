def resolve():
    x, a, b = map(int, input().split())
    if b <= a:
        print("delicious")
    elif a < b <= a + x:
        print("safe")
    else:  # if a + x < b
        print("dangerous")


if __name__ == "__main__":
    resolve()
