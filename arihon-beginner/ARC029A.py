def solve():
    n = int(input())
    times = list(int(input()) for _ in range(n))
    shortest = 50 * 4
    for i in range(2 ** n):
        form = '{' + ':0{num}b'.format(num=str(n)) + '}'
        grill = list(form.format(i))
        t0, t1 = 0, 0
        for t, g in zip(times, grill):
            if g == '0':
                t0 += t
            else:
                t1 += t
        result = max(t0, t1)
        if result < shortest:
            shortest = result
    return shortest


if __name__ == "__main__":
    print(solve())
