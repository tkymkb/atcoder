def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a_sorted = sorted(a, reverse=True)
    alice = sum(a_sorted[0::2])
    bob = sum(a_sorted[1::2])
    return alice - bob


if __name__ == "__main__":
    print(solve())
