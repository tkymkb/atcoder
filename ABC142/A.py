def resolve():
    n = int(input())
    if n % 2 == 0:
        print(0.5)
    else:
        print((n // 2 + 1) / n)


if __name__ == "__main__":
    resolve()
