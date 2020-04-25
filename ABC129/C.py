def resolve():
    n, m = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    is_safe = [True] * (n + 1)
    broken = list(int(input()) for _ in range(m))
    for b in broken:
        is_safe[b] = False

    steps = [1] + [0] * n
    if is_safe[1]:
        steps[1] = 1
    for i in range(2, n + 1):
        if is_safe[i - 1]:
            steps[i] += steps[i - 1]
        if is_safe[i - 2]:
            steps[i] += steps[i - 2]
        steps[i] %= mod
    print(steps[n])


if __name__ == "__main__":
    resolve()
