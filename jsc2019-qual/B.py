def resolve():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    count = 0
    for i, ai in enumerate(a):
        nl = sum(x < ai for x in a[:i])
        nr = sum(x < ai for x in a[i + 1:])
        count += k // 2 * nr * (k + 1) + nl * (k - 1) * (k - 2) // 2
        count %= mod
    print(count)


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
        input = """2 2
2 1"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 5
1 1 1"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """10 998244353
10 9 8 7 5 6 3 4 2 1"""
        output = """185297239"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
    resolve()
