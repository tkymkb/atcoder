def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    odd = a[::2]
    even = a[1::2]
    if n % 2:
        ans = odd[::-1] + even
    else:
        ans = even[::-1] + odd
    print(*ans)


if __name__ == "__main__":
    resolve()
