def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    k = len(set(a))
    if k % 2:
        print(k)
    else:
        print(k - 1)


if __name__ == "__main__":
    resolve()
