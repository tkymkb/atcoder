def resolve():
    s = input()
    count = [s.count(c) for c in "abc"]
    if max(count) - min(count) < 2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    resolve()
