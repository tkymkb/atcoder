def solve():
    n = int(input())
    a = list(map(int, input().split()))
    return sum([count(ai) for ai in a if ai % 2 == 0])


def count(n):
    ans = 0
    while n % 2 == 0:
        ans += 1
        n /= 2
    return ans


if __name__ == "__main__":
    print(solve())
