def resolve():
    n = int(input())
    s = list(int(input()) for _ in range(n))
    non0 = [si for si in s if not str(si).endswith("0")]
    total = sum(s)
    if not str(total).endswith("0"):
        print(total)
    elif non0:
        print(total - min(non0))
    else:
        print(0)


if __name__ == "__main__":
    resolve()
