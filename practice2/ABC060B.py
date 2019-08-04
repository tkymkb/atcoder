def solve():
    a, b, c = map(int, input().split())
    for i in range(1, b + 1):
        if (a * i) % b == c:
            return "YES"
    return "NO"


if __name__ == "__main__":
    print(solve())
