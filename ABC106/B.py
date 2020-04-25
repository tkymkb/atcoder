def solve():
    n = int(input())
    ans = 0
    for i in range(1, n + 1, 2):
        divider = 0
        for j in range(3, n // 3 + 1, 2):
            if i % j == 0:
                divider += 1
        if divider == 6:
            ans += 1
    print(ans)


if __name__ == "__main__":
    solve()
