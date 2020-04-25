def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    neg = 0
    pos = []
    for ai, bi in zip(a, b):
        if ai < bi:
            neg += bi - ai
            ans += 1
        else:
            pos.append(ai - bi)
    if neg > sum(pos):
        print(-1)
        return 0
    pos.sort()
    for pi in pos[::-1]:
        if neg <= 0:
            break
        neg -= pi
        ans += 1
    print(ans)


if __name__ == "__main__":
    resolve()
