def resolve():
    n = int(input())
    b = list(map(int, input().split()))
    a = [b[0]]
    for i in range(1, n - 1):
        a.append(min(b[i - 1], b[i]))
    a.append(b[-1])
    print(sum(a))


if __name__ == "__main__":
    resolve()
