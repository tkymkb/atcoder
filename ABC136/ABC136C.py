def solve():
    n = int(input())
    hs = list(map(int, input().split()))
    for i in reversed(range(n)):
        if i == 0:
            return "Yes"
        elif hs[i - 1] - hs[i] > 1:
            return "No"
        elif hs[i - 1] - hs[i] == 1:
            hs[i - 1] -= 1
        else:
            continue
    return "Yes"


if __name__ == "__main__":
    print(solve())
