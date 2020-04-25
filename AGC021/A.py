def resolve():
    n = int(input())
    ns = str(n)
    ln = len(ns)
    left = int(ns[0])
    c1 = int(str(left) + "9" * (ln - 1))
    c2 = int(str(left - 1) + "9" * (ln - 1))
    if c1 <= int(n):
        print(sum([int(ci) for ci in str(c1)]))
    else:
        print(sum([int(ci) for ci in str(c2)]))


if __name__ == "__main__":
    resolve()
