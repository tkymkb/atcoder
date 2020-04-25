def solve():
    n = int(input())
    max_cake = n // 4
    max_donut = n // 7
    for c in range(max_cake + 1):
        for d in range(max_donut + 1):
            if n == 4 * c + 7 * d:
                return "Yes"
    return "No"


if __name__ == "__main__":
    print(solve())
