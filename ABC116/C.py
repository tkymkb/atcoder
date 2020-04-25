def resolve():
    n = int(input())
    h = list(map(int, input().split()))
    res = 0
    for height in range(1, max(h) + 1):
        flag = False
        for i in range(n):
            if h[i] >= height and not flag:
                flag = True
                res += 1
            elif h[i] < height:
                flag = False
    print(res)


if __name__ == "__main__":
    resolve()
