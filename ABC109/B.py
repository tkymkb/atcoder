def solve():
    n = int(input())
    w = list(input() for _ in range(n))
    if len(set(w)) != n:
        return "No"
    for i in range(n - 1):
        if w[i][-1] != w[i + 1][0]:
            return "No"
    return "Yes"


if __name__ == "__main__":
    print(solve())
