# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！


def solve():
    h, w = map(int, input().split())
    moves = {("r", "\\"): "d", ("r", "/"): "u",
             ("l", "\\"): "u", ("l", "/"): "d",
             ("u", "\\"): "l", ("u", "/"): "r",
             ("d", "\\"): "r", ("d", "/"): "l"}
    diffs = {"r": (1, 0), "l": (-1, 0), "u": (0, -1), "d": (0, 1)}

    box = list(input() for _ in range(h))
    now_x, now_y, direction = 0, 0, "r"
    count = 0
    while not (now_x > w - 1 or now_x < 0 or now_y > h - 1 or now_y < 0):
        count += 1
        if box[now_y][now_x] != "_":
            direction = moves[(direction, box[now_y][now_x])]
        diff_x, diff_y = diffs[direction]
        now_x += diff_x
        now_y += diff_y
    return count


if __name__ == "__main__":
    print(solve())
