def resolve():
    a, b = map(int, input().split())
    div_a = set(prime_factorize(a))
    div_b = set(prime_factorize(b))
    print(len(div_a & div_b) + 1)
    # print(div_a)
    # print(div_b)


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


if __name__ == "__main__":
    resolve()
