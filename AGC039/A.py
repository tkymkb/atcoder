def resolve():
    s = input()
    k = int(input())
    c = 1
    ls = len(s)
    if len(set(s)) == 1 and ls % 2 == 1:
        if k % 2 == 0:
            ans = ls * (k // 2)
        else:
            ans = ls * (k // 2) + ls // 2
        print(ans)
    else:
        ans = 0
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                c += 1
            else:
                ans += c // 2
                c = 1
        ans += c // 2
        if s[-2] != s[-1] and s[0] == s[-1] and s[0] != s[1]:
            ans += 1
            print(ans * k - 1)
        else:
            print(ans * k)

# abx abx aba
# abxa xbxa xbxa
# abxax abxax abxax

if __name__ == "__main__":
    resolve()
