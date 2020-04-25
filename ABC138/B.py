def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1 / sum([1 / ai for ai in a])
    print(ans)


if __name__ == "__main__":
    resolve()
