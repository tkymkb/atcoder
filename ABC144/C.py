def resolve():
    n = int(input())
    for i in range(2, int(n ** 0.5) + 1)[::-1]:
        if n % i == 0:
            ans = i + n // i - 2
            print(ans)
            return 0
    print(n - 1)


if __name__ == "__main__":
    resolve()
