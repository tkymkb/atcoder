def resolve():
    s = input()
    k = int(input())
    ans = set()
    for i in range(len(s) - k + 1):
        ans.add(s[i:i + k])
    print(len(ans))


if __name__ == "__main__":
    resolve()
