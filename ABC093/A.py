def resolve():
    s = input()
    ans = "Yes" if all([True if c in s else False for c in ["a", "b", "c"]]) else "No"
    print(ans)


if __name__ == "__main__":
    resolve()
