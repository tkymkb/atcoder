def resolve():
    a, b = input().split()
    if (a, b) == ("H", "H") or (a, b) == ("D", "D"):
        print("H")
    elif (a, b) == ("H", "D") or (a, b) == ("D", "H"):
        print("D")


if __name__ == "__main__":
    resolve()
