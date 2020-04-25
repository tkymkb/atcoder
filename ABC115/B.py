def solve():
    n = int(input())
    p = list(int(input()) for _ in range(n))
    return sum(p) - max(p) // 2


if __name__ == "__main__":
    print(solve())
