def resolve():
    s = input()
    ls = len(s)
    for i in range(ls):
        for j in range(i, ls):
            if s[:i] + s[j:] == "keyence":
                print("YES")
                return 0
    print("NO")
    return 0


if __name__ == "__main__":
    resolve()
