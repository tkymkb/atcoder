def resolve():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    bc = list(list(map(int, input().split())) for _ in range(m))
    pairs = [(ai, 1) for ai in a]
    for b, c in bc:
        pairs.append((c, b))
    pairs.sort(key=lambda x: x[0], reverse=True)
    c = 0
    ans = 0
    for v, num in pairs:
        if c + num <= n:
            ans += v * num
            c += num
        else:
            ans += v * (n - c)
            break
    print(ans)


if __name__ == "__main__":
    resolve()
