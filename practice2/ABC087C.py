def solve():
    n = int(input())
    field = [list(map(int, input().split())) for _ in range(2)]
    return max([sum(field[0][:i + 1]) + sum(field[1][i:]) for i in range(n)])


if __name__ == "__main__":
    print(solve())
