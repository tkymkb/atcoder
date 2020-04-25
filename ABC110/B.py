def solve():
    n, m, x, y = map(int, input().split())
    xs = list(map(int, input().split()))
    xs.append(x)
    ys = list(map(int, input().split()))
    ys.append(y)
    return "War" if max(xs) >= min(ys) else "No War"


if __name__ == "__main__":
    print(solve())
