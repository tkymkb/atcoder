def resolve():
    h, w = list(map(int, input().split()))
    s = list(input() for _ in range(h))
    for row in s:
        for idx, cell in enumerate(row):
            if cell == ".":




if __name__ == "__main__":
    resolve()
