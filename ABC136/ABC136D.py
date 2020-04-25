def solve():
    s = list(input())
    kids = [0] * len(s)
    for i in range(len(s)):
        diff, steps = 0, 0
        now = s[i]
        tonari = s[i + 1] if now == "R" else s[i - 1]
        while now == tonari:
            if now == "R":
                diff += 1
                steps += 1
            else:
                diff -= 1
                steps += 1
            now = tonari
            tonari = s[i + diff]

        if steps % 2:
            kids[i + diff + 1] += 1
        else:
            kids[i + diff] += 1

    return " ".join([str(k) for k in kids])


def solve2():
    s = list(input())
    kids = [0] * len(s)
    for i in range(len(s)):
        diff, steps = 0, 0
        next_idx = i + 1 if s[i] == "R" else i - 1
        now_idx = i
        while now_idx == next_idx:
            if s[now_idx] == "R":
                steps += 1
                next_idx = now_idx + 1
            else:
                steps += 1
                next_idx = now_idx - 1
            now_idx = next_idx
        if steps % 2 and s[i] == "R":
            kids[now_idx + 1] += 1
        elif steps % 2 and s[i] == "L":
            kids[now_idx - 1] += 1
        elif not steps % 2 and s[i] == "R":
            kids[now_idx] += 1
        elif not steps % 2 and s[i] == "L":
            kids[now_idx] += 1

    return " ".join([str(k) for k in kids])


if __name__ == "__main__":
    print(solve())
