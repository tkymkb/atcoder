def resolve():
    n, m, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ans = min(sum([1 for ai in a if ai >= x]), sum([1 for ai in a if ai < x]))
    print(ans)


if __name__ == "__main__":
    resolve()
