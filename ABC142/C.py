def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted([(i, ai) for i, ai in enumerate(a)], key=lambda x: x[1])
    print(" ".join([str(i + 1) for i, _ in b]))


if __name__ == "__main__":
    resolve()
