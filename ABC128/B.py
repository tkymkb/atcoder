def solve():
    n = int(input())
    sp = list(list(input().split()) for _ in range(n))
    ans = sorted(enumerate(sp), key=lambda x: (x[1][0], -int(x[1][1])))
    for d in ans:
        print(d[0] + 1)


if __name__ == "__main__":
    solve()
