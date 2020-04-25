def solve():
    a, b, c, d, e = [int(input()) for _ in range(5)]
    k = int(input())
    return ":(" if e - a > k else "Yay!"


if __name__ == "__main__":
    print(solve())
