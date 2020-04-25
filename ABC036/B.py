def resolve():
    n = int(input())
    s = list(list(input()) for _ in range(n))
    for i in range(n):
        print("".join([l[i] for l in s[::-1]]))


if __name__ == "__main__":
    resolve()
