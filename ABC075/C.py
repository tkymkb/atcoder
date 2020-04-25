def solve():
    s = input()
    t = input()
    ls = len(s)
    lt = len(t)
    for i in range(ls - lt + 1)[::-1]:
        if all([si == ti or si == "?" for si, ti in zip(s[i:i + lt], t)]):
            return (s[:i] + t + s[i + lt:]).replace("?", "a")
    return "UNRESTORABLE"


def resolve():
    print(solve())


if __name__ == "__main__":
    resolve()
