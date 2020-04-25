def resolve():
    o = input()
    e = input()
    if len(o) == len(e):
        ans = "".join([oi + ei for oi, ei in zip(o, e)])
    elif len(o) > len(e):
        ans = "".join([oi + ei for oi, ei in zip(o, e)]) + o[-1]
    else:
        ans = "".join([oi + ei for oi, ei in zip(o, e)]) + e[-1]
    print(ans)


if __name__ == "__main__":
    resolve()
