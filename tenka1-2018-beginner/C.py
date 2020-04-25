def resolve():
    n = int(input())
    a = list(int(input()) for _ in range(n))
    a.sort()
    ans = []
    for i in range(n):
        if i % 2:
            now = a.pop()
        else:
            now = a.pop(0)
        ans.append(now)
    print(ans)
    b = 0
    for i in range(n - 1):
        b += abs(ans[i + 1] - ans[i])
    print(b)


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
        input = """5
6
8
1
2
3"""
        output = """21"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """6
3
1
4
1
5
9"""
        output = """25"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """3
5
5
1"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
    resolve()
