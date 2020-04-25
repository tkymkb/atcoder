def resolve():
    a, b, k = list(map(int, input().split()))
    s = set()
    for i in range(a, min(a + k, b + 1)):
        s.add(i)
    for i in range(max(a, b - k + 1), b + 1):
        s.add(i)
    for i in sorted(s):
        print(i)


if __name__ == "__main__":
    resolve()
