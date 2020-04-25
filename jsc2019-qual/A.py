def resolve():
    m, d = map(int, input().split())
    if d < 22:
        return 0
    count = 0
    for mi in range(4, m + 1):
        for di in range(22, d + 1):
            d10, d1 = str(di)
            if int(d10) * int(d1) == mi and int(d1) > 1:
                count += 1
    return count


if __name__ == "__main__":
    print(resolve())
