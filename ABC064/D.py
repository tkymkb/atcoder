def resolve():
    s = input()
    tmp = s
    while "()" in tmp:
        tmp = tmp.replace("()", "")
    l = tmp.count(")")
    r = tmp.count("(")
    ans = "(" * l + s + ")" * r
    print(ans)


if __name__ == "__main__":
    resolve()
