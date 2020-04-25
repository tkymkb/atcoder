def solve():
    n = int(input())
    l = list(map(int, input().split()))
    return "Yes" if max(l) < sum(l) - max(l) else "No"


if __name__ == "__main__":
    print(solve())
