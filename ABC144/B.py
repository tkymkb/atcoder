def resolve():
    n = int(input())
    for i in range(1, 10):
        if n % i == 0 and n // i < 10:
            print("Yes")
            return 0
    print("No")


if __name__ == "__main__":
    resolve()
