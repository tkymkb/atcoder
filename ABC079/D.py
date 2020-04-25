def resolve():
    h, w = map(int, input().split())
    c = list(list(map(int, input().split())) for _ in range(10))
    a = list(list(map(int, input().split())) for _ in range(h))
    for k in range(10):  # 経由
        for i in range(10):  # 始点
            for j in range(10):  # 終点
                c[i][j] = min(c[i][j], c[i][k] + c[k][j])
    costs = [c[i][1] for i in range(10)]
    costs += [0]  # -1の分
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += costs[a[i][j]]
    print(ans)


if __name__ == "__main__":
    resolve()
