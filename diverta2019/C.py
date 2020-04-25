def resolve():
    n = int(input())
    s = list(input() for _ in range(n))
    ans = 0
    for si in s:
        ans += si.count("AB")
    ends_with_a = len([si for si in s if not si.startswith("B") and si.endswith("A")])
    starts_with_b = len([si for si in s if si.startswith("B") and not si.endswith("A")])
    ab = len([si for si in s if si.startswith("B") and si.endswith("A")])
    if ab:
        ans += ab + min(ends_with_a, starts_with_b)
    else:
        ans += min(ends_with_a, starts_with_b)
    print(ans)


if __name__ == "__main__":
    resolve()

