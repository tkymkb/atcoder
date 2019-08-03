def solve():
    n, y = list(map(int, input().split()))
    for man in range(n + 1):
        for gosen in range(n - man + 1):
            sen = n - man - gosen
            total = 10000 * man + 5000 * gosen + 1000 * sen
            if total == y:
                return ' '.join([str(man), str(gosen), str(sen)])
    return ' '.join(["-1", "-1", "-1"])


if __name__ == "__main__":
    print(solve())
