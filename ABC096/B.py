def resolve():
    abc = list(map(int, input().split()))
    n = int(input())
    ans = max(abc) * 2 ** n + sum(abc) - max(abc)
    print(ans)


if __name__ == "__main__":
    resolve()
