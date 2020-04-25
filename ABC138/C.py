def resolve():
    n = int(input())
    v = sorted(list(map(int, input().split())))
    while len(v) > 2:
        new_v = [sum(v[:2]) / 2] + v[2:]
        v = new_v
    print(sum(v) / 2)


if __name__ == "__main__":
    resolve()
