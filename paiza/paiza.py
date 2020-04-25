# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

input_line = input()
leet = {"A": "4", "E": "3", "G": "6", "I": "1", "O": "0", "S": "5", "Z": "2"}
ans = ""
for c in input_line:
    if c in leet:
        converted = leet[c]
    else:
        converted = c
    ans += converted
print(ans)
