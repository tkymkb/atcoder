def solve():
    n = int(input())
    vs = list(map(int, input().split()))
    cs = list(map(int, input().split()))
    return sum([v - c for v, c in zip(vs, cs) if v > c])


if __name__ == "__main__":
    print(solve())
