def solve():
    a, b = map(int, input().split())
    return "Yes" if (a * b) % 2 == 1 else "No"


if __name__ == "__main__":
    print(solve())
