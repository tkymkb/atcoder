def solve():
    s = input()
    genom = ["A", "T", "G", "C"]
    count, ans = 0, 0
    for c in s:
        if c in genom:
            count += 1
            if count > ans:
                ans = count
        else:
            count = 0
    print(ans)


if __name__ == "__main__":
    solve()
