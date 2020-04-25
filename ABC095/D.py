def resolve():
    n, c = list(map(int, input().split()))
    xv = sorted(list(list(map(int, input().split())) for _ in range(n)), key=lambda x: x[0])
    now, cal = 0, 0
    for x, v in xv:
        d = get_dist(now, x)
        if d < v:
            now = x
            cal += v - d
        xv.remove([x, v])
        xv.sort(key=lambda x: get_dist(now, x[0]))
    print(cal)




def get_dist(now, pos):
    dist = abs(now - pos)
    if dist > 10:
        dist -= 20
    return abs(dist)

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
        input = """3 20
2 80
9 120
16 1"""
        output = """191"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 20
2 80
9 1
16 120"""
        output = """192"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """1 100000000000000
50000000000000 1"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """15 10000000000
400000000 1000000000
800000000 1000000000
1900000000 1000000000
2400000000 1000000000
2900000000 1000000000
3300000000 1000000000
3700000000 1000000000
3800000000 1000000000
4000000000 1000000000
4100000000 1000000000
5200000000 1000000000
6600000000 1000000000
8000000000 1000000000
9300000000 1000000000
9700000000 1000000000"""
        output = """6500000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
    resolve()
