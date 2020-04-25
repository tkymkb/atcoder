def resolve():
    n = int(input())
    s = input()
    b_left, w_right = 0, s.count(".")
    ans = n
    for c in s:
        if c == "#":
            b_left += 1
        else:
            w_right -= 1
        if b_left + w_right < ans:
            ans = b_left + w_right
    print(ans)


if __name__ == "__main__":
    resolve()
