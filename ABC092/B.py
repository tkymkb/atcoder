def resolve():
    n = int(input())
    d, x = list(map(int, input().split()))
    a = list(int(input()) for _ in range(n))
    choco = sum([1 + (d - 1) // ai for ai in a]) + x
    print(choco)


if __name__ == "__main__":
    resolve()
