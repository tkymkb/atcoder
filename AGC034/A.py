def resolve():
    n, a, b, c, d = list(map(int, input().split()))
    s = input()
    if "##" in s[a - 1:c] or "##" in s[b - 1:d]:
        print("No")
        return 0

    if c < d:
        print("Yes")
    else:
        if "..." in s[b - 2:d + 1]:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    resolve()
