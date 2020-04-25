def solve():
    n = int(input())
    ds = sorted(list(map(int, input().split())))
    abc_max = ds[n // 2 - 1]
    arc_min = ds[n // 2]
    return arc_min - abc_max


if __name__ == "__main__":
    print(solve())
