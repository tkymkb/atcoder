def resolve():
    # n switches, m bulbs
    n, m = map(int, input().split())
    s = list(list(map(int, input().split()))[1:] for _ in range(m))
    p = list(map(int, input().split()))
    print(sum([1 for i in range(1 << n) if all([sum([1 for sji in sj if i & (1 << (sji - 1))]) % 2 == pj for sj, pj in zip(s, p)])]))


if __name__ == "__main__":
    resolve()
