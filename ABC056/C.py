def resolve():
    x = int(input())
    i = 0
    steps = 0
    while steps < x:
        i += 1
        steps = i * (i + 1) // 2
    print(i)


if __name__ == "__main__":
    resolve()
