def solve():
    n = int(input())
    a = list(map(int, input().split()))
    return max(a) - min(a)


if __name__ == "__main__":
    print(solve())
