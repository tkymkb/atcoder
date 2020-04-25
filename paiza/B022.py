# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

m, n, k = map(int, input().split())
speech = list(int(input()) for _ in range(k))
votes = [0] * m + [n]
for s in speech:
    new_votes = 0
    for idx, v in enumerate(votes):
        if idx != s - 1 and v > 0:
            votes[idx] -= 1
            new_votes += 1
    votes[s - 1] += new_votes

ans = "\n".join([str(i + 1) for i, v in enumerate(votes[:-1]) if v == max(votes[:-1])])
print(ans)
