import fractions


def solve():
    a, b, c, d = map(int, input().split())
    lcm = c * d // fractions.gcd(c, d)
    div_c = b // c - (a - 1) // c
    div_d = b // d - (a - 1) // d
    div_cd = b // lcm - (a - 1) // lcm
    return (b - a + 1) - div_c - div_d + div_cd


if __name__ == "__main__":
    print(solve())
