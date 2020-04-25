def resolve():
    w, h, n = map(int, input().split())
    min_x, min_y = 0, 0
    max_x, max_y = w, h
    for _ in range(n):
        x, y, a = map(int, input().split())
        if a == 1:
            min_x = max(min_x, x)
        elif a == 2:
            max_x = min(max_x, x)
        elif a == 3:
            min_y = max(min_y, y)
        elif a == 4:
            max_y = min(max_y, y)
    if min_x >= max_x or min_y >= max_y:
        print(0)
    else:
        print((max_x - min_x) * (max_y - min_y))


if __name__ == "__main__":
    resolve()
