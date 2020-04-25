def resolve():
    a, d = map(int, input().split())
    print(max(a, d) * (min(a, d) + 1))


if __name__ == "__main__":
    resolve()
