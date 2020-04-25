def resolve():
    n = int(input())
    xyh = list(list(map(int, input().split())) for _ in range(n))
    px, py, ph = [[x, y, h] for x, y, h in xyh if h > 0][0]
    for cx in range(101):
        for cy in range(101):
            H = ph + abs(cx - px) + abs(cy - py)
            if all(hi == max(H - abs(cx - xi) - abs(cy - yi), 0) for xi, yi, hi in xyh):
                return " ".join([str(cx), str(cy), str(H)])


if __name__ == "__main__":
    print(resolve())
