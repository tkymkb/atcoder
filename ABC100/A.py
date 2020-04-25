def solve():
    a, b = map(int, input().split())
    return "Yay!" if a <= 8 and b <= 8 else ":("


if __name__ == "__main__":
    print(solve())
