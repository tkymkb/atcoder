def solve():
    n = int(input())
    change = 1000 - n
    ans = 0
    for c in [500, 100, 50, 10, 5, 1]:
        cnt = change // c
        ans += cnt
        change -= c * cnt
        if change == 0:
            return ans


if __name__ == "__main__":
    print(solve())
