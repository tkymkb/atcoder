def resolve():
    s = input()
    now, ans = 0, 0
    a = [0]
    bottom = 10 ** 18
    for si in s:
        if si == "<":
            now += 1
        else:
            now -= 1
        ans += now
        a.append(now)
        if now < bottom:
            bottom = now
    if bottom < 0:
        ans += -bottom * len(s)
    b = [ai - bottom for ai in a]
    print(a, b, ans, sum(b))

import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """<>>"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """<>>><<><<<<<>>><"""
        output = """28"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
    resolve()
