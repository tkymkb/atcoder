def solve():
    n = int(input())
    a = list(map(int, input().split()))
    return "YES" if sum(a) % 2 == 0 else "NO"


if __name__ == "__main__":
    print(solve())
