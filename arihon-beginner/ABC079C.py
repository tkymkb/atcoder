def solve():
    cs = [c for c in input()]
    for i in range(2 ** 3):
        symbols = ["+" if b == "0" else "-" for b in list('{:03b}'.format(i))] + [""]
        formula = "".join([x[0] + x[1] for x in zip(cs, symbols)])
        if eval(formula) == 7:
            return formula + "=7"


if __name__ == "__main__":
    print(solve())
