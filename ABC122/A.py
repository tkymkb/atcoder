def solve():
    b = input()
    d = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return d[b]


if __name__ == "__main__":
    print(solve())
