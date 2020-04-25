def resolve():
    n, a, b = map(int, input().split())
    sd = list(list(input().split()) for _ in range(n))
    x = 0
    for s, d in sd:
        p = 0
        d = int(d)
        if d < a:
            p = a
        elif a <= d <= b:
            p = d
        else:
            p = b
        if s == "West":
            x -= p
        else:
            x += p
    if x < 0:
        print("West", -x)
    elif x > 0:
        print("East", x)
    else:
        print("0")


if __name__ == "__main__":
    resolve()
