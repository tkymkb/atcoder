def resolve():
    a, b = map(int, input().split())
    print(max(0, a - 2 * b))


if __name__ == "__main__":
    resolve()