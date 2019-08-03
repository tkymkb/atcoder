def solve():
    n = int(input())
    d = list(map(int, [input() for i in range(n)]))
    return len(set(d))


if __name__ == "__main__":
    print(solve())
