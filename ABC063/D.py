import heapq


def resolve():
    n, a, b = map(int, input().split())
    h = []
    for _ in range(n):
        heapq.heappush(h, -int(input()))
    ans = 0
    while any([True for hi in h if hi < 0]):
        bombed = heapq.heappop(h)
        h = [hi + b for hi in h]
        heapq.heappush(h, bombed + a)
        ans += 1
    print(ans)

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
        input = """4 5 3
8
7
4
2"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2 10 4
20
20"""
        output = """4"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """5 2 1
900000000
900000000
1000000000
1000000000
1000000000"""
        output = """800000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
    resolve()
