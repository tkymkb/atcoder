def resolve():
    x, y = map(int, input().split())
    c = []
    for i in range(1 << 2):
        ans = 0
        _x, _y = x, y
        if i & 1:
            _x *= -1
            ans += 1
        if i & 2:
            _y *= -1
            ans += 1
        if _x <= _y:
            ans += _y - _x
            c.append(ans)
    print(min(c))


if __name__ == "__main__":
    resolve()
