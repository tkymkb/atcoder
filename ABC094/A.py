def resolve():
    a, b, x = map(int, input().split())
    ans = "YES" if a <= x <= a + b else "NO"
    print(ans)


if __name__ == "__main__":
    resolve()
