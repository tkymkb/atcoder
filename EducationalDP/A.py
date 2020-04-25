def resolve():
    u"""
    もらうDP
    """
    n = int(input())
    h = list(map(int, input().split()))
    dp = [10 ** 9] * n
    dp[0] = 0
    dp[1] = abs(h[1] - h[0])
    for i in range(2, n):
        dp[i] = min(dp[i - 1] + abs(h[i - 1] - h[i]), dp[i - 2] + abs(h[i - 2] - h[i]))
    print(dp[-1])


if __name__ == "__main__":
    resolve()
