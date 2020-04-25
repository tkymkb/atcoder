def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    res = 1
    mode = "0"
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            if mode == "+":
                res += 1
                mode = "0"
            else:
                mode = "-"
        elif a[i] < a[i + 1]:
            if mode == "-":
                res += 1
                mode = "0"
            else:
                mode = "+"
    print(res)


if __name__ == "__main__":
    resolve()
