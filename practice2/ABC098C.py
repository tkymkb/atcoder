def solve():
    n = int(input())
    people = input()
    # ans = people[1:].count("E")
    # x = ans
    # for i in range(n):
    #     if people[i - 1] == "W":
    #         x += 1
    #     if people[i] == "E":
    #         x -= 1
    #     ans = min(ans, x)
    # return ans
    return min([people[:i].count("W") + people[i + 1:].count("E") for i in range(n)])


if __name__ == "__main__":
    print(solve())
