# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

l, n, m = map(int, input().split())
data = list(list(map(int, input().split())) for _ in range(m))
print(l, n, m)
print(sorted(data, key=lambda x: x[0]))
bottom_left = sorted([bar for bar in data if bar[0] == 1], key=lambda x: -x[1])[0]
data.remove(bottom_left)
now_x, now_y = 2, bottom_left[2]
print("bottom_left", bottom_left)

# bar[0]: 縦棒(x), bar[1]: 出発y, bar[2]: 到着y
nex = []
for bar in data:
    candidates = []
    # 出発点が今の縦棒
    print("bar", bar)
    if bar[0] == now_x and bar[1] < now_y:
        candidates.append([bar[1], bar])
    # 出発点が今の縦棒の一つ左
    elif bar[0] == now_x - 1 and bar[1] < now_y:
        candidates.append([bar[2], bar])
    print("cand", candidates)
    nex = max(candidates, key=lambda x: x[0])
    print(next)

# next1 = sorted([bar for bar in data if bar[0] == 2 and bar[1] < bottom_left[1]], key=lambda x: -x[1])[0]
# next2 = sorted([bar for bar in data if bar[0] == 3 and bar[1] < next1[2]], key=lambda x: -x[1])[0]
# print(sorted(data, key=lambda x: x[0]))
# print(bottom_left)
# print(next1)
# print(next2)

