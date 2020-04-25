def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    m = max(a)
    a.remove(m)
    m2 = min(a, key=lambda x: abs(x - m / 2))
    print(m, m2)


if __name__ == "__main__":
    resolve()
