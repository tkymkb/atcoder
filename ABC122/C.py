def solve():
    n, q = map(int, input().split())
    s = input()
    lrs = list(list(map(int, input().split())) for _ in range(q))
    # ans = [s[l - 1:r].count("AC") for l, r in lrs]
    c = [0] * n
    for i in range(1, n):
        c[i] = c[i - 1]
        if s[i - 1] == "A" and s[i] == "C":
            c[i] += 1
    ans = [c[r - 1] - c[l - 1] for l, r in lrs]
    print(*ans, sep="\n")


if __name__ == "__main__":
    solve()
