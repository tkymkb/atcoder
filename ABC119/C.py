def resolve():
    N, A, B, C = map(int, input().split())
    l = list(int(input()) for _ in range(N))

    def rec(i, a, b, c):
        if i == N:
            if not a or not b or not c:
                return 10 ** 9
            else:
                return abs(A - a) + abs(B - b) + abs(C - c) - 30
        ret0 = rec(i + 1, a, b, c)
        ret1 = rec(i + 1, a + l[i], b, c) + 10
        ret2 = rec(i + 1, a, b + l[i], c) + 10
        ret3 = rec(i + 1, a, b, c + l[i]) + 10
        return min([ret0, ret1, ret2, ret3])

    print(rec(0, 0, 0, 0))


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
        input = """5 100 90 80
98
40
30
21
80"""
        output = """23"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """8 100 90 80
100
100
90
90
90
80
80
80"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """8 1000 800 100
300
333
400
444
500
555
600
666"""
        output = """243"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()