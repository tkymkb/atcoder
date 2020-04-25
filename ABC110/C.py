from collections import defaultdict


def solve():
    s = input()
    t = input()
    ds = defaultdict(int)
    for c in s:
        ds[c] += 1
    nums_s = sorted(ds.values())
    dt = defaultdict(int)
    for c in t:
        dt[c] += 1
    nums_t = sorted(dt.values())
    return "Yes" if nums_s == nums_t else "No"


if __name__ == "__main__":
    print(solve())
