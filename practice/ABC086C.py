def solve():
    n = int(input())
    ts, xs, ys = 0, 0, 0
    for _ in range(n):
        tg, xg, yg = map(int, input().split())
        dt = tg - ts
        distance = abs(xg - xs) + abs(yg - ys)
        if distance > dt or distance % 2 != dt % 2:
            return "No"
        ts, xs, ys = tg, xg, yg
    return "Yes"


if __name__ == "__main__":
    print(solve())
