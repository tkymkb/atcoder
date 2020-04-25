def solve():
    n = int(input())
    a = list(int(input()) for _ in range(n))
    ranking = sorted(a)[::-1]
    first = ranking[0]
    second = ranking[1]
    first_idx = a.index(first)
    for idx in range(n):
        if idx == first_idx:
            print(second)
        else:
            print(first)


if __name__ == "__main__":
    solve()
