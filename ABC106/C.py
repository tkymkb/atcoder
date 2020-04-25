def solve():
    s = input()
    k = int(input())
    head_ones = 0
    for c in s:
        if c != "1":
            break
        else:
            head_ones += 1
    return "1" if head_ones >= k else [c for c in s if c != "1"][0]


if __name__ == "__main__":
    print(solve())
