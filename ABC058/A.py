def resolve():
    a, b, c = map(int, input().split())
    print("YES" if b - a == c - b else "NO")


if __name__ == "__main__":
    resolve()
