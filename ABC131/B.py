def solve():
    n, l = map(int, input().split())
    tastes = [l + i for i in range(n)]
    if 0 in tastes:
        return sum(tastes)
    elif all([t > 0 for t in tastes]):
        return sum(tastes) - min(tastes)
    elif all([t < 0 for t in tastes]):
        return sum(tastes) - max(tastes)


if __name__ == "__main__":
    print(solve())
