def solve():
    h, w = list(map(int, input().split()))
    field = [["."] * (w + 2)] + [["."] + list(input()) + ["."] for _ in range(h)] + [["."] * (w + 2)]
    for i in range(1, h + 2):
        for j in range(1, w + 2):
            if field[i][j] == "#" and not is_paintable(field, i, j):
                return "No"
    return "Yes"


def is_paintable(field: list, i: int, j: int):
    return "#" in [field[i - 1][j], field[i + 1][j], field[i][j - 1], field[i][j + 1]]


if __name__ == "__main__":
    print(solve())
