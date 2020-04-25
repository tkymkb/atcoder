def resolve():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    dp = [10 ** 9] * n
    dp[0] = 0
    dp[1] = abs(h[1] - h[0])
    for i in range(2, n):
        for j in range(1, min(k + 1, i + 1)):
            dp[i] = min(dp[i], dp[i - j] + abs(h[i] - h[i - j]))
    print(dp[-1])


if __name__ == "__main__":
    resolve()

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
        input = """5 3
10 30 40 50 20"""
        output = """30"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 1
10 20 10"""
        output = """20"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """2 100
10 10"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """10 4
40 10 20 70 80 10 20 70 80 60"""
        output = """40"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
