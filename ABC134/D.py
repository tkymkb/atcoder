def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    # index: 0, box num: 1
    for i in range(1, n + 1)[::-1]:
        total = 0
        for j in range(i, n, i):
            total += b[j - 1]
        if total % 2 == a[i - 1]:
            b[i - 1] = 0
        else:
            b[i - 1] = 1
    total = sum(b)
    print(total)
    if any([i for i in b if b == 1]):
        print(" ".join([str(idx + 1) for idx, v in enumerate(b) if v == 1]))


if __name__ == "__main__":
    solve()
