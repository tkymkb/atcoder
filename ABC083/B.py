def resolve():
    n = int(input())
    s = list(input() for _ in range(n))
    m = int(input())
    t = list(input() for _ in range(m))
    words = set(s)
    ans = []
    for w in words:
        ans.append(s.count(w) - t.count(w))
    print(max(ans) if max(ans) > 0 else 0)


if __name__ == "__main__":
    resolve()
