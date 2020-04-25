def resolve():
    n = int(input())
    s = input()
    x = 0
    ans = 0
    for c in s:
        x += 1 if c == "I" else -1
        if x > ans:
            ans = x
    print(ans)


if __name__ == "__main__":
    resolve()
