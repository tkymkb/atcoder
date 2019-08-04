def solve():
    h, w = list(map(int, input().split()))
    field = [["."] * (w + 2)] + [["."] + list(input()) + ["."] for _ in range(h)] + [["."] * (w + 2)]
    # result = [[0] * (w + 2)] * (h + 2)

    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if field[i][j] == ".":
                count = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if field[i + dx][j + dy] == "#":
                            count += 1
                field[i][j] = str(count)

    for i in range(1, h + 1):
        print(''.join([str(e) for e in field[i][1:w + 1]]))


if __name__ == "__main__":
    solve()
