def solve():
    n = int(input())
    buttons = [int(input()) for _ in range(n)]
    c = 1
    now = buttons[0]  # button1
    while now != 2 and c < n:
        c += 1
        now = buttons[now - 1]
    return c if c < n else -1


if __name__ == "__main__":
    print(solve())
