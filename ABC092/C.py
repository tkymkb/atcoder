def resolve():
    n = int(input())
    a = [0] + list(map(int, input().split())) + [0]
    total = sum([abs(a[i] - a[i + 1]) for i in range(n + 1)])
    for i in range(1, n + 1):
        print(total + abs(a[i + 1] - a[i - 1]) - abs(a[i] - a[i - 1]) - abs(a[i] - a[i + 1]))


if __name__ == "__main__":
    resolve()
